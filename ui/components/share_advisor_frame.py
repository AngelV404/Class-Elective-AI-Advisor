import customtkinter as ctk
from ..themes import *


class share_advisor_frame(ctk.CTkFrame):
    def __init__(self, parent,email,on_share=None,on_cancel=None):
        super().__init__(parent, fg_color=FullertonWhite)
        
        self.on_share=on_share
        self.on_cancel=on_cancel
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        
        self.main_view=ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.main_view.grid(row=0,column=0,sticky='nswe')
        self.main_view.grid_columnconfigure(0, weight=1)
        
        title=ctk.CTkLabel(self.main_view,text='Detail',font=list_font)
        title.grid(row=0,column=0,sticky='nwe',pady=(0,10))

        self.email=email
        
        label=ctk.CTkLabel(self.main_view, text='Course will be shared with advisor', font=list_font)
        email_label=ctk.CTkLabel(self.main_view,text=email,font=list_font)
        label.grid(row=1,column=0,sticky='nswe')
        email_label.grid(row=2,column=0,sticky='nswe')
        
        share_button=createButton(self.main_view,'Share',command=self.handle_share)
        share_button.configure(width=200)
        share_button.grid(row=3,column=0,pady=(40,20))
        
        
        cancel_button=createButton(self.main_view,'Cancel',self.handle_cancel)
        cancel_button.configure(width=200)
        cancel_button.grid(row=4,column=0,pady=20)
        
        self.confirmation_view=self.create_share_confirmation_frame()
        
    def handle_share(self):
        if callable(self.on_share):
            self.on_share()
            self.main_view.grid_remove()
            self.confirmation_view.grid()

            
        
    def handle_cancel(self):
        if callable(self.on_cancel):
            self.on_cancel()
            
    def reset(self):
        self.confirmation_view.grid_remove()
        self.main_view.grid()


            
    def create_share_confirmation_frame(self):
        frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        frame.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(frame, text='Detail', font=list_font)
        title.grid(row=0, column=0, pady=(0, 10))

        label = ctk.CTkLabel(
            frame, text='Your Course Has Been Sent', font=regular_font)
        label.configure(text_color=AlertRed)
        label.grid(row=1, column=0, pady=40)

        frame.grid_remove()
        return frame
        