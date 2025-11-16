

class RecommendedController:
    def __init__(self, view):
        self.view = view
        self.recommendations = []  # recommended course data
        self.current_course = None
        
        # courses=
        # [
        # "Code": "CPSC 471",
        # "Name": "Computer Communications",
        # "Description": "Focuses on data communications and networking fundamentals.",
        # "Credits": 3,
        # "Department": "Computer Science",
        # "Prerequisite": "CPSC 351",
        # "Rating": 90
        # ]
    def set_recommendations(self, courses):
        self.recommendation = courses
        self.view.course_list.clear()

        for course in courses:
            self.view.course_list.add_course_card(
                code=course["Code"],
                name=course["Name"],
                unit=course["Credits"],
                prerequisite=course.get("Prerequisite", "None"),
                on_explanation=lambda c=course: self.show_explanation(c),
                on_options=lambda c=course: self.show_options(c)
            )

    def show_explanation(self, course):
        explanation = course.get("Description", "No explanation available.")
        self.view.subframes["explanation"].set_text(explanation)
        self.view.show_subframe("explanation")

    def show_current_explanation(self):
        if self.current_course:
            self.view.subframes['explanation'].set_text(
                self.current_course.get(
                    "Description", "No explanation available.")
            )
            self.view.show_subframe("explanation")

    def show_options(self, course):

        self.current_course = course
        self.view.subframes["share"].reset()
        self.view.show_subframe("options")

    def save_course(self):
        if self.current_course is not None:
            # TODO:save course to db
            self.view.show_subframe("saved")

    def share_with_advisor(self):
        if self.current_course is not None:
            # TODO: sent email to advisor
            pass
