import os
import tkinter as tk
from tkinter import messagebox
from auth.auth_provider import AuthError
from auth.local_auth import LocalAuthProvider


def get_provider():
    backend = os.getenv("AUTH_BACKEND", "local").lower()
    return  LocalAuthProvider()

provider = get_provider()

root = tk.Tk()
root.title("Smart Elective Advisor — Auth Demo")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack()
mode = tk.StringVar(value="login")

def build_form():
    for w in frame.winfo_children():
        w.destroy()

    tk.Label(frame, text="Smart Elective Advisor").grid(row=0, column=0, columnspan=2)

    if mode.get() == "register":
        tk.Label(frame, text="Full name").grid(row=1, column=0, sticky="e")
        full_name_entry = tk.Entry(frame, width=30)
        full_name_entry.grid(row=1, column=1)
    else:
        full_name_entry = None

    tk.Label(frame, text="Email").grid(row=2 if mode.get() == "register" else 1, column=0, sticky="e")
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=2 if mode.get() == "register" else 1, column=1)

    tk.Label(frame, text="Password").grid(row=3 if mode.get() == "register" else 2, column=0, sticky="e")
    pw_entry = tk.Entry(frame, show="*", width=30)
    pw_entry.grid(row=3 if mode.get() == "register" else 2, column=1)

    if mode.get() == "register":
        tk.Label(frame, text="Confirm Password").grid(row=4, column=0, sticky="e")
        confirm_entry = tk.Entry(frame, show="*", width=30)
        confirm_entry.grid(row=4, column=1)
    else:
        confirm_entry = None

    def do_register():
        if pw_entry.get() != confirm_entry.get():
            messagebox.showerror("Error", "Passwords do not match")
            return
        try:
            result = provider.register_user(full_name_entry.get(), email_entry.get(), pw_entry.get())
            messagebox.showinfo("Success", "User registered successfully!")
            print(result)
        except AuthError as e:
            messagebox.showerror("Register error", str(e))

    def do_login():
        try:
            result = provider.authenticate_user(email_entry.get(), pw_entry.get())
            messagebox.showinfo("Welcome", f"Welcome {result['user']['full_name']}!")
            print(result)
        except AuthError as e:
            messagebox.showerror("Login error", str(e))

    row_btn = 5 if mode.get() == "register" else 3
    if mode.get() == "register":
        tk.Button(frame, text="Register", command=do_register).grid(row=row_btn, column=0, pady=8)
    else:
        tk.Button(frame, text="Login", command=do_login).grid(row=row_btn, column=0, pady=8)

    def toggle():
        mode.set("register" if mode.get() == "login" else "login")
        build_form()

    tk.Button(frame, text="Switch", command=toggle).grid(row=row_btn, column=1, pady=8)

build_form()
root.mainloop()