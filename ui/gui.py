import tkinter as tk
from db import dbsetup, queries
from .CourseFrame import *
from .HomeFrame import HomeFrame
# from HelpFrame import HelpFrame
# from PreferencesFrame import PreferencesFrame
from .ProfileFrame import *
# from RecommendedFrame import RecommendedFrame


class App(tk.Tk):
    def __init__(self, email):
        super().__init__()
        self.user = queries.get_user(email)

        self.title("Class Advisor")
        self.geometry("800x600")
        
        self.main_frame=tk.Frame(self, bg="navy")
        self.main_frame.pack(expand=False, fill="both")

        # sidebar
        self.sidebar = tk.Frame(self.main_frame, width=200, height=600, bg="white")
        self.sidebar.pack_propagate(False)  # fixed size
        self.sidebar.pack(side="left", fill="y", padx=1,pady=1)

        # create buttons
        tk.Button(self.sidebar, text="Home", relief="solid", highlightbackground="navy", highlightthickness=1, bg="white", activebackground="orange",
                  command=lambda: self.show_frame("Home")).pack(fill="both", expand=True,  pady=(0, 20), padx=(0, 20))
        tk.Button(self.sidebar, text="Courses", relief="solid", bd=1, highlightbackground="navy", highlightthickness=2, bg="white", activebackground="orange",
                  command=lambda: self.show_frame("CourseSearch")).pack(fill="both", expand=True, pady=(0, 20), padx=(0, 20))
        tk.Button(self.sidebar, text="Preferences", relief="solid", bd=1, highlightbackground="navy", highlightthickness=2, bg="white", activebackground="orange",
                  command=lambda: self.show_frame("Preferences")).pack(fill="both", expand=True, pady=(0, 20), padx=(0, 20))
        tk.Button(self.sidebar, text="Recommended", relief="solid", bd=1, highlightbackground="navy", highlightthickness=2, bg="white", activebackground="orange",
                  command=lambda: self.show_frame("Recommended")).pack(fill="both", expand=True, pady=(0, 20), padx=(0, 20))
        tk.Button(self.sidebar, text="Profile", relief="solid", bd=1, highlightbackground="navy", highlightthickness=2, bg="white", activebackground="orange",
                  command=lambda: self.show_frame("Profile")).pack(fill="both", expand=True, pady=(0, 20), padx=(0, 20))
        tk.Button(self.sidebar, text="Help", relief="solid", bd=1, highlightbackground="navy", highlightthickness=2, bg="white", activebackground="orange",
                  command=lambda: self.show_frame("Help")).pack(fill="both", expand=True, pady=(0, 20), padx=(0, 20))

        # main area
        self.content = tk.Frame(self.main_frame, bg="Black")
        self.content.pack(expand=True, fill="both",padx=2,pady=2)

        # Setup db
        dbsetup.connectdb()

        # Load frames
        self.frames = {
            "CourseSearch": CourseSearchFrame(self.content, self),
            "Home": HomeFrame(self.content, self),
            "Courses": CourseFrame(self.content, self),
            "Sections": SectionFrame(self.content, self),
            # "Help": HelpFrame(self.content, self),
            "Profile": ProfileFrame(self.content, self),
            "Saved": SavedFrame(self.content, self)
            # "Recommended": RecommendedFrame(self.content, self),
            # "Preferences": PreferencesFrame(self.content, self)
        }
        self.content.grid_rowconfigure(0, weight=1)   # row 0 expands vertically
        self.content.grid_columnconfigure(0, weight=1)  # column 0 expands horizontally

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


app = App('a@csu.fullerton.edu')
app.mainloop()