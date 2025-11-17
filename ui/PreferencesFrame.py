import customtkinter as ctk
from .themes import *
from .csuf_data import *
from db import queries
from controller.PreferencesController import *


class PreferencesFrame(ctk.CTkFrame):
    def __init__(self, parent, App):
        super().__init__(parent, fg_color=FullertonWhite)
        self.user = App.user
        self.controller = PreferencesController(self,App)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)

        #title
        self.title = ctk.CTkLabel(
            self, text='User preferences', font=heading_font)
        self.title.grid(row=0, column=1, sticky='nesw', pady=(20,10))
        
        #warning message
        self.warning_msg=ctk.CTkLabel(self,text='',font=regular_font,text_color=AlertRed)
        self.warning_msg.grid(row=1,column=1,sticky='nesw')

        # input field
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.grid(row=2, column=1)
        self.entry_frame.configure(fg_color=FullertonWhite)
        self.entry_frame.columnconfigure(1, weight=1)

        # college label
        self.college_label = createEntryLabel(self.entry_frame, 'College Of:')
        self.college_label.grid(row=0, column=0, sticky="e", padx=15, pady=10)

        # college dropdown menu with placeholder
        self.college_menu = createOptionMenu(
            self.entry_frame, ['Select a college'] + csuf_colleges, command=self.college_selected)
        self.college_menu.set('Select a college')  # Set initial placeholder
        self.college_menu.grid(row=0, column=1, sticky='w', padx=15, pady=10)

        # department label
        self.department_label = createEntryLabel(
            self.entry_frame, 'Department:')
        self.department_label.grid(
            row=1, column=0, sticky="e", padx=15, pady=10)

        # department dropdown menu with placeholder
        self.department_menu = createOptionMenu(
            self.entry_frame, ['Select a department'], command=self.department_selected)
        # Set initial placeholder
        self.department_menu.set('Select a department')
        self.department_menu.grid(
            row=1, column=1, sticky='w', padx=15, pady=10)

        # degree level label
        self.degree_level_label = createEntryLabel(
            self.entry_frame, 'Degree Level:')
        self.degree_level_label.grid(
            row=2, column=0, sticky="e", padx=15, pady=10)

        # degree level dropdown with placeholder
        self.degree_level_menu = createOptionMenu(
            self.entry_frame, ['Select a degree level'], command=self.degree_level_selected)
        # Set initial placeholder
        self.degree_level_menu.set('Select a degree level')
        self.degree_level_menu.grid(
            row=2, column=1, sticky='w', padx=15, pady=10)

        # degree label
        self.degree_label = createEntryLabel(
            self.entry_frame, 'Degree:')
        self.degree_label.grid(
            row=3, column=0, sticky="e", padx=15, pady=10)

        # degree dropdown with placeholder
        self.degree_menu = createOptionMenu(
            self.entry_frame, ['Select a degree'])
        self.degree_menu.set('Select a degree')  # Set initial placeholder
        self.degree_menu.grid(
            row=3, column=1, sticky='w', padx=15, pady=10)

        # preferred job label
        self.preferred_job_label = createEntryLabel(
            self.entry_frame, 'Preferred Job:')
        self.preferred_job_label.grid(
            row=4, column=0, sticky="e", padx=15, pady=10)

        # preferred job text entry
        self.preferred_job_entry = createEntryBox(self.entry_frame)
        self.preferred_job_entry.grid(
            row=4, column=1, sticky="e", padx=15, pady=10)

        # counselor email label
        self.counselor_email_label = createEntryLabel(
            self.entry_frame, 'Counselor Email:')
        self.counselor_email_label.grid(
            row=5, column=0, sticky="e", padx=15, pady=10)

        # counselor email text entry
        self.counselor_email_entry = createEntryBox(self.entry_frame)
        self.counselor_email_entry.grid(
            row=5, column=1, sticky="e", padx=15, pady=10)

        # create submit button
        self.submit_button = createButton(
            self.entry_frame, 'Submit', command=self.submit_preferences)
        self.submit_button.grid(row=6, column=1, sticky="e", padx=15, pady=10)

        # job description label
        self.job_description_label = ctk.CTkLabel(
            self, text='Job Description:', font=regular_font)
        self.job_description_label.grid(row=3, column=1, pady=(0, 5))

        # job description entry
        self.job_description_entry = createEntryBox(self)
        self.job_description_entry.grid(row=4, column=1)
        self.job_description_entry.configure(width=500)

        self.controller.load_preferences()

    def college_selected(self, selected):
        if selected != 'Select a college':
            departments = self.controller.on_college_selected(selected)
            self.department_menu.configure(
                values=['Select a department'] + departments)
            self.department_menu.set('Select a department')
            self.degree_level_menu.configure(values=['Select a degree level'])
            self.degree_level_menu.set('Select a degree level')
            self.degree_menu.configure(values=['Select a degree'])
            self.degree_menu.set('Select a degree')

    def department_selected(self, selected):
        if selected != 'Select a department':
            degree_levels = self.controller.on_department_selected(selected)
            self.degree_level_menu.configure(
                values=['Select a degree level'] + degree_levels)
            self.degree_level_menu.set('Select a degree level')
            self.degree_menu.configure(values=['Select a degree'])
            self.degree_menu.set('Select a degree')

    def degree_level_selected(self, selected):
        if selected != 'Select a degree level':
            selected_department = self.department_menu.get()
            if (selected_department, selected) in department_degree_to_degrees:
                degrees = self.controller.on_degree_level_selected(
                    selected_department, selected)
                self.degree_menu.configure(
                    values=['Select a degree'] + degrees)
                self.degree_menu.set('Select a degree')

    def display_preferences(self):
        data = self.controller.load_preferences()
        
        if not data:
            self.college_menu.set("Select a college")
            self.department_menu.set("Select a department")
            self.degree_level_menu.set("Select a degree level")
            self.degree_menu.set("Select a degree")
            self.preferred_job_entry.delete(0, "end")
            self.counselor_email_entry.delete(0, "end")

        else:
            (
                college,
                department,
                degree_level,
                degree,
                preferred_job,
                counselor_email,
            ) = data

            self.college_menu.set(college)
            self.department_menu.set(department)
            self.degree_level_menu.set(degree_level)
            self.degree_menu.set(degree)
            self.preferred_job_entry.insert(0, preferred_job or "")
            self.counselor_email_entry.insert(0, counselor_email or "")

    def submit_preferences(self):
        data = {
            "college": self.college_menu.get(),
            "department": self.department_menu.get(),
            "degree_level": self.degree_level_menu.get(),
            "degree": self.degree_menu.get(),
            "preferred_job": self.preferred_job_entry.get(),
            "counselor_email": self.counselor_email_entry.get(),
            "job_description":self.job_description_entry.get(),
        }
        self.controller.submit_preferences(data)
        queries.change_degree(self.user, self.degree_menu)


    def show_message(self, msg):
        self.warning_msg.configure(text=msg)
        
    def hide_message(self):{
        self.warning_msg.configure(text='')
    }

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x600")

    page = PreferencesFrame(root)
    page.pack(fill="both", expand=True)

    root.mainloop()
