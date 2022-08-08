from Professor import Professor
from Enroll import Enroll

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max_ = max_
        self.min_ = min_
        #we might have several professors teaching the course... we will also need to validate that the professors are correct inputs
        #it most have at least one professor teaching the course
        self.professors = []
        #used to track students who are enrolled in the course
        self.enrollments = []

        #like with Person class, we need to check that the inputs for the professors[] are valid
        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                assert isinstance(entry, Professor), "Invalid professor...\n"

            self.professors = professor
        else:
            # if address is not in the prev two forms, then it is invalid input
            raise ValueError("Invalid professor Input...\n")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError("Invalid professor Input...\n")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError("Invalid Enroll\n")

        if len(self.enrollments) == self.max_:
            raise ValueError("Cannot Enroll, course is full...\n")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min_


    #should consider having methods for removing professors or enrollments

