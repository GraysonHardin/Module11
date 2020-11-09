"""
Program: inheritance_assignment.py
Author: Grayson Hardin
Last date modified: 11/9/2020

Program takes a list of values from Employee and allows the Manager to inherit them and specific their details. For example, Manager can take in a department to specific where the Employee should go.
"""

import locale
from datetime import date


class Employee:
    def __init__(self, start_date, salary, last_name, first_name, address, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, change_salary):
        self.salary = change_salary

    def display(self):
        locale.setlocale(locale.LC_ALL, '')
        return f'Last name: {self.last_name} \nFirst name: {self.first_name} \nAddress: {self.address} \nPhone number: {self.phone_number} \nSalary: {locale.currency(self.salary, grouping=True)} \nStart date: {self.start_date}'


class Person:
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Manager(Employee, Person):
    def __init__(self, department, start_date, salary, last_name, first_name, address, phone_number, direct_reports=[]):
        Employee.__init__(self, start_date, salary, last_name, first_name, address, phone_number)
        Person.__init__(self, last_name, first_name, address)
        self._department = department
        self._direct_reports = direct_reports

    def display_direct_reports(self):
        for report in self._direct_reports:
            print(report.display())


employee = Employee(date.today(), 40000, 'Hardin', 'Bob', '1192 Red Drive', '515-319-8142')

manager = Manager('Warehouse', date.today(), 40000, 'Hardin', 'Grayson', '5412 Blue Drive', '515-219-6129', [employee])
print(manager.display())  # Employee display was utilized

manager.display_direct_reports()
manager.give_raise(42000)
print(manager.display())  # Employee display was utilized

del employee
del manager
