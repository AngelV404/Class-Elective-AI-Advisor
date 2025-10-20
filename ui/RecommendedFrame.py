import customtkinter as ctk
from themes import *


class RecommendFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=FullertonWhite)
        self.title=ctk.CTkLabel(self, text='Courses Recommended',font=heading_font)
        self.title.grid(row=0,column=0,sticky='nsew',pady=(35,35))

        self.detail_frame=ctk.CTkFrame(self)
        self.detail_frame.grid(row=1,column=0)
        
        self.course_frame=ctk.CTkFrame(self.detail_frame)
        self.course_frame.grid(row=0,column=0)
        
        self.explanation_frame=ctk.CTkFrame(self.detail_frame)
        self.explanation_frame.grid(row=0,column=1)
        
        self.course_title=ctk.CTkLabel(self.course_frame,text='Recommended Courses',font=regular_font)
        self.course_title.grid(row=0,column=0,sticky='s')


    def recommendCourse(self, course_title,unit,rating,prerequisites):
        self.list_frame=ctk.CTkFrame(self.course_frame)
        
        self.title=ctk.CTkLabel(self.list_frame,text=course_title,font=list_font)
        self.title.grid(row=0,column=0,sticky='w')
        
        
        
        
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = RecommendFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
