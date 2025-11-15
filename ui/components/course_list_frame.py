import customtkinter as ctk
from ..themes import *
from .course_card import course_card


class course_list_frame(ctk.CTkFrame):
    def __init__(self, parent, title):
        super().__init__(parent, fg_color=FullertonWhite)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # title
        self.course_frame_title = ctk.CTkLabel(
            self, text=title, font=regular_font)
        self.course_frame_title.grid(
            row=0, column=0, pady=(10, 0), sticky='we')

        # Scrollable container for cards
        self.card_frame = ctk.CTkScrollableFrame(
            self, fg_color=FullertonWhite)
        self.card_frame.grid(row=1, column=0, sticky='nswe')
        self.card_frame.grid_columnconfigure(0, weight=1)
        
        self.row_num=0

    # remove all cards
    def clear(self):
        for widget in self.card_frame.winfo_children():
            widget.destroy()
        self.row_num=0

    def add_course_card(self, title, unit, rating, prerequisite,
                        on_explanation=None, on_options=None):
        new_card = course_card(self.card_frame, title, unit,
                               rating, prerequisite, on_explanation, on_options)
        
        new_card.grid(row=self.row_num, column=0, sticky='we')
        self.row_num+=1