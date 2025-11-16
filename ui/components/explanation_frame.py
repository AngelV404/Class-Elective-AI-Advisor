import customtkinter as ctk
from ..themes import *


class explanation_frame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color=FullertonWhite)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        
        explanation_title = ctk.CTkLabel(
            self, text='Explanation', font=list_font)
        explanation_title.grid(row=0, column=0, sticky='nswe')

        self.textbox = ctk.CTkTextbox(
            self, wrap="word", font=("Encode Sans Expanded SemiBold", 13), fg_color=FullertonWhite)
        self.textbox.grid(row=1, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")     
        
        
    def set_text(self,text):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")      
        self.textbox.insert("1.0", text)       
        self.textbox.configure(state="disabled")