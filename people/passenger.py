# class Passenger (inherits from Person)
from people.people import Person


class Passenger(Person):
	def __init__(self):
		super().__init__()
		self.passport_number = None

	def init_passport(self):
		self.passport_number = input("Please insert the passport number: ")