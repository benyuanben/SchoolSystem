from datetime import datetime

from Course import Course
from Student import Student

class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise ValueError("Invalid Student\n")
        if not isinstance(course, Course):
            raise ValueError("Invalid Course\n")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade
