"""
Program: employee_class.py
Author: Grayson Hardin
Last date modified: 11/9/2020
Similar to previous assignments where Employee has a standard list of attributes - that are similar to global attributes / versatile - while other classes such as hourly and salary set the specific details concerning pay.
"""

import locale
from datetime import date


class Employee:
    def __init__(self, last_name, first_name, address, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def display(self):
        return f'{self.last_name} {self.first_name} {self.address} {self.phone_number}'


class SalariedEmployee(Employee):  # All required attributes for salary employee
    def __init__(self, start_date, salary, last_name, first_name, address, phone_number):
        super().__init__(last_name, first_name, address, phone_number)
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, change_salary):
        self.salary = change_salary

    def display(self):
        locale.setlocale(locale.LC_ALL, '')
        return f'Last name: {self.last_name} \nFirst name: {self.first_name} \nAddress: {self.address} \nPhone number: {self.phone_number} \nSalary: {locale.currency(self.salary, grouping=True)} \nStart date: {self.start_date}'


class HourlyEmployee(Employee):  # All required attributes for hourly employee
    def __init__(self, start_date, hourly_pay, last_name, first_name, address, phone_number):
        super().__init__(last_name, first_name, address, phone_number)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    def give_raise(self, change_hourly_pay):
        self.hourly_pay = change_hourly_pay

    def display(self):
        locale.setlocale(locale.LC_ALL, '')
        return f'Last name: {self.last_name} \nFirst name: {self.first_name} \nAddress: {self.address} \nPhone number: {self.phone_number} \nHourly pay: {locale.currency(self.hourly_pay, grouping=True)} \nStart date: {self.start_date}'


#  Various outputs to show difference between salary and hourly, as well as employee itself
salariedEmployee = SalariedEmployee(date.today(), 40000, 'Hardin', 'Grayson', '2084 West Wing', '124-234-0519')
print(salariedEmployee.display())
salariedEmployee.give_raise(45000)
print(salariedEmployee.display())

employee = Employee('Hardin', 'Grayson', '2084 West Wing', '124-234-0519')
print(employee.display())

hourly_employee = HourlyEmployee(date.today(), 10, 'Hardin', 'Grayson', '2084 West Wing', '124-234-0519')
print(hourly_employee.display())
