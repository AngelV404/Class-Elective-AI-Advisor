import customtkinter as ctk


# Colors
FullertonBlue = "#00274C"
FullertonOrange = "#FF7900"
FullertonWhite = "#FFFFFF"
FullertonBlack = "#000000"
AlertRed = "#FF0000"
FullertonLightOrange = '#FFDAB9'

# Fonts
heading_font = ("Encode Sans Expanded SemiBold", 36, "bold")
regular_font = ("Encode Sans Expanded SemiBold", 20, "bold")
list_font = ("Encode Sans Expanded SemiBold", 15, "bold")


def createEntryLabel(parent, text):
    new_label = ctk.CTkLabel(
        parent,
        text=text,
        font=regular_font,
        fg_color=FullertonWhite
    )

    return new_label


def createEntryBox(parent):
    new_entry = ctk.CTkEntry(
        parent,
        corner_radius=0,
        border_color='grey',
        width=350,
        height=35,
        fg_color=FullertonLightOrange,
        text_color='black',
        font=list_font,
        border_width=2
    )
    return new_entry


def createButton(parent, text, command=None):
    new_button = ctk.CTkButton(parent,
                               text=text,
                               command=command,
                               font=("Encode Sans Expanded SemiBold", 20),
                               fg_color=FullertonBlue,
                               text_color=FullertonLightOrange,
                               corner_radius=8,
                               width=140,
                               height=40)
    return new_button


def createOptionMenu(parent, option, command=None):
    dropdown = ctk.CTkOptionMenu(
        parent,
        values=option,
        command=command,  
        width=350,
        height=35,
        fg_color=FullertonLightOrange,
        button_color=FullertonOrange,
        text_color="black",
        corner_radius=2,
        font=regular_font,
        dropdown_fg_color=FullertonOrange,
        dropdown_font=list_font,
        dynamic_resizing=False
    )
    
    return dropdown
