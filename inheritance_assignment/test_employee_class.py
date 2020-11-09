from inheritance_assignment.employee_class import Employee, SalariedEmployee, HourlyEmployee
import unittest
import datetime


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(
            last_name='Hardin',
            first_name='Grayson',
            address='2084 West Wing',
            phone_number='124-234-0519'
        )

        self.salaried_employee = SalariedEmployee(
            salary=40000,
            start_date=datetime.date(2020, 11, 6),
            last_name='Hardin',
            first_name='Grayson',
            address='2084 West Wing',
            phone_number='124-234-0519'

        )

        self.hourly_employee = HourlyEmployee(
            hourly_pay=10,
            start_date=datetime.date(2020, 11, 6),
            last_name='Hardin',
            first_name='Grayson',
            address='2084 West Wing',
            phone_number='124-234-0519'
        )

    def tearDown(self):
        del self.employee
        del self.salaried_employee
        del self.hourly_employee

    def test_employee_attributes(self):
        expected_last_name = 'Hardin'
        expected_first_name = 'Grayson'
        expected_address = '2084 West Wing'
        expected_phone_number = '124-234-0519'

        self.assertEqual(self.employee.last_name, expected_last_name)
        self.assertEqual(self.employee.first_name, expected_first_name)
        self.assertEqual(self.employee.address, expected_address)
        self.assertEqual(self.employee.phone_number, expected_phone_number)

    def test_salaried_employee_attributes(self):
        expected_salary = 40000
        expected_last_name = 'Hardin'
        expected_first_name = 'Grayson'
        expected_address = '2084 West Wing'
        expected_phone_number = '124-234-0519'

        self.assertEqual(self.salaried_employee.salary, expected_salary)
        self.assertEqual(self.salaried_employee.last_name, expected_last_name)
        self.assertEqual(self.salaried_employee.first_name, expected_first_name)
        self.assertEqual(self.salaried_employee.address, expected_address)
        self.assertEqual(self.salaried_employee.phone_number, expected_phone_number)

    def test_hourly_employee_attributes(self):
        expected_hourly_pay = 10
        expected_last_name = 'Hardin'
        expected_first_name = 'Grayson'
        expected_address = '2084 West Wing'
        expected_phone_number = '124-234-0519'

        self.assertEqual(self.hourly_employee.hourly_pay, expected_hourly_pay)
        self.assertEqual(self.hourly_employee.last_name, expected_last_name)
        self.assertEqual(self.hourly_employee.first_name, expected_first_name)
        self.assertEqual(self.hourly_employee.address, expected_address)
        self.assertEqual(self.hourly_employee.phone_number, expected_phone_number)

    def test_salaried_employee_display_message(self):
        expected_display = f'Last name: Hardin \nFirst name: Grayson \nAddress: 2084 West Wing \nPhone number: 124-234-0519 \nSalary: $40,000.00 \nStart date: 2020-11-06'

        self.assertEqual(self.salaried_employee.display(), expected_display)

    def test_employee_display(self):
        expected_display = f'Hardin Grayson 2084 West Wing 124-234-0519'

        self.assertEqual(self.employee.display(), expected_display)

    def test_salaried_employee_give_raise(self):
        self.salaried_employee.give_raise(45000)
        self.assertEqual(self.salaried_employee.salary, 45000)

    def test_hourly_employee_give_raise(self):
        self.hourly_employee.give_raise(12)
        self.assertEqual(self.hourly_employee.hourly_pay, 12)


if __name__ == '__main__':
    unittest.main()
