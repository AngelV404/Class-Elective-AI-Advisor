import tkinter as tk
from functools import partial
from db import queries

class CourseFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        tk.Label(self, text="Course Search").pack(pady=20)
        name_label = tk.Label(self, text="Search by Course Name:")
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        code_label = tk.Label(self, text="Search by Course Code:")
        code_label.pack(pady=5)
        self.code_entry = tk.Entry(self)
        self.code_entry.pack(pady=5)

        tk.Button(self, text="Submit", command=partial(self.displaycourses)).pack()

    def displaycourses(self):
        results = queries.get_courses(self.code_entry, self.name_entry)
        results_frame = self.controller.frames["Results"]
        results_frame.update_results(results)
        self.controller.show_frame("Results")


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller

        tk.Label(self, text="Course Results", font=("Arial", 16)).pack(pady=20)
        self.results_container = tk.Frame(self)
        self.results_container.pack()

        tk.Button(self, text="Back", command=lambda: controller.show_frame("Courses")).pack(pady=10)

    def update_results(self, results):
        for widget in self.results_container.winfo_children():
            widget.destroy()

        if not results:
            tk.Label(self.results_container, text = "No Courses Found").pack()
            return
        

        for row in results:
            tk.Label(self.results_container, text= f'{row[0]} {row[1]}').pack(pady=10)