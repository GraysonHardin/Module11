import datetime


class Person:
    def __init__(self, person_id, last_name, first_name, phone_number, address):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address


class Student:
    def __init__(self, person, gpa, major, start_date):
        self.person = person
        self.gpa = gpa
        self.major = major
        self.start_date = start_date

    def change_major(self, value):
        self.major = value

    def change_gpa(self, value):
        self.gpa = value

    def display(self):
        print(f'First name: {self.person.first_name}, \nLast Name: {self.person.last_name}, \nPhone number: {self.person.phone_number} \nAddress: {self.person.address} \nGPA is: {self.gpa} \nMajor is: {self.major}')


person = Person(1, 'Hardin', 'Grayson', '832-293-9912', '2020 Liberty St')

student = Student(person, 4.0, 'PolSci', datetime.date(2020, 1, 1))

student.change_gpa(3.0)
student.change_major('CIS')
student.display()
del(person, student)

