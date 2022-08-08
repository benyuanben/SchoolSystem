from Person import Person
from Enroll import Enroll

class Student(Person):
    def __init__(self, first, last, dob, phone, address, international=False):
        #initialize the parameters using the __init__ from Person class
        super().__init__(self, first, last, dob, phone, address)
        self.international = international
        #used to store enrolled classes later on
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError("Invalid Enroll...\n")

        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3