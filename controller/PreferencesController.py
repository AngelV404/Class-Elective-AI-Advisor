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
        # TODO:connect to db and load saved preferences

        # return data is a tuple:
        #   (
        #    "college",
        #    "department",
        #    "degree_level",
        #    "degree",
        #    "preferred_job",
        #    "counselor_email",
        #   )

        data = None
        return data

    def submit_preferences(self, data):
        # get data as a dict[]
        optional_fields = ["preferred_job", "counselor_email"]

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
        # TODO:save to db, sent to ai

        ai_courses = [
            {
                "title": "CPSC 454 - Cloud Computing",
                "unit": "3",
                "rating": "97",
                "prerequisite": "CPSC 351",
                "explanation": "Learn about distributed systems and cloud security."
            },
            {
                "title": "CPSC 483 - Machine Learning",
                "unit": "3",
                "rating": "95",
                "prerequisite": "CPSC 335",
                "explanation": "Covers supervised and unsupervised learning models."
            }
        ]

        rec_page = self.App.pages["Recommended"]
        rec_page.controller.set_recommendations(ai_courses)
        rec_page.show_subframe(name=None)
        self.App.buttonClicked('Recommended')
