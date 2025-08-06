class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)
        print("Course:", self.course)

student1 = Student("Sanjana Kumari", 101, "BCA")

student1.display_info()
