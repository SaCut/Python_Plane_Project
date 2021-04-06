# class Passenger (inherits from Person)

from People import Person

class Passenger(Person):
	def __init__(self):
		super().__init__()
		self.passport_number = self.get_passport()

	def get_passport(self):
		return input("Please insert the passport number: ")