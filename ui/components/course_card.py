import customtkinter as ctk
from ..themes import *


class course_card(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 title,
                 unit,
                 rating,
                 prerequisite,
                 on_explanation=None,
                 on_options=None):
        super().__init__(parent, fg_color=FullertonWhite)
        
        self.on_explanation=on_explanation
        self.on_options=on_options
        self.grid_columnconfigure(0,weight=1)

        card = ctk.CTkFrame(self, fg_color='#E8EEF3')
        card.grid(sticky='nswe', pady=2)
        card.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(card, text=title, font=list_font)
        title.grid(row=0, column=0, sticky='w', padx=3)

        unit = ctk.CTkLabel(card, text=f"Units: {unit}",  font=list_font)
        unit.grid(row=1, column=0, sticky='w', padx=3)

        rating = ctk.CTkLabel(
            card, text=f"Rating: {rating}/100", font=list_font)
        rating.grid(row=2, column=0, sticky='w', padx=3)

        prerequisite = ctk.CTkLabel(
            card, text=f"Prerequisite: {prerequisite}", font=list_font)
        prerequisite.grid(row=3, column=0, sticky='w', padx=3)

        button_frame = ctk.CTkFrame(card, fg_color='#E8EEF3')
        button_frame.grid(row=4, column=0, pady=20)

        explanation = createButton(
            button_frame, 'Explanation', self.handle_explanation)
        explanation.grid(row=0, column=0, sticky='we', padx=20)

        options = createButton(button_frame, 'Options',
                              self.handle_options)
        options.grid(row=0, column=1, sticky='we', padx=20)
        
    def handle_explanation(self):
        if (callable(self.on_explanation)):
            self.on_explanation()
            
    def handle_options(self):
        if (callable(self.on_options)):
            self.on_options()
        

