# Parent class Person (inherits from DbWrapper)

class Person(): # (DbWrapper)
	def __init__(self, exists=False):
		# self.database = exists
		self.first_name = None
		self.last_name = None
		self.tax_number = None

	def init_person_data(self):
		self.first_name = input("\nPlease insert the first name: ")
		self.last_name = input("\nPlease insert the last name: ")
		self.tax_number = input("\nPlease insert the tax number: ")

