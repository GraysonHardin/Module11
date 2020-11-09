""""
Program: derived_class.py
Author: Grayson Hardin
Last date modified: 11/9/2020

Program that prints student ID, name, and optional parameters.
"""


class Person:
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Student(Person):
    def __init__(self, student_id, last_name, first_name, major='Computer Science', gpa=0.0):
        super().__init__(last_name, first_name)
        self.student_id = student_id
        self._major = major
        self._gpa = gpa

    def display(self):
        return f'{self.student_id} {self._last_name} {self._first_name} {self._address} {self._major} {self._gpa}'


# Driver
my_student = Student(900111111, 'Hardin', 'Grayson')  # Base requirements
print(my_student.display())
my_student = Student(900111111, 'Hardin', 'Grayson', 'Computer Engineering')  # Added an optional value
print(my_student.display())
my_student = Student(900111111, 'Hardin', 'Grayson', 'Computer Engineering', 4.0)  # Added two optional values
print(my_student.display())
del my_student
