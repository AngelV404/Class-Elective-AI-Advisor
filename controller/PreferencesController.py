from ui.csuf_data import *


class PreferencesController:
    def __init__(self, view, App):
        self.view = view
        self.App = App

    # ----------Drop Down Menu Logic---------------------
    def on_college_selected(self, college):
        return csuf_departments.get(college, [])

    def on_department_selected(self, department):
        return department_to_degree_levels.get(department, [])

    def on_degree_level_selected(self, department, level):
        key = (department, level)
        return department_degree_to_degrees.get(key, [])

# ---------------------------------------------------------
    def load_preferences(self):
        # TODO:load saved preferences from db

        data = None
        return data

    def submit_preferences(self, data):
        # get data as a dict[]
        optional_fields = ["job_description", "counselor_email"]

        for key, value in data.items():
            if key in optional_fields:
                continue

            value = value.strip()
            if value == "" or value.startswith('Select'):
                self.view.show_message(
                    f'Please fill in or select a valid {key}')
                return
        self.view.hide_message()
        print(data)
        # TODO:save preference to db, sent to ai, get back ai recommended courses
        

        ai_courses = [
            {
                "Code": "CPSC 454",
                "Name": "Cloud Computing and Security",
                "Description": "Learn about distributed systems and cloud security.",
                "Credits": 3,
                "Department": "Computer Science",
                "Prerequisite": "CPSC 351",
                "Explanation":"some explanation from ai"
            },
            {
                "Code": "CPSC 483",
                "Name": "Machine Learning",
                "Description": "Covers supervised and unsupervised learning models.",
                "Credits": 3,
                "Department": "Computer Science",
                "Prerequisite": "CPSC 335",
                "Explanation":"some explanation from ai"
            },
            {
                "Code": "CPSC 471",
                "Name": "Computer Communications",
                "Description": "Focuses on data communications and networking fundamentals.",
                "Credits": 3,
                "Department": "Computer Science",
                "Prerequisite": "CPSC 351",
                "Explanation":"some explanation from ai"
            }
]


        rec_page = self.App.pages["Recommended"]
        rec_page.controller.set_recommendations(ai_courses)
        rec_page.show_subframe(name=None)
        self.App.buttonClicked('Recommended')
