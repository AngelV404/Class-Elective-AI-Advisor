import customtkinter as ctk
from .themes import *


class HelpFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=FullertonWhite)
        self.label = ctk.CTkLabel(
            self, text="Help & Support", font=heading_font)
        self.label.pack(pady=20)

        self.entry = createEntryBox(self)
        self.entry.configure(
            placeholder_text="Enter a topic (e.g., 'How to get recommendations?')", width=400)
        self.entry.pack(pady=10)

        self.search_button = createButton(
            self, "Search", self.show_help_result)
        self.search_button.pack(pady=10)

        self.result_box = ctk.CTkTextbox(self, width=600, height=200)
        self.result_box.pack(pady=10)
        self.result_box.configure(width=700,
                                  height=350,
                                  corner_radius=10,
                                  border_width=2,
                                  border_color="#00274C",
                                  font=list_font,
                                  wrap="word")

    def show_help_result(self):
        query = self.entry.get().lower()
        response = "Feature coming soon! Please contact your advisor if you need help."

        if "recommend" in query:
            response = "To get recommendations, go to the Preferences page, fill in your details, and click Submit."
        elif "save" in query:
            response = "You can save a course from the Recommended page by pressing 'Save'."
        elif "advisor" in query:
            response = "You can share saved courses with your advisor via the 'Share with Advisor' button."

        self.result_box.delete("1.0", "end")
        self.result_box.insert("end", response)
