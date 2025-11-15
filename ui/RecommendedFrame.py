import customtkinter as ctk
from .themes import *
from .components.course_list_frame import course_list_frame
from .components.explanation_frame import explanation_frame
from .components.share_advisor_frame import share_advisor_frame
from controller.RecommendedController import RecommendedController


class RecommendedFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=FullertonWhite)

        self.controller = RecommendedController(self)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=7)
        self.grid_columnconfigure(0, weight=1)

        # title
        self.title = ctk.CTkLabel(
            self, text='Courses Recommended', font=heading_font)
        self.title.grid(row=0, column=0, sticky='we', pady=(25, 10))

        # main frame (split layout)
        self.main_frame = ctk.CTkFrame(self, fg_color=FullertonWhite)
        self.main_frame.grid(row=1, column=0, sticky='nswe')
        self.main_frame.grid_columnconfigure(0, weight=1, uniform="equal")
        self.main_frame.grid_columnconfigure(1, weight=1, uniform="equal")
        self.main_frame.grid_rowconfigure(0, weight=1)

        # left: recommended course list
        self.course_list = course_list_frame(
            self.main_frame, title='Recommended Courses')
        self.course_list.grid(row=0, column=0, sticky='nswe')

        # right: course detail area
        self.detail_frame = ctk.CTkFrame(
            self.main_frame, fg_color=FullertonWhite)
        self.detail_frame.grid(row=0, column=1, sticky='nswe')
        self.detail_frame.grid_rowconfigure(0, weight=0)
        self.detail_frame.grid_rowconfigure(1, weight=8)
        self.detail_frame.grid_columnconfigure(0, weight=1)

        self.course_frame_title = ctk.CTkLabel(
            self.detail_frame, text='Explanation / Options', font=regular_font)
        self.course_frame_title.grid(row=0, column=0, pady=10, sticky='we')

        # subframes (right side)
        self.subframes = {
            "explanation": explanation_frame(self.detail_frame),
            "options": self.create_options_frame(),
            "saved": self.create_saved_frame(),
            "share": share_advisor_frame(
                self.detail_frame,
                email='eksud@csu.fullerton.edu',
                on_share=self.controller.share_with_advisor,
                on_cancel=self.controller.show_current_explanation),
        }

        self.current_subframe = None

    def show_subframe(self, name=None):
        if name == None and self.current_subframe == None:
            return

        if name == None and self.current_subframe:
            self.subframes[self.current_subframe].grid_remove()
            self.current_subframe = None
            return

        if self.current_subframe:
            self.subframes[self.current_subframe].grid_remove()
        self.subframes[name].grid(row=1, column=0, sticky='nsew')
        self.current_subframe = name

    # ---------------------- modular detail frames ----------------------

    def create_options_frame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)

        frame.grid_columnconfigure((0, 2), weight=1)
        frame.grid_columnconfigure(1, weight=3)

        save_button = createButton(
            frame, 'Save Course', command=self.controller.save_course)
        save_button.configure(width=200)
        save_button.grid(row=0, column=1, pady=(60, 10))

        share_button = createButton(
            frame, 'Share With Advisor', command=lambda: self.show_subframe('share'))
        share_button.configure(width=200)
        share_button.grid(row=1, column=1, pady=10)

        frame.grid_remove()
        return frame

    def create_saved_frame(self):
        frame = ctk.CTkFrame(self.detail_frame, fg_color=FullertonWhite)
        frame.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(frame, text='Detail', font=list_font)
        title.grid(row=0, column=0, pady=(0, 10))

        confirm_msg = ctk.CTkLabel(
            frame, text='Course Has Been Saved', font=list_font)
        confirm_msg.grid(row=1, column=0, pady=10)

        # TODO:link to saved courses
        view_btn = createButton(frame, 'View Saved Courses')
        view_btn.configure(width=200)
        view_btn.grid(row=2, column=0, pady=10)

        share_btn = createButton(frame, 'Share with Advisor',
                                 command=lambda: self.show_subframe('share'))
        share_btn.configure(width=200)
        share_btn.grid(row=3, column=0, pady=10)

        frame.grid_remove()
        return frame
