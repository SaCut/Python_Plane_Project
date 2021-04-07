from abstract_db_record import AbstractDbObject


class Person(AbstractDbObject):

	def __init__(self, oid, table):
		super().__init__(oid, table)
		self.first_name = None
		self.last_name = None
		self.age = None
		self.tickets = []

	def init_person_data(self, oid, first_name, last_name, age, db_wrapper):
		self.oid = oid
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.tickets = db_wrapper.load_passenger_tickets(self.oid)
