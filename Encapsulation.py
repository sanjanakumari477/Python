class Person:
    def __init__(self, age):
        self.__age = age     # name-mangled: _Person__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        if val < 0: raise ValueError("age >= 0")
        self.__age = val
