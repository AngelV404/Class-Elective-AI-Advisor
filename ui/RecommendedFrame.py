import customtkinter as ctk
from .themes import *


class RecommendedFrame(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent, fg_color=FullertonWhite)
        self.controller=controller
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=7)
        self.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self, text='Courses Recommended', font=heading_font)
        self.title.grid(row=0, column=0, sticky='we', pady=(25, 10))

        self.main_frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.main_frame.grid(row=1, column=0, sticky='nswe')
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # recommended courses
        self.course_frame = ctk.CTkFrame(
            self.main_frame, fg_color=FullertonWhite)
        self.course_frame.grid(row=0, column=0, sticky='nswe')
        self.course_frame.grid_rowconfigure(0, weight=0)
        self.course_frame.grid_rowconfigure(1, weight=10)
        self.course_frame.grid_columnconfigure(0, weight=1)

        self.course_frame_title = ctk.CTkLabel(
            self.course_frame, text='Recommended Courses', font=regular_font)
        self.course_frame_title.grid(
            row=0, column=0, pady=(10, 0), sticky='we')

        self.card_frame = ctk.CTkScrollableFrame(
            self.course_frame, fg_color=FullertonWhite)
        self.card_frame.grid(row=1, column=0, sticky='nswe')
        self.card_frame.grid_columnconfigure(0, weight=1)

        # TODO:delete
        courseCard1 = self.course_card(
            'Cloud Computing and Security (CPSC 454)', '3', '100', 'CPSC 351, CPSC 253f')
        courseCard1.grid(row=0)

        courseCard1 = self.course_card(
            'Cloud Computing and Security (CPSC 454)', '3', '100', 'CPSC 351, CPSC 253f')
        courseCard1.grid(row=1)

        courseCard1 = self.course_card(
            'Cloud Computing and Security (CPSC 454)', '3', '100', 'CPSC 351, CPSC 253f')
        courseCard1.grid(row=2)

        # detail/explanation
        self.detail_frame = ctk.CTkFrame(
            self.main_frame, fg_color=FullertonWhite)
        self.detail_frame.grid(row=0, column=1, sticky='nswe')
        self.detail_frame.grid_rowconfigure(0, weight=0)
        self.detail_frame.grid_rowconfigure(1, weight=10)
        self.detail_frame.grid_columnconfigure(0, weight=1)

        self.course_frame_title = ctk.CTkLabel(
            self.detail_frame, text='Explanation / Options', font=regular_font)
        self.course_frame_title.grid(row=0, column=0, pady=10, sticky='we')

        self.textbox = ctk.CTkTextbox(
            self.detail_frame, wrap="word", font=("Encode Sans Expanded SemiBold", 13), fg_color=FullertonWhite)
        self.textbox.grid(row=1, column=0, sticky="nsew")

        #text

        self.textbox.configure(state="disabled")
        
        # option menu
        self.option_frame=ctk.CTkFrame(self.detail_frame,fg_color=FullertonWhite)
        self.option_frame.grid(row=1,column=0,sticky='nswe')
        self.option_frame.grid_remove()

        self.save_button=createButton(self.option_frame,'Save Course')
        self.save_button.grid(row=0,column=0,sticky='s',pady=10)
        self.save_button.configure(width=200)
        
        self.share_button=createButton(self.option_frame,'Share With Advisor')
        self.share_button.grid(row=1,column=0,sticky='n',pady=10)
        self.share_button.configure(width=200)
        
        
        self.option_frame.grid_rowconfigure(0,weight=1)
        self.option_frame.grid_rowconfigure(3,weight=3)
        self.option_frame.grid_columnconfigure(0,weight=15)
        self.option_frame.grid_columnconfigure(2,weight=1)
        
    def option_clicked(self):
        self.textbox.grid_remove()
        self.option_frame.grid()
    
    def explanation_clicked(self):
        self.option_frame.grid_remove()
        self.textbox.grid()

    def course_card(self, title, unit, rating, prerequisite):
        card = ctk.CTkFrame(self.card_frame, fg_color='#E8EEF3')
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
        

        explanation = createButton(button_frame, 'Explanation',lambda:self.explanation_clicked())
        explanation.grid(row=0, column=0, sticky='we', padx=20)

        options = createButton(button_frame, 'Options',self.option_clicked)
        options.grid(row=0, column=1, sticky='we', padx=20)

        return card


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = RecommendedFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
