# As an airport Assistant, I want to be able to create a passenger with a name and Passport number, so that I can add them to a flight
# User should be able to create a new object of the Passenger class
# A passenger should only be created if all information is provided
# class Passenger (inherits from Person)
from people import Person

class Passenger(Person):
	def __init__(self):
		super().__init__()
		self.passport_number = None

	def make_from_db(self, pid, first_name, last_name, tax_no, passport_no):
		super().init_person_data(pid, first_name, last_name, tax_no)
		self.passport_number = passport_no
