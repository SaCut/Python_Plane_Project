class Aircraft:

    def __init__(self):
        self.aircraft_id = None
        self.flight = False  # temp value
        self.flight_capacity = None

    def init_aircraft_data(self, aircraft_id, flight, capacity):
        self.aircraft_id = aircraft_id
        self.flight = flight
        self.flight_capacity = capacity

    def fly(self):
        pass

    def land(self):
        pass

    def fuel_up(self):
        pass
