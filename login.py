import os
from pathlib import Path
from dotenv import load_dotenv

# Load the .env file that sits next to gui.py
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

import tkinter as tk
from tkinter import messagebox, simpledialog
from auth.auth_provider import AuthError
import ui.gui
from auth.cognito_auth import CognitoAuthProvider

# or pick provider by env var if you already have that logic

provider = CognitoAuthProvider()

root = tk.Tk()
root.title("Smart Elective Advisor — Cognito Auth")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack()
mode = tk.StringVar(value="login")

def build():
    for w in frame.winfo_children(): w.destroy()
    tk.Label(frame, text="Smart Elective Advisor").grid(row=0, column=0, columnspan=3, pady=(0,8))

    if mode.get() == "register":
        tk.Label(frame, text="Full name").grid(row=1, column=0, sticky="e")
        full = tk.Entry(frame, width=30); full.grid(row=1, column=1, columnspan=2)
    else:
        full = None

    tk.Label(frame, text="Email").grid(row=2 if mode.get()=="register" else 1, column=0, sticky="e")
    email = tk.Entry(frame, width=30); email.grid(row=2 if mode.get()=="register" else 1, column=1, columnspan=2)

    tk.Label(frame, text="Password").grid(row=3 if mode.get()=="register" else 2, column=0, sticky="e")
    pw = tk.Entry(frame, show="*", width=30); pw.grid(row=3 if mode.get()=="register" else 2, column=1, columnspan=2)

    if mode.get()=="register":
        tk.Label(frame, text="Confirm Password").grid(row=4, column=0, sticky="e")
        pw2 = tk.Entry(frame, show="*", width=30); pw2.grid(row=4, column=1, columnspan=2)
    else:
        pw2 = None

    def do_register():
        try:
            if pw.get() != pw2.get():
                messagebox.showerror("Error", "Passwords do not match")
                return
            res = provider.register_user(full.get().strip(), email.get().strip(), pw.get())
            messagebox.showinfo("Verify", res.get("message", "Check your email for a verification code."))
        except AuthError as e:
            messagebox.showerror("Register", str(e))

    def do_confirm():
        try:
            addr = email.get().strip()
            code = simpledialog.askstring("Confirm", f"Enter code sent to {addr}")
            if not code: return
            provider.confirm_sign_up(addr, code.strip())
            messagebox.showinfo("Confirm", "Email verified. You can now log in.")
        except AuthError as e:
            messagebox.showerror("Confirm", str(e))

    def do_resend():
        try:
            provider.resend_confirmation_code(email.get().strip())
            messagebox.showinfo("Resend", "Verification code re-sent.")
        except AuthError as e:
            messagebox.showerror("Resend", str(e))

    def do_login():
        try:
            res = provider.authenticate_user(email.get().strip(), pw.get())
            name = res["user"].get("full_name") or res["user"]["email"]
            messagebox.showinfo("Welcome", f"Welcome {name}!")
            # tokens available: res["tokens"]["IdToken"], ["AccessToken"], ["RefreshToken"]
        except AuthError as e:
            messagebox.showerror("Login", str(e))

    row_btn = 5 if mode.get()=="register" else 3
    if mode.get()=="register":
        tk.Button(frame, text="Register", command=do_register).grid(row=row_btn, column=0, pady=8, sticky="ew")
        tk.Button(frame, text="Confirm code", command=do_confirm).grid(row=row_btn, column=1, pady=8, sticky="ew")
        tk.Button(frame, text="Resend code", command=do_resend).grid(row=row_btn, column=2, pady=8, sticky="ew")
    else:
        tk.Button(frame, text="Login", command=do_login).grid(row=row_btn, column=0, pady=8, sticky="ew")
        tk.Button(frame, text="Confirm code", command=do_confirm).grid(row=row_btn, column=1, pady=8, sticky="ew")
        tk.Button(frame, text="Resend code", command=do_resend).grid(row=row_btn, column=2, pady=8, sticky="ew")

    def toggle():
        mode.set("register" if mode.get()=="login" else "login"); build()
    tk.Button(frame, text="Switch", command=toggle).grid(row=row_btn+1, column=0, columnspan=3, pady=8, sticky="ew")

build()
root.mainloop()