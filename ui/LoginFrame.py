import customtkinter as ctk
from ui.themes import *


class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=FullertonWhite)
        self.controller=controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(3, weight=5)

        self.title = ctk.CTkLabel(self, text='Login', font=heading_font)
        self.title.grid(row=0, column=1, sticky='nesw', pady=(35, 35))

        # user input field
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.grid(row=1, column=1)
        self.entry_frame.configure(fg_color=FullertonWhite)
        self.entry_frame.columnconfigure(1, weight=1)

        # email label
        self.email_label = createEntryLabel(self.entry_frame, "Email:")
        self.email_label.grid(row=0, column=0, sticky="e", padx=15, pady=10)

        # email entry box
        self.email_entry = createEntryBox(self.entry_frame)
        self.email_entry.grid(row=0, column=1, sticky="w")

        # password label
        self.password_label = createEntryLabel(
            self.entry_frame, text='Password:')
        self.password_label.grid(
            row=1, column=0, sticky='e', padx=15, pady=10)

        # password entry box
        self.password_entry = createEntryBox(self.entry_frame)
        self.password_entry.grid(row=1, column=1, sticky='w')
        self.password_entry.configure(show='*')

        # submit frame
        self.submit_frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.submit_frame.grid(row=2, column=1)
        self.submit_frame.grid_columnconfigure(0, weight=1)
        self.submit_frame.grid_columnconfigure(1, weight=0)

        # login button
        login_button = createButton(self.submit_frame, 'Login', command=lambda: self.controller.do_login(self))
        login_button.grid(row=0, column=1, pady=20, sticky='e')

        # register label
        self.register_label = createEntryLabel(
            self.submit_frame, text="If you don't have an account:")
        self.register_label.grid(row=1, column=0, padx=15, pady=10)

        # register button
        self.register_button = createButton(self.submit_frame, 'Register',command=lambda: self.controller.buttonClicked("Register") )
        self.register_button.grid(row=1, column=1, sticky='e')


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = LoginFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
