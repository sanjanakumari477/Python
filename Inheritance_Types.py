🔹 There are five types of inheritance in Python.

They are:

1.Single Inheritance – One child inherits from one parent

2.Multiple Inheritance – One child inherits from multiple parents

3.Multilevel Inheritance – A class inherits from another derived class

4.Hierarchical Inheritance – Multiple children inherit from one parent

5.Hybrid Inheritance – Combination of two or more types of inheritance

📌 Python supports all five types.

🔹 Q3. What is super() in Python?

super() is a built-in function used to access methods and constructors of the parent (super) class from the child class.

🔹 Why use super()?

To call parent class constructor

To reuse parent class methods

To avoid duplicate code

Useful in multiple inheritance

🔹 What is MRO? (Method Resolution Order)

MRO (Method Resolution Order) is the order in which Python searches for a method or attribute in a hierarchy of classes, especially in multiple inheritance.

📌 MRO tells Python which method to execute first if the same method name exists in multiple parent classes.

🔹 Why is MRO Needed?

In multiple inheritance, different parent classes may have methods with the same name.
MRO helps Python decide:
