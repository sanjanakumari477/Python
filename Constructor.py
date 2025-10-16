class Student:
    
    def __init__(self, name, roll_no, marks):
        # Constructor to initialize values
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

# Creating objects
student1 = Student("Sanjana Kumari", 101, 88)
student2 = Student("Rishi Kumar", 102, 92)

# Display details
student1.display()
print()
student2.display()
