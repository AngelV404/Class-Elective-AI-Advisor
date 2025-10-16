import customtkinter as ctk
from LoginFrame import LoginFrame
from themes import *
from WelcomePage import WelcomePage
from registerFrame import RegisterFrame
# from HelpFrame import HelpFrame
# from PreferencesFrame import PreferencesFrame
# from ProfileFrame import ProfileFrame
# from RecommendedFrame import RecommendedFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Smart Elective Advisor')
        self.geometry('1100x700')
        ctk.set_appearance_mode('light')

        ctk.set_default_color_theme('blue')

        # set up the grid for root window
        self.grid_columnconfigure(0, weight=0)  # sidebar fixed width
        # main area takes the remaining space
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  # stretch entire height
        self.configure(fg_color=FullertonWhite)

        # create sidebar frame
        self.sidebarFrame = ctk.CTkFrame(self,
                                         width=250,
                                         corner_radius=0,
                                         border_color=FullertonBlue,
                                         border_width=3)

        self.sidebarFrame.grid(row=0, column=0, sticky='nsew')
        self.sidebarFrame.configure(fg_color=FullertonWhite)
        self.sidebarFrame.grid_propagate(False)

        # create main area frame
        self.mainArea = ctk.CTkFrame(self,
                                     corner_radius=0,
                                     border_color=FullertonBlue,
                                     border_width=3)
        self.mainArea.grid(row=0, column=1, sticky='nsew')
        self.mainArea.configure(fg_color=FullertonWhite)


        # create sidebar buttons
        self.selectedButton = 'Home'
        self.buttons = {}  # store a references to buttons
        self.sidebarButton("Home").grid(row=0, column=0, pady=(0, 20))
        self.buttons[self.selectedButton].configure(
            fg_color=FullertonOrange, hover_color=FullertonOrange)

        self.sidebarButton('Login').grid(row=1, column=0, pady=(0, 20))
        self.sidebarButton('Preferences').grid(row=2, column=0, pady=(0, 20))
        self.sidebarButton('Recommended').grid(row=3, column=0, pady=(0, 20))
        self.sidebarButton('Profile').grid(row=4, column=0, pady=(0, 20))
        self.sidebarButton('Help').grid(row=5, column=0)

        #pages
        self.pages = {
            "Home": WelcomePage(self.mainArea),
            "Login": LoginFrame(self.mainArea, self),
            "Register":RegisterFrame(self.mainArea, self)
            # "Preferences": PreferencesFrame(self.mainArea),
            # "Recommended": RecommendedFrame(self.mainArea),
            # "Profile": ProfileFrame(self.mainArea),
            # "Help": HelpFrame(self.mainArea)
        }

        # show welcome page
        self.currentPage = self.pages['Home']
        self.currentPage.pack(fill='both', expand=True, padx=3, pady=3)

    def sidebarButton(self, name):
        new_button = ctk.CTkButton(
            self.sidebarFrame,
            text=name,
            height=100,
            border_color=FullertonBlue,
            width=230,
            border_width=3,
            font=regular_font,
            text_color=FullertonBlue,
            hover_color=FullertonLightOrange,
            fg_color=FullertonWhite,
            corner_radius=0,
            command=lambda: self.buttonClicked(name)
        )
        self.buttons[name] = new_button

        return new_button

    def buttonClicked(self, name):
        if name in self.buttons and self.selectedButton != name:
            self.buttons[name].configure(
                fg_color=FullertonOrange, hover_color=FullertonOrange)
            self.buttons[self.selectedButton].configure(
                fg_color=FullertonWhite, hover_color=FullertonLightOrange)
            self.selectedButton = name

        # hide current page
        if self.currentPage is not None:
            self.currentPage.pack_forget()

        # show selected page
        self.currentPage = self.pages[name]
        self.currentPage.pack(fill="both", expand=True, padx=3, pady=3)


if __name__ == "__main__":
    app = App()
    app.mainloop()
