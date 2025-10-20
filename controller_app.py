import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

import customtkinter as ctk
from tkinter import simpledialog, messagebox

from auth.cognito_auth import CognitoAuthProvider, AuthError

class AppController:
    def __init__(self, root, login_frame_cls, register_frame_cls):
        self.root = root
        self.provider = CognitoAuthProvider()

        # container
        self.container = ctk.CTkFrame(root)
        self.container.pack(fill="both", expand=True)

        # build frames
        self.frames = {}
        self.frames["Login"] = login_frame_cls(self.container, controller=self)
        self.frames["Register"] = register_frame_cls(self.container, controller=self)

        # show default
        self.buttonClicked("Login")

    def buttonClicked(self, name: str):
        for f in self.frames.values():
            f.grid_forget()
        frame = self.frames[name]
        frame.grid(row=0, column=0, sticky="nsew")

    # Actions called by frames 
    def do_register(self, frame):
        full_name = frame.name_entry.get().strip()
        email     = frame.email_entry.get().strip()
        password  = frame.password_entry.get()
        confirm   = frame.confirm_entry.get()

        frame.warning_label.configure(text_color=frame.cget("fg_color"))  # clear

        if password != confirm:
            frame.warning_label.configure(text_color="red", text="Passwords do not match.")
            return
        try:
            msg = self.provider.register_user(full_name, email, password)
            messagebox.showinfo("Verify", msg)

            code = simpledialog.askstring("Confirm", f"Enter the 6-digit code sent to {email}")
            if code:
                self.provider.confirm_sign_up(email, code.strip())
                messagebox.showinfo("Confirmed", "Email verified. You can now log in.")
                self.buttonClicked("Login")
        except AuthError as e:
            frame.warning_label.configure(text_color="red", text=str(e))

    def do_resend_code(self, frame):
        email = frame.email_entry.get().strip()
        try:
            self.provider.resend_confirmation(email)
            messagebox.showinfo("Resent", f"Verification code resent to {email}.")
        except AuthError as e:
            frame.warning_label.configure(text_color="red", text=str(e))

    def do_login(self, frame):
        email    = frame.email_entry.get().strip()
        password = frame.password_entry.get()
        try:
            tokens = self.provider.authenticate_user(email, password)
            messagebox.showinfo("Welcome", f"Welcome {email}!")
        except AuthError as e:
            frame_title = getattr(frame, "title", None)
            if hasattr(frame, "warning_label"):
                frame.warning_label.configure(text_color="red", text=str(e))
            else:
                messagebox.showerror("Login error", str(e))