import customtkinter as ctk
from tkinter import messagebox, simpledialog
from auth.cognito_auth import CognitoAuthProvider, AuthError
from .LoginFrame import LoginFrame
from .themes import *
from .WelcomePage import WelcomePage
from .registerFrame import RegisterFrame
from db import dbsetup, queries
# from HelpFrame import HelpFrame
from .PreferencesFrame import PreferenceFrame
from .ProfileFrame import *
from .CourseFrame import *
# from RecommendedFrame import RecommendedFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.user = queries.get_user('a@csu.fullerton.edu')
        dbsetup.connectdb()
        self.provider = CognitoAuthProvider()
        self.auth_tokens = None

        self.title('Smart Elective Advisor')
        self.geometry('1100x700')
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
                                         width=250,
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


        # create sidebar buttons
        self.selectedButton = 'Home'
        self.buttons = {}  # store a references to buttons
        self.sidebarButton("Home").grid(row=0, column=0, pady=(0, 20))
        self.buttons[self.selectedButton].configure(
            fg_color=FullertonOrange, hover_color=FullertonOrange)

        self.sidebarButton('Login').grid(row=1, column=0, pady=(0, 20))
        self.sidebarButton('Preferences').grid(row=2, column=0, pady=(0, 20))
        self.sidebarButton('Course Search').grid(row=3, column=0, pady=(0, 20))
        self.sidebarButton('Recommended').grid(row=4, column=0, pady=(0, 20))
        self.sidebarButton('Profile').grid(row=5, column=0, pady=(0, 20))
        self.sidebarButton('Help').grid(row=6, column=0)

        #pages
        self.pages = {
            "Home": WelcomePage(self.mainArea),
            "Login": LoginFrame(self.mainArea, self),
            "Register":RegisterFrame(self.mainArea, self),
            "Preferences": PreferenceFrame(self.mainArea),
            # "Recommended": RecommendedFrame(self.mainArea),
            "Course Search": CourseSearchFrame(self.mainArea, self),
            "Courses": CourseFrame(self.mainArea, self),
            "Sections": SectionFrame(self.mainArea, self),
            "Profile": ProfileFrame(self.mainArea, self),
            "Saved": SavedFrame(self.mainArea, self)
            # "Help": HelpFrame(self.mainArea)
        }

        # show welcome page
        self.currentPage = None
        self.show_page('Home')

    def sidebarButton(self, name):
        new_button = ctk.CTkButton(
            self.sidebarFrame,
            text=name,
            height=100,
            border_color=FullertonBlue,
            width=230,
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
        if name in self.buttons and self.selectedButton != name:
            self.buttons[name].configure(
                fg_color=FullertonOrange, hover_color=FullertonOrange)
            self.buttons[self.selectedButton].configure(
                fg_color=FullertonWhite, hover_color=FullertonLightOrange)
            self.selectedButton = name

        self.show_page(name)

    def show_page(self, name):
        if self.currentPage is not None:
            self.currentPage.pack_forget()

        frame = self.pages.get(name)
        if frame is not None:
            self.currentPage = frame
            self.currentPage.pack(fill="both", expand=True, padx=3, pady=3)

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

    def do_resend_code(self, frame):
        email = frame.email_entry.get().strip()
        try:
            self.provider.resend_confirmation(email)
            messagebox.showinfo(
                "Resent", f"Verification code resent to {email}.")
        except AuthError as e:
            frame.warning_label.configure(text_color=AlertRed, text=str(e))

    def do_login(self, frame):
        email = frame.email_entry.get().strip()
        password = frame.password_entry.get()

        if hasattr(frame, "warning_label"):
            frame.warning_label.configure(text="", text_color=AlertRed)

        try:
            tokens = self.provider.authenticate_user(email, password)
            self.auth_tokens = tokens
            self.current_user_email = email
            messagebox.showinfo("Welcome", f"Welcome {email}!")
            self.buttonClicked("Home")
        except AuthError as e:
            if hasattr(frame, "warning_label"):
                frame.warning_label.configure(text=str(e))
            else:
                messagebox.showerror("Login error", str(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()