# Parent class Person (inherits from DbWrapper)

class Person:  # (DbWrapper)
	def __init__(self, exists=False):
		# self.database = exists
		self.first_name = None
		self.last_name = None
		self.tax_number = None

	def init_person_data(self, first_name, last_name, tax_no):
		self.first_name = first_name
		self.last_name = last_name
		self.tax_number = tax_no

