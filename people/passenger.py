# class Passenger (inherits from Person)
from people.people import Person


class Passenger(Person):
	def __init__(self):
		super().__init__()
		self.passport_number = None

	def make_from_db(self, first_name, last_name, tax_no, passport_no):
		super().init_person_data(first_name, last_name, tax_no)
		self.passport_number = passport_no

	def init_passport(self):
		self.passport_number = input("Please insert the passport number: ")