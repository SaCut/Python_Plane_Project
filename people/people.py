from abstract_db_record import AbstractDbObject


class Person(AbstractDbObject):

	def __init__(self, oid, table):
		super().__init__(oid, table)
		self.first_name = None
		self.last_name = None
		self.tax_number = None

	def init_person_data(self, oid, first_name, last_name, tax_no):
		self.oid = oid
		self.first_name = first_name
		self.last_name = last_name
		self.tax_number = tax_no
