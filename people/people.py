# Parent class Person (inherits from DbWrapper)

class Person:  # (DbWrapper)
	def __init__(self):
		self.pid = None
		self.first_name = None
		self.last_name = None
		self.tax_number = None

	def init_person_data(self, pid, first_name, last_name, tax_no):
		self.pid = pid
		self.first_name = first_name
		self.last_name = last_name
		self.tax_number = tax_no

