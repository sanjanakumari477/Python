# Example of OOP in Python

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name      # Attribute
        self.age = age        # Attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Derived Class (Inheritance)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call base class constructor
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        # Overriding parent method
        print(f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}")


# Another Derived Class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}, Age: {self.age}, Subject: {self.subject}")


# Main Program
if __name__ == "__main__":
    # Creating objects
    s1 = Student("Rahul", 20, "S101")
    t1 = Teacher("Anita", 35, "Mathematics")

    # Display details
    s1.display_info()
    t1.display_info()
