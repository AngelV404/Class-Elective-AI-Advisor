import sqlite3, time, bcrypt
from typing import Dict, Any, Optional
from .auth_provider import AuthProvider, AuthError, validate_password, generate_jwt, validate_email_domain

MAX_FAILED_ATTEMPTS = 5
LOCKOUT_SECONDS = 5 * 60

class LocalAuthProvider(AuthProvider):
    def __init__(self, db_path="auth.db"):
        self.db_path = db_path
        self._init_db()
    
    def _connect(self):
        return sqlite3.connect(self.db_path)
    
    def _init_db(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash BLOB NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            failed_attempts INTEGER DEFAULT 0,
            lockout_until INTEGER DEFAULT 0
        )
        """)
        conn.commit()
        conn.close()

    def _get_user_row(self, email: str):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, full_name, email, password_hash, failed_attempts, lockout_until FROM users WHERE email=?", (email.lower(),))
        row = cur.fetchone()
        conn.close()
        return row
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        row = self._get_user_row(email)
        if not row:
            return None
        return {
            "id": row[0], "full_name": row[1], "email": row[2],
            "password_hash": row[3], "failed_attempts": row[4], "lockout_until": row[5]
        }

    def register_user(self, full_name: str, email: str, password: str) -> Dict[str, Any]:
        email = email.strip().lower()
        
        err = validate_email_domain(email)
        if err:
            raise AuthError(err)
        
        err = validate_password(password)
        if err:
            raise AuthError(err)

        if self.get_user_by_email(email):
            raise AuthError("Email already registered.")

        pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        conn = self._connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (full_name, email, password_hash) VALUES (?, ?, ?)", (full_name, email, pw_hash))
        conn.commit()
        user_id = cur.lastrowid
        conn.close()

        return {
            "user": {"id": user_id, "full_name": full_name, "email": email},
            "tokens": {"access_token": generate_jwt({"sub": user_id, "email": email})}
        }

    def authenticate_user(self, email: str, password: str) -> Dict[str, Any]:
        row = self._get_user_row(email.strip().lower())
        if not row:
            raise AuthError("Incorrect credentials.")

        id_, full_name, email, pw_hash, failed_attempts, lockout_until = row
        now = int(time.time())

        if lockout_until and now < lockout_until:
            raise AuthError("Account locked. Try again later.")

        if not bcrypt.checkpw(password.encode("utf-8"), pw_hash):
            failed_attempts += 1
            conn = self._connect()
            cur = conn.cursor()
            if failed_attempts >= MAX_FAILED_ATTEMPTS:
                cur.execute("UPDATE users SET failed_attempts=?, lockout_until=? WHERE id=?", (failed_attempts, now + LOCKOUT_SECONDS, id_))
            else:
                cur.execute("UPDATE users SET failed_attempts=? WHERE id=?", (failed_attempts, id_))
            conn.commit()
            conn.close()
            raise AuthError("Incorrect credentials.")
        else:
            conn = self._connect()
            cur = conn.cursor()
            cur.execute("UPDATE users SET failed_attempts=0, lockout_until=0 WHERE id=?", (id_,))
            conn.commit()
            conn.close()
            return {
                "user": {"id": id_, "full_name": full_name, "email": email},
                "tokens": {"access_token": generate_jwt({"sub": id_, "email": email})}
            }

