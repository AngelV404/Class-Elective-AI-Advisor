import customtkinter as ctk
from .themes import *

class LoginFrame(ctk.Frame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=FullertonWhite)
        
        
        
        
        
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = LoginFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
