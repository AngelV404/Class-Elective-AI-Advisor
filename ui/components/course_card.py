import customtkinter as ctk
from ..themes import *


class course_card(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 name,
                 code,
                 unit,
                 prerequisite,
                 on_explanation=None,
                 on_options=None):
        super().__init__(parent, fg_color=FullertonWhite)

        self.on_explanation = on_explanation
        self.on_options = on_options
        self.grid_columnconfigure(0, weight=1)

        card = ctk.CTkFrame(self, fg_color='#E8EEF3')
        card.grid(sticky='nswe', pady=2)
        card.grid_columnconfigure(0, weight=1)

        self.title_frame = ctk.CTkFrame(card, fg_color='#E8EEF3')
        self.title_frame.grid_columnconfigure((0, 1), weight=1)
        code = ctk.CTkLabel(self.title_frame, text=code, font=regular_font)
        name = ctk.CTkLabel(self.title_frame, text=name, font=(
            "Encode Sans Expanded SemiBold", 16))
        code.grid(row=0, column=0, sticky='w')
        name.grid(row=0, column=1, sticky='w', padx=10)
        self.title_frame.grid(row=0, column=0, sticky='w', padx=3)

        unit = ctk.CTkLabel(card, text=f"Units: {unit}",  font=list_font)
        unit.grid(row=1, column=0, sticky='w', padx=3)

        prerequisite = ctk.CTkLabel(
            card, text=f"Prerequisite: {prerequisite}", font=list_font)
        prerequisite.grid(row=2, column=0, sticky='w', padx=3)

        button_frame = ctk.CTkFrame(card, fg_color='#E8EEF3')
        button_frame.grid(row=3, column=0, pady=20)

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
