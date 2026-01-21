Constructor (__init__)
What is Constructor?

A constructor is a special function that runs automatically when an object is created.

👉 Used to initialize data.

Example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sanjana", 22)
print(s1.name)
print(s1.age)


📌 self refers to the current object.
