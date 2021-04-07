from abstract_db_record import AbstractDbObject


class Aircraft(AbstractDbObject):

    def __init__(self, oid, table):
        super().__init__(oid, table)
        self.flight = False  # temp value
        self.flight_capacity = None

    def init_aircraft_data(self, aircraft_id, flight, capacity):
        self.oid = aircraft_id
        self.flight = flight
        self.flight_capacity = capacity

    def fly(self):
        pass

    def land(self):
        pass

    def fuel_up(self):
        pass
