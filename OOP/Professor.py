from Person import Person

class Professor(Person):
    def __init__(self, first, last, dob, phone, address, salary):
        # initialize the parameters using the __init__ from Person class
        super().__init__(self, first, last, dob, phone, address)
        self.salary = salary
        #used to keep track of courses that the professor is taking
        self.courses = []
        #used to make sure no repeat raises
        self.got_raise = False

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise ValueError("Invalid Course...\n")

        self.courses.append(course)