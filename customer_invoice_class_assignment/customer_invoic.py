""""
Program: invoice_class.py
Author: Grayson Hardin
Last date modified: 11/1/2020
This program takes a list of items and prints a invoice of the item and price.
"""

import locale


class Invoice:
    # List of variables
    def __init__(self, invoice_id, customer, items_with_price={}):
        self.invoice_id = invoice_id
        self.customer = customer
        self.items_with_price = items_with_price

    def add_item(self, value):  # Dictionary
        self.items_with_price.update(
            value
        )

    def create_invoice(self):  # Initiate the invoice
        locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8') # If crashes, check here for previous version
        base_string = f'The customer ID is: {self.customer.customer_id} {self.customer.last_name} {self.customer.first_name} \n{self.customer.phone_number} {self.customer.address}'
        print(base_string)

        for item, price in self.items_with_price.items():
            print(item, ":", locale.currency(price, grouping=True))
        total_before_tax = sum(self.items_with_price.values())
        price_with_tax = (total_before_tax * .06) + total_before_tax  # Calculates tax
        print('The total amount due is:', locale.currency(price_with_tax, grouping=True))


class Customer:
    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address


captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()