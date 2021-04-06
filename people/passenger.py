# class Passenger (inherits from Person)
from people.people import Person


class Passenger(Person):
	def __init__(self):
		super().__init__()
		self.passport_number = None

	def make_from_db(self, pid, first_name, last_name, tax_no, passport_no):
		super().init_person_data(pid, first_name, last_name, tax_no)
		self.passport_number = passport_no
