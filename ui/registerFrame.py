import customtkinter as ctk
from .themes import *


class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent, fg_color=FullertonWhite)
        self.controller=controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(3, weight=3)

        self.title_frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.title_frame.grid(row=0, column=1, sticky="nsew")

        self.title_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text="User Registration",
            font=heading_font,
            fg_color=FullertonWhite
        )
        self.title_label.grid(row=0, column=0, sticky="n",
                              pady=(30, 0), padx=(30, 0))

        self.warning_label = ctk.CTkLabel(
            self.title_frame,
            text="Error Registering",
            font=list_font,
            text_color=FullertonWhite,
            fg_color=FullertonWhite
        )
        self.warning_label.grid(row=1, column=0, sticky="n",
                                pady=(0, 10), padx=(30, 0))


        # user input field
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.grid(row=1, column=1)
        self.entry_frame.configure(fg_color=FullertonWhite)
        self.entry_frame.columnconfigure(1, weight=1)

        # full name label
        self.name_label = createEntryLabel(self.entry_frame, 'Full Name:')
        self.name_label.grid(row=0, column=0, sticky='e', padx=15, pady=10)

        # full name entry box
        self.name_entry = createEntryBox(self.entry_frame)
        self.name_entry.grid(row=0, column=1, padx=(0, 120))

        # Email label
        self.email_label = createEntryLabel(self.entry_frame, 'Email:')
        self.email_label.grid(row=1, column=0, sticky='e', padx=15, pady=10)

        # Email entry box
        self.email_entry = createEntryBox(self.entry_frame)
        self.email_entry.grid(row=1, column=1, padx=(0, 120))

        # Password label
        self.password_label = createEntryLabel(self.entry_frame, 'Password:')
        self.password_label.grid(
            row=2, column=0, sticky='e', padx=15, pady=(10, 5))

        # Password entry box
        self.password_entry = createEntryBox(self.entry_frame)
        self.password_entry.grid(row=2, column=1, padx=(0, 120))
        self.password_entry.configure(show="*")

        # password rule text
        self.password_rule = ctk.CTkTextbox(
            self.entry_frame, activate_scrollbars=False)
        self.password_rule.grid(row=3, column=1, sticky='w')
        self.password_rule.insert(
            '0.0', "Password must have at least 8 characters, a number, a capital letter, and a special character")
        self.password_rule.configure(state='disabled', font=(
            "Encode Sans Expanded SemiBold", 13), fg_color=FullertonWhite, wrap='word', width=460, height=50)

        # confirm password label
        self.confirm_label = createEntryLabel(
            self.entry_frame, 'Confirm Password:')
        self.confirm_label.grid(
            row=4, column=0, sticky='e', padx=15, pady=(5, 10))

        # confirm password entry box
        self.confirm_entry = createEntryBox(self.entry_frame)
        self.confirm_entry.grid(row=4, column=1, padx=(0, 120))
        self.confirm_entry.configure(show='*')

        # submit frame
        self.submit_frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.submit_frame.grid(row=2, column=1, padx=(140, 0))
        self.submit_frame.grid_columnconfigure(0, weight=1)
        self.submit_frame.grid_columnconfigure(1, weight=0)

        # cancel button
        self.cancel_button = createButton(self.submit_frame, 'Cancel')
        self.cancel_button.grid(row=0, column=0, pady=20, padx=(0, 30))

        # register button
        self.register_button = createButton(
            self.submit_frame, 'Register')
        self.register_button.grid(row=0, column=1, padx=(0, 100))

        # login label
        self.login_label = createEntryLabel(
            self.submit_frame, text="If you have an account:")
        self.login_label.grid(row=1, column=0, padx=15, pady=10)

        # login button
        self.login_button = createButton(self.submit_frame, 'Login', command=lambda:self.controller.buttonClicked('Login'))
        self.login_button.grid(row=1, column=1, sticky='e', padx=(0, 100))

    def shows_alert(self):
        self.warning_label.configure(text_color=AlertRed)


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = RegisterFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
