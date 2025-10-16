import tkinter as tk
from functools import partial
from db import queries

class CourseSearchFrame(tk.Frame):
    
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
        Courses_frame = self.controller.frames["Courses"]
        Courses_frame.update_results(results)
        self.controller.show_frame("Courses")


class CourseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller

        # Allocate space for results
        bottom = tk.Frame(self, bg="white")
        bottom.pack(fill="both", expand=True, side="bottom")

        # Scrollable container for results
        self.canvas = tk.Canvas(bottom, bg="white", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(bottom, orient="vertical", command=self.canvas.yview)
        self.results_container = tk.Frame(self.canvas, bg="White")

        self.results_container.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.results_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx= 5, pady=5)
        self.scrollbar.pack(side="right", fill="y")

        # Back button
        tk.Button(self, text="Back", command=lambda: controller.show_frame("CourseSearch")).pack(pady=10,padx = 10, side="left")
        
        tk.Label(self, text="Course Search").pack(pady=10,padx = 20, side="left")

    def update_results(self, results):
        # Grab and destroy all previous results
        for widget in self.results_container.winfo_children():
            widget.destroy()

        # If no results
        if not results:
            tk.Label(self.results_container, text = "No Courses Found").pack()
            return

        for row in results:
            CourseBox(self.results_container, self.controller, row[0],row[1],row[2], row[3])

    def displaysections(controller, id):
        results = queries.get_sections(id)
        results_frame = controller.frames["Sections"]
        results_frame.update_results(results)
        controller.show_frame("Sections")

class CourseBox(tk.Frame):
    def __init__(self, parent, controller, code, name, description, id):
        super().__init__(parent, bg="#ffffff", bd=1, relief="solid")

        self.expanded = False
        self.id = id

        box = tk.Frame(parent, bg="#f0f0f0", bd=2, relief="groove")
        box.grid_columnconfigure(1, weight=1)
        box.pack(fill="x", expand=False, pady=3)
        
        # Hover highlight effect
        box.bind("<Enter>", lambda e, b=box: b.config(bd = 3))
        box.bind("<Leave>", lambda e, b=box: b.config(bd = 2))

        # Add course code and name inside box
        tk.Label(box, text=code, bg="#f0f0f0", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=4)
        tk.Label(box, text=name, bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=1, sticky="w", padx=10, pady=4)

        self.toggle_btn = tk.Button(box, text="▼ Show", command=self.toggle)
        self.toggle_btn.grid(row=0, column=2, sticky="e")

        # Description
        self.description_label = tk.Label(
            box, text=description, bg="#f0f0f0", wraplength=400, justify="left"
        )
    
        # Button for viewing sections
        tk.Button(box, text="Sections", command=partial(CourseFrame.displaysections, controller, id)).grid(row=0, column=3, sticky="e", padx=2, pady=4)
        # Button for wishlisting
        tk.Button(box, text="Wishlist", command=lambda: "Wishlisting Course").grid(row=1, column=3, sticky="e", padx=2, pady=4)

        # Let title stretch, button stay right
        self.grid_columnconfigure(0, weight=1)

    def toggle(self):
        if self.expanded:
            # Hide the description
            self.description_label.grid_forget()
            self.toggle_btn.config(text="▼ Show")
            self.expanded = False
        else:
            # Show the description
            self.description_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=4, padx= 10)
            self.toggle_btn.config(text="▲ Hide")
            self.expanded = True

class SectionFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller

        # Allocate space for results
        bottom = tk.Frame(self, bg="white")
        bottom.pack(fill="both", expand=True, side="bottom")

        # Scrollable container for results
        self.canvas = tk.Canvas(bottom, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(bottom, orient="vertical", command=self.canvas.yview)
        self.results_container = tk.Frame(self.canvas, bg="White")

        self.results_container.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.results_container, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx= 5, pady=5)
        scrollbar.pack(side="right", fill="y")

        # Back button
        tk.Button(self, text="Back", command=lambda: controller.show_frame("Courses")).pack(pady=10,padx = 10, side="left")
        
    
    def update_results(self, results):
        # Grab and destroy all previous results
        for widget in self.results_container.winfo_children():
            widget.destroy()
            self.title.destroy()
            self.desc.destroy()
            self.prereq.destroy()
            self.prereq_label.destroy()

        # If no results
        if not results:
            tk.Label(self.results_container, text = "No Course Sections Found").pack()
            return
        
        self.title = tk.Label(self, text=results[0][1], font=("Arial",14))
        self.title.pack(pady=5)
        self.desc  = tk.Label(self, text=results[0][5], font=("Arial",10), wraplength=450)
        self.desc.pack(pady=5)


        # Create box for each row
        for row in results:
            code, name = row[0] + "-" + str(row[2]), row[1]
            box = tk.Frame(self.results_container, bg="#f0f0f0", bd=2, relief="groove")
            box.grid_columnconfigure(1, weight=1)
            box.pack(fill="x", expand=False, pady=3)
            
            # Hover highlight effect
            box.bind("<Enter>", lambda e, b=box: b.config(bd=4))
            box.bind("<Leave>", lambda e, b=box: b.config(bd=2))

            # Add section details to box
            tk.Label(box, text=code, bg="#f0f0f0", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w", padx=8, pady=8)
            tk.Label(box, text=name, bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=1, sticky="w", padx=8, pady=8)
            tk.Label(box, text= f"Instructor: {row[6]}", bg="#f0f0f0", font=("Arial", 8)).grid(row=0, column=2, sticky="s", padx=10, pady=8)
            tk.Label(box, text=f"Registered: {row[8]}/{row[7]}", bg="#f0f0f0", font=("Arial", 7)).grid(row=1, column=3, sticky="n", padx=10, pady=0)
            tk.Label(box, text=f"Waitlisted: {row[9]}", bg="#f0f0f0", font=("Arial", 8)).grid(row=2, column=3, sticky="s", padx=10, pady=0)

            # Add class to schedule
            tk.Button(box, text="Add to Schedule", command=lambda: "").grid(row=0, column=3, sticky="w", padx=10, pady=2, columnspan=3)
        
        # Prerequisites label
        self.prereq_label  = tk.Label(self, text="Prerequisites: ", font=("Arial",10), bg = "white")
        self.prereq_label.pack(pady=5, side="left")

        # Query and dislplay prerequisites for course
        prereqs = queries.get_prereq_status(row[10], self.controller.user)
        self.prereq = tk.Text(self, height=len(prereqs), wrap = tk.WORD, bg= "White", width=30)
        self.prereq.pack(pady=5)

        # Color prerequisite green if taken else red
        if prereqs:
            for i in range(len(prereqs)):
                if prereqs[i][2] == 1:
                    self.prereq.insert("end", prereqs[i][0] + ' ' + prereqs[i][1], "green")
                else:
                    self.prereq.insert("end", prereqs[i][0] + ' ' + prereqs[i][1], "red")
                if i != len(prereqs) - 1:
                    self.prereq.insert("end", "\n")
        else:
            self.prereq.insert("end", "None")
        self.prereq.tag_configure("green", foreground="green")
        self.prereq.tag_configure("red", foreground="red")
        self.prereq.config(state="disabled") 
