import os
import re
try:
    import jwt  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency for tests
    jwt = None  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

JWT_SECRET = os.getenv("JWT_SECRET", "replace-this-secret")
JWT_ALGO = "HS256"
JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", "60"))

class AuthError(Exception):
    pass

class AuthProvider:
    def register_user(self, full_name: str, email: str, password: str) -> Dict[str, Any]:
        raise NotImplementedError

    def authenticate_user(self, email: str, password: str) -> Dict[str, Any]:
        raise NotImplementedError

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError
    
def validate_email_domain(email: str) -> Optional[str]:
    """Ensure email belongs to csu.fullerton.edu domain."""
    if not email.lower().endswith("@csu.fullerton.edu"):
        return "A valid csu.fullerton.edu email is required."
    return None

def validate_password(password: str) -> Optional[str]:
    """Return None if OK, else error message."""
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "Password must include an uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must include a lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must include a digit."
    return None

def generate_jwt(payload: dict) -> str:
    exp = datetime.utcnow() + timedelta(minutes=JWT_EXP_MINUTES)
    payload2 = payload.copy()
    payload2["exp"] = exp
    return jwt.encode(payload2, JWT_SECRET, algorithm=JWT_ALGO)