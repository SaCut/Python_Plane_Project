# Parent class Person (inherits from DbWrapper)

class Person(): # (DbWrapper)
	def __init__(self, exists=False):
		self.database = exists
		self.first_name = self.get_name()
		self.last_name = self.get_surname()
		self.tax_number = self.get_number()

	def get_name(self):
		if not self.database:
			return input("\nPlease insert the first name: ")

	def get_surname(self):
		if not self.database:
			return input("\nPlease insert the last name: ")

	def get_number(self):
		return input("\nPlease insert the last tax number: ")
