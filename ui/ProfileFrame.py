import tkinter as tk
from functools import partial
from db import queries

class ProfileFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        tk.Label(self, text="User Profile").pack(pady=20)

        tk.Button(self, text="View Saved Courses", command=self.display_saved).pack()

    def display_saved(self):
        results = queries.get_saved(self.controller.user)
        self.controller.currentPage.pack_forget()
        self.controller.pages["Saved"].update_results(results)
        self.controller.buttonClicked("Saved")

class SavedFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller

        # Header
        top = tk.Frame(self, bg="white", bd = 2)
        top.pack(fill="both", expand=False, side="top")

        tk.Button(top, text="Back", command=lambda: controller.buttonClicked("Profile")).pack(pady=10,padx = 10, side="left")
        
        tk.Label(top, text="Saved Courses:", font=("Arial", 16), bg="white", bd=2).pack(pady=10,padx = 20, side="left")
        
        tk.Label(top, text="Courses Added Through Wishlist\nOR Required By Degree", font=("Arial", 10), bg="white", bd=2).pack(pady=10,padx = 10, side="left")

        # Allocate space for results
        bottom = tk.Frame(self, bg="White", bd = 2, padx=10, pady=5)
        bottom.pack(fill="both", expand=True, side="bottom")

        left = tk.Canvas(bottom, bg="White")
        left.pack(fill="both", expand=False, side="left")
        
        self.scrollbar = tk.Scrollbar(left, orient="vertical", command=left.yview)
        self.results_container = tk.Frame(left, bg="white")

        self.results_container.bind(
            "<Configure>",
            lambda e: left.configure(scrollregion=left.bbox("all")),
        )
        left.create_window((0, 0), window=self.results_container, anchor="nw")
        left.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y", expand=False)

        self.right = tk.Frame(bottom, bg="white", bd = 2)
        self.right.pack(fill="y", expand=False, side="left")
        
    
    def update_results(self, results):
        # Grab and destroy all previous results
        for widget in self.results_container.winfo_children():
            widget.destroy()

        # If no results
        if not results:
            tk.Label(self.results_container, text = "Something went wrong :(").pack(fill="x", expand=True)
            return

        for row in results:
            box = tk.Frame(self.results_container, bg="#f0f0f0", bd=2, relief="groove")
            box.grid_columnconfigure(1, weight=1)
            box.pack(fill="x", expand=False, pady=3)
            
            # Hover highlight effect
            box.bind("<Enter>", lambda e, b=box: b.config(bd=4))
            box.bind("<Leave>", lambda e, b=box: b.config(bd=2))

            # Add section details to box
            tk.Label(box, text=row[0], bg="#f0f0f0", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w", padx=4, pady=4)
            tk.Label(box, text=row[1], bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=1, sticky="w", padx=4, pady=4)
            tk.Button(box, text="Details", command=partial(self.show_details, row[3])).grid(row=0, column=2, sticky="e", padx=4, pady=4)

            tk.Label(box, text= f"Added Through: {row[2]}", bg="#f0f0f0", font=("Arial", 9)).grid(row=1, column=0, columnspan=2, padx=2, pady=4, sticky="w")

    def show_details(self, course):
        # destroy previous widgets
        for widget in self.right.winfo_children():
            widget.destroy()
        
        details = queries.get_course_details(course)[0]
        # Course code
        tk.Label(self.right, text = details[1],font=("Arial",12)).pack(fill="x", side="top")
        # Course Name
        tk.Label(self.right, text = details[2],font=("Arial",12)).pack(fill="x", side="top")
        # Course Details
        text_widget = tk.Text(self.right, wrap="word", relief="flat", height=10)
        text_widget.insert("end", details[3])
        text_widget.config(state="disabled")
        text_widget.pack(fill="both")
        # Course credits
        tk.Label(self.right, text = f"Credits: {details[4]}",font=("Arial",10), bg="white").pack(fill="x", side="top", pady=5)


        # Course prerequiste section
        tk.Label(self.right, text = "Course Prerequisites:", font=("Arial", 12)).pack(fill="x", side="top")
        prereqs = queries.get_prereq_status(course, self.controller.user)
        self.prereq = tk.Text(self.right, height=len(prereqs), wrap = tk.WORD, bg= "White", width=30)
        self.prereq.pack(pady=5, side="top", anchor="n")

        # Color prerequisite green if taken else red
        if prereqs:
            for i in range(len(prereqs)):
                if prereqs[i][2] == 1:
                    self.prereq.insert("end", prereqs[i][0] + ' ' + prereqs[i][1], "green")
                elif prereqs[i][2] == 2:
                    self.prereq.insert("end", prereqs[i][0] + ' ' + prereqs[i][1], "yellow")
                else:
                    self.prereq.insert("end", prereqs[i][0] + ' ' + prereqs[i][1], "red")
                if i != len(prereqs) - 1:
                    self.prereq.insert("end", "\n")
            self.prereq.tag_configure("green", foreground="green")
            self.prereq.tag_configure("yellow", foreground="#c2ab17")
            self.prereq.tag_configure("red", foreground="red")
        else:
            self.prereq.insert("end", "None")
        self.prereq.config(state="disabled") 