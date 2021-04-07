class FlightTrip:
    def __init__(self):
        self.flight_id = None
        self.ticket_price = None
        self.aircraft_id = None
        self.duration = None
        self.destination = None
        self.origin = None
        self.passenger_list = None

    def __str__(self):
        return f"{self.flight_id} {self.ticket_price} {self.aircraft_id} {self.destination} {self.duration} {self.origin}"

    def make_from_db(self, flight_id, ticket_price, aircraft_id, destination, duration, origin, passenger_list):
        self.flight_id = flight_id
        self.ticket_price = ticket_price
        self.aircraft_id = aircraft_id
        self.duration = duration
        self.destination = destination
        self.origin = origin
        self.passenger_list = passenger_list

    def make_manual(self, ticket_price, aircraft_id, destination, duration, origin, db_wrapper, flight_dict):
        # make a place holder passenger
        self.make_from_db(None, ticket_price, aircraft_id, destination, duration, origin, [])

        # generate the real one
        db_wrapper.save_single_flight(self, flight_dict)

    def flight_attendees_list_report(self):
        pass

    def add_passenger(self):
        pass

    def assign_plane(self):
        pass
