import customtkinter as ctk
from .themes import *


class WelcomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color=FullertonWhite)

        self.title_box = ctk.CTkTextbox(self, height=130)
        self.title_box.insert("0.0", 'Welcome to Smart Elective Advisor')
        self.title_box.configure(
            state='disabled', font=heading_font, fg_color=FullertonWhite, wrap='word')
        self.title_box.tag_config("center",justify='center')
        self.title_box.tag_add('center', "1.0","end")
        self.title_box.pack(fill='x', padx=50, pady=(120, 0))

        self.message_box = ctk.CTkTextbox(self)
        self.message_box.insert(
            "0.0", 'The Smart Elective Advisor assists University students in choosing the most suitable elective courses based on their interests, career goals, and academic performance. \nUse the menu to get started.')
        self.message_box.configure(
            state='disable', font=regular_font, fg_color=FullertonWhite, wrap='word')
        self.message_box.tag_config("center",justify='center')
        self.message_box.tag_add("center","1.0","end")
        self.message_box.pack(fill='both', expand=True, padx=100, pady=(0, 20))


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = WelcomePage(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
