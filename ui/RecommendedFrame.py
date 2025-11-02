import customtkinter as ctk
from themes import *


class RecommendedFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=FullertonWhite)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=7)
        self.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self, text='Courses Recommended', font=heading_font)
        self.title.grid(row=0, column=0, sticky='we', pady=(25, 10))

        self.main_frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.main_frame.grid(row=1, column=0, sticky='nswe')
        self.main_frame.grid_columnconfigure(0, weight=1, uniform="equal")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1, uniform="equal")

        self.RecommendedCoursesFrame()
        self.CourseDetailFrame()

        self.subframes = {
            "explanation": self.ExplanationFrame(),
            "options": self.OptionsFrame(),
            "saved": self.SavedFrame(),
            "share": self.ShareFrame(),
            "share_confirmation": self.SharedConfirmationFrame()
        }

        self.current_subframe = None

    def show_subframe(self, name):
        if self.current_subframe is not None:
            self.subframes[self.current_subframe].grid_remove()

        self.subframes[name].grid()
        self.current_subframe = name

#helper
    def create_course_card(self, title, unit, rating, prerequisite):
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

        explanation = createButton(
            button_frame, 'Explanation', lambda: self.show_subframe("explanation"))
        explanation.grid(row=0, column=0, sticky='we', padx=20)

        options = createButton(button_frame, 'Options',
                               lambda: self.show_subframe("options"))
        options.grid(row=0, column=1, sticky='we', padx=20)

        return card

    def RecommendedCoursesFrame(self):
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

        courseCard1 = self.create_course_card(
            'Cloud Computing and Security (CPSC 454)', '3', '100', 'CPSC 351, CPSC 253f')
        courseCard1.grid(row=0)

        courseCard1 = self.create_course_card(
            'Cloud Computing and Security (CPSC 454)', '3', '100', 'CPSC 351, CPSC 253f')
        courseCard1.grid(row=1)

        courseCard1 = self.create_course_card(
            'Cloud Computing and Security (CPSC 454)', '3', '100', 'CPSC 351, CPSC 253f')
        courseCard1.grid(row=2)

    def CourseDetailFrame(self):
        self.detail_frame = ctk.CTkFrame(
            self.main_frame, fg_color=FullertonWhite)
        self.detail_frame.grid(row=0, column=1, sticky='nswe')
        self.detail_frame.grid_rowconfigure(0, weight=0)
        self.detail_frame.grid_rowconfigure(1, weight=10)
        self.detail_frame.grid_columnconfigure(0, weight=1)

        self.course_frame_title = ctk.CTkLabel(
            self.detail_frame, text='Explanation / Options', font=regular_font)
        self.course_frame_title.grid(row=0, column=0, pady=10, sticky='we')

    def OptionsFrame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)
        frame.grid(row=1, column=0, sticky='nswe')
        frame.grid_remove()

        save_button = createButton(
            frame, 'Save Course', command=lambda: self.show_subframe("saved"))
        save_button.grid(row=0, column=0, sticky='s', pady=10)
        save_button.configure(width=200)

        share_button = createButton(
            frame, 'Share With Advisor', command=lambda: self.show_subframe("share"))
        share_button.grid(row=1, column=0, sticky='n', pady=10)
        share_button.configure(width=200)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(3, weight=3)
        frame.grid_columnconfigure(0, weight=15)
        frame.grid_columnconfigure(2, weight=1)

        return frame

    def SavedFrame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)
        frame.grid(row=1, column=0, sticky='nswe')
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_remove()

        
        title=ctk.CTkLabel(frame,text='Detail',font=list_font)
        title.grid(row=0,column=0,sticky='nwe',pady=(0,10))

        confirm_msg=ctk.CTkLabel(frame,text='Course Has Been Saved', font=list_font)
        confirm_msg.grid(row=1,column=0,sticky='nswe',pady=10)

        view_courses_button=createButton(frame,'View Saved Courses')
        view_courses_button.configure(width=200)
        view_courses_button.grid(row=2,column=0,sticky='ns',pady=10)

        share_button=createButton(frame,'Share with Advisor',lambda:self.show_subframe('share'))
        share_button.configure(width=200)
        share_button.grid(row=3,column=0,sticky='ns',pady=10)        
        
        return frame

    def ShareFrame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)
        frame.grid(row=1, column=0, sticky='nswe')
        frame.grid_remove()
        frame.grid_columnconfigure(0,weight=1)
        
        title=ctk.CTkLabel(frame,text='Detail',font=list_font)
        title.grid(row=0,column=0,sticky='nwe',pady=(0,10))

        email='eksud@csu.fullerton.edu'
        
        label=ctk.CTkLabel(frame, text='Course will be shared with advisor', font=list_font)
        email_label=ctk.CTkLabel(frame,text=email,font=list_font)
        label.grid(row=1,column=0,sticky='nswe')
        email_label.grid(row=2,column=0,sticky='nswe')
        
        share_button=createButton(frame,'Share',command=lambda:self.show_subframe('share_confirmation'))
        share_button.configure(width=200)
        share_button.grid(row=3,column=0,pady=(40,20))
        
        
        cancel_button=createButton(frame,'Cancel',lambda:self.show_subframe('explanation'))
        cancel_button.configure(width=200)
        cancel_button.grid(row=4,column=0,pady=20)
        
        return frame

    def SharedConfirmationFrame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)
        frame.grid(row=1, column=0, sticky='nswe')
        frame.grid_remove()
        frame.grid_columnconfigure(0,weight=1)
        
        title=ctk.CTkLabel(frame,text='Detail',font=list_font)
        title.grid(row=0,column=0,sticky='nwe',pady=(0,10))

        email='eksud@csu.fullerton.edu'
        
        label=ctk.CTkLabel(frame, text='Course will be shared with advisor', font=list_font)
        email_label=ctk.CTkLabel(frame,text=email,font=list_font)
        label.grid(row=1,column=0,sticky='nswe')
        email_label.grid(row=2,column=0,sticky='nswe')
        
        confirm=ctk.CTkLabel(frame,text='Your Course Has Been Sent',font=regular_font)
        confirm.configure(text_color=AlertRed)
        confirm.grid(row=3,column=0,pady=40)
        
        return frame

    def ExplanationFrame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)
        frame.grid(row=1, column=0, sticky="new")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=8)

        explanation_title = ctk.CTkLabel(
            frame, text='Explanation', font=list_font)
        explanation_title.grid(row=0, column=0, sticky='nswe')

        textbox = ctk.CTkTextbox(
            frame, wrap="word", font=("Encode Sans Expanded SemiBold", 13), fg_color=FullertonWhite)
        textbox.grid(row=1, column=0, sticky="nsew")
        textbox.configure(state="disabled")

        frame.grid_remove()
        return frame


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = RecommendedFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
