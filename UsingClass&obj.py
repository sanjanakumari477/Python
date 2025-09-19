class Student:
    # Constructor to initialize object attributes
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to display student details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    # Method to check grade
    def check_grade(self):
        if self.marks >= 75:
            print("Grade: A")
        elif self.marks >= 50:
            print("Grade: B")
        else:
            print("Grade: C")
# Creating objects of Student class
student1 = Student("Sanjana", 101, 85)
student2 = Student("Amit", 102, 65)

# Accessing methods through objects
student1.display_info()
student1.check_grade()

print("\n")

student2.display_info()
student2.check_grade()
