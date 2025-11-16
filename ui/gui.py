import customtkinter as ctk
from tkinter import messagebox, simpledialog
from auth.cognito_auth import CognitoAuthProvider, AuthError
from auth.auth_provider import validate_password
from .LoginFrame import LoginFrame
from .themes import *
from .WelcomePage import WelcomePage
from .registerFrame import RegisterFrame
from db import dbsetup, queries
from .HelpFrame import HelpFrame
from .PreferencesFrame import PreferencesFrame
from .ProfileFrame import *
from .CourseFrame import *
from .RecommendedFrame import RecommendedFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        dbsetup.connectdb()
        self.user = queries.get_user('a@csu.fullerton.edu')
        
        self.provider = CognitoAuthProvider()
        self.auth_tokens = None
        self.is_logged_in = False

        self.title('Smart Elective Advisor')
        self.geometry('1000x638')
        ctk.set_appearance_mode('light')

        ctk.set_default_color_theme('blue')

        # set up the grid for root window
        self.grid_columnconfigure(0, weight=0)  # sidebar fixed width
        # main area takes the remaining space
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # stretch entire height
        self.configure(fg_color=FullertonWhite)

        # create sidebar frame
        self.sidebarFrame = ctk.CTkFrame(self,
                                         width=210,
                                         corner_radius=0,
                                         border_color=FullertonBlue,
                                         border_width=3)

        self.sidebarFrame.grid(row=0, column=0, sticky='nsew')
        self.sidebarFrame.configure(fg_color=FullertonWhite)
        self.sidebarFrame.grid_propagate(False)

        # create main area frame
        self.mainArea = ctk.CTkFrame(self,
                                     corner_radius=0,
                                     border_color=FullertonBlue,
                                     border_width=3)
        self.mainArea.grid(row=0, column=1, sticky='nsew')
        self.mainArea.configure(fg_color=FullertonWhite)

        self.mainArea.rowconfigure(0, weight=1)
        self.mainArea.columnconfigure(0, weight=1)

        # create sidebar buttons
        self.selectedButton = 'Home'
        self.buttons = {}  # store a references to buttons
        self.sidebarButton("Home").grid(row=0, column=0, pady=(0, 13))
        self.buttons[self.selectedButton].configure(
            fg_color=FullertonOrange, hover_color=FullertonOrange)

        self.sidebarButton('Login').grid(row=1, column=0, pady=(0, 13))
        self.sidebarButton('Preferences').grid(row=2, column=0, pady=(0, 13))
        self.sidebarButton('Course Search').grid(row=3, column=0, pady=(0, 13))
        self.sidebarButton('Recommended').grid(row=4, column=0, pady=(0, 13))
        self.sidebarButton('Profile').grid(row=5, column=0, pady=(0, 13))
        self.sidebarButton('Help').grid(row=6, column=0)

        # pages
        self.pages = {
            "Home": WelcomePage(self.mainArea),
            "Login": LoginFrame(self.mainArea, self),
            "Register": RegisterFrame(self.mainArea, self),
            "Preferences": PreferencesFrame(self.mainArea,self),
            "Recommended": RecommendedFrame(self.mainArea),
            "Course Search": CourseSearchFrame(self.mainArea, self),
            "Courses": CourseFrame(self.mainArea, self),
            "Sections": SectionFrame(self.mainArea, self),
            "Profile": ProfileFrame(self.mainArea, self),
            "Saved": SavedFrame(self.mainArea, self),
            "Help": HelpFrame(self.mainArea)
        }

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
            page.grid_remove()

        # show welcome page
        self.currentPage = None
        self.show_page('Home')

    def sidebarButton(self, name):
        new_button = ctk.CTkButton(
            self.sidebarFrame,
            text=name,
            height=80,
            border_color=FullertonBlue,
            width=190,
            border_width=3,
            font=regular_font,
            text_color=FullertonBlue,
            hover_color=FullertonLightOrange,
            fg_color=FullertonWhite,
            corner_radius=0,
            command=lambda: self.buttonClicked(name)
        )
        self.buttons[name] = new_button

        return new_button

    def buttonClicked(self, name):
        if not self.is_logged_in and name not in ('Login', 'Home'):
            messagebox.showinfo('','Please Login or Register to Continue')
        else:
            if name in self.buttons and self.selectedButton != name:
                self.buttons[name].configure(
                    fg_color=FullertonOrange, hover_color=FullertonOrange)
                self.buttons[self.selectedButton].configure(
                    fg_color=FullertonWhite, hover_color=FullertonLightOrange)
                self.selectedButton = name

            self.show_page(name)

    def show_page(self, name):


            if self.currentPage is not None:
                self.currentPage.grid_remove()

            frame = self.pages.get(name)
            if frame is not None:
                self.currentPage = frame
                frame.grid()

    # Actions called by frames
    def do_register(self, frame):
        full_name = frame.name_entry.get().strip()
        email = frame.email_entry.get().strip()
        password = frame.password_entry.get()
        confirm = frame.confirm_entry.get()

        frame.warning_label.configure(text="", text_color=FullertonWhite)

        if password != confirm:
            frame.warning_label.configure(text_color=AlertRed,
                                          text="Passwords do not match.")
            return
        try:
            msg = self.provider.register_user(full_name, email, password)
            messagebox.showinfo("Verify", msg)

            code = simpledialog.askstring(
                "Confirm", f"Enter the 6-digit code sent to {email}")
            if code:
                self.provider.confirm_sign_up(email, code.strip())
                messagebox.showinfo(
                    "Confirmed", "Email verified. You can now log in.")
                self.buttonClicked("Login")
        except AuthError as e:
            frame.warning_label.configure(text_color=AlertRed, text=str(e))

    def do_logout(self):
        confirm = messagebox.askyesno(
            "Logout", "Are you sure you want to log out?")
        if confirm:
            self.auth_tokens = None
            self.current_user_email = None
            self.is_logged_in = False
            self.user = None

            messagebox.showinfo(
                "Logged out", "You have been logged out successfully.")

            # Clear password fields
            login_frame = self.pages.get("Login")
            if login_frame:
                login_frame.password_entry.delete(0, "end")
                login_frame.email_entry.delete(0, "end")
            if "Login" in self.buttons:
                self.buttons["Login"].configure(
                    text="Login", command=lambda: self.buttonClicked("Login"))
                
            self.selectedButton = "Login"
            self.buttonClicked("Login")

    def do_resend_code(self, frame):
        email = frame.email_entry.get().strip()
        try:
            self.provider.resend_confirmation(email)
            messagebox.showinfo(
                "Resent", f"Verification code resent to {email}.")
        except AuthError as e:
            frame.warning_label.configure(text_color=AlertRed, text=str(e))

    def do_forgot_password(self, frame):
        email = frame.email_entry.get().strip()
        if not email:
            messagebox.showerror("Missing email", "Please enter your email to reset your password.")
            return
        try:
            self.provider.start_password_reset(email)
            messagebox.showinfo("Password reset", f"A verification code was sent to {email}.")
            code = simpledialog.askstring("Reset Code", "Enter the verification code from your email:")
            if not code:
                return
            new_password = simpledialog.askstring("New Password", "Enter your new password:", show='*')
            if not new_password:
                return
            confirm_password = simpledialog.askstring("Confirm Password", "Confirm your new password:", show='*')
            if new_password != confirm_password:
                messagebox.showerror("Mismatch", "Passwords do not match.")
                return
            err = validate_password(new_password)
            if err:
                messagebox.showerror("Invalid password", err)
                return
            self.provider.confirm_password_reset(email, code.strip(), new_password)
            messagebox.showinfo("Updated", "Your password has been reset. Please log in.")
            self.buttonClicked("Login")
        except AuthError as e:
            messagebox.showerror("Reset failed", str(e))

    def do_change_password(self, frame=None):
        if not self.is_logged_in or not self.auth_tokens:
            messagebox.showinfo("Login required", "Please log in before changing your password.")
            self.buttonClicked("Login")
            return

        access_token = self.auth_tokens.get("tokens", {}).get("AccessToken")
        if not access_token:
            messagebox.showerror("Unavailable", "Unable to change password without an access token.")
            return

        current_password = simpledialog.askstring("Current Password", "Enter your current password:", show='*')
        if not current_password:
            return
        new_password = simpledialog.askstring("New Password", "Enter your new password:", show='*')
        if not new_password:
            return
        confirm_password = simpledialog.askstring("Confirm Password", "Confirm your new password:", show='*')
        if new_password != confirm_password:
            messagebox.showerror("Mismatch", "Passwords do not match.")
            return

        err = validate_password(new_password)
        if err:
            messagebox.showerror("Invalid password", err)
            return

        try:
            self.provider.change_password(access_token, current_password, new_password)
            messagebox.showinfo("Success", "Password changed successfully.")
        except AuthError as e:
            messagebox.showerror("Change failed", str(e))

    def do_login(self, frame):
        email = frame.email_entry.get().strip()
        password = frame.password_entry.get()

        if hasattr(frame, "warning_label"):
            frame.warning_label.configure(text="", text_color=AlertRed)

        try:
            tokens = self.provider.authenticate_user(email, password)
            self.auth_tokens = tokens
            self.current_user_email = email
            try:
                self.user = queries.get_user(email)
            except Exception:
                self.user = None
            messagebox.showinfo("Welcome", f"Welcome {email}!")
            self.buttonClicked("Home")
            self.is_logged_in = True

            if "Login" in self.buttons:
                self.buttons["Login"].configure(
                    text="Logout", command=self.do_logout)

        except AuthError as e:
            if hasattr(frame, "warning_label"):
                frame.warning_label.configure(text=str(e))
            else:
                messagebox.showerror("Login error", str(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()
