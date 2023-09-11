# -*- coding: UTF-8 -*-
# What we do ...
# Name: wolke
# Klasse: FS WPFL
# Datum: 01.09.23
# MAC OS 11.6  Python 3.11

# https://www.w3schools.com/python/python_classes.asp
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)


class Student(Person):
    def __init__(self, fname, age, lname='None'):
        super().__init__(fname, age)
        self.lname = lname


# add properties etc.

if __name__ == "__main__":
    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)
    print(p1)
    p1.myfunc()
    s1 = Student('Paul', 19)
    print(s1)
