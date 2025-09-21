import tkinter as tk


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")

        # create a container frame for the content to center it
        content_container = tk.Frame(self, bg="white")
        content_container.pack(expand=True, padx=20, pady=20)

        welcome_label = tk.Label(
            content_container,
            text="Welcome to Smart Elective Advisor",
            font=("Arial", 20, "bold"),
            bg="white"
        )
        welcome_label.pack(pady=10)

        description_label = tk.Label(
            content_container,
            text="The Smart Elective Advisor assists University students in\n"
                 "choosing the most suitable elective courses based\n"
                 "on their interests, career goals, and academic performance.\n"
                 "Use the menu to get started.",
            font=("Arial", 12),
            justify="center",
            bg="white"
        )
        description_label.pack(pady=10)
