from abstract_db_record import AbstractDbObject


class FlightTrip (AbstractDbObject):
    def __init__(self):
        super().__init__(None, "flight_trip")
        self.ticket_price = None
        self.aircraft_id = None
        self.duration = None
        self.destination = None
        self.origin = None
        self.passenger_list = None

    def __str__(self):
        return f"{self.oid} {self.ticket_price} {self.aircraft_id} {self.destination} {self.duration} {self.origin}"

    def make_from_db(self, flight_id, ticket_price, aircraft_id, destination, duration, origin, passenger_list):
        self.oid = flight_id
        self.ticket_price = ticket_price
        self.aircraft_id = aircraft_id
        self.duration = duration
        self.destination = destination
        self.origin = origin
        self.passenger_list = passenger_list
        return self

    def __save_and_regenerate_with_id(self, db_wrapper):
        ticket_price = self.ticket_price
        aircraft_id = self.aircraft_id
        destination = self.destination
        duration = self.duration
        origin = self.origin

        if aircraft_id is not None:
            db_wrapper.cursor.execute(
                f"INSERT INTO {self.table} "
                + f"VALUES ({ticket_price}, {aircraft_id}, '{destination}', {duration}, '{origin}');")
        else:
            db_wrapper.cursor.execute(
                f"INSERT INTO {self.table} "
                + f"VALUES ({ticket_price}, Null, '{destination}', {duration}, '{origin}');")

        db_wrapper.connection.commit()

        # delete the passenger list
        try:
            db_wrapper.cursor.execute(f"DELETE FROM flight_order WHERE {self.table}_id = {self.oid}")
            db_wrapper.connection.commit()
        except Exception:
            print("ouch")

        # generate the passenger list
        for passenger in self.passenger_list:
            db_wrapper.add_single_flight_order(passenger, self)

        flt = FlightTrip().make_from_db(self.get_max_id(db_wrapper), ticket_price, aircraft_id, destination, duration, origin, self.passenger_list)
        return flt

    def delete_from_db(self, db_wrapper):
        super().delete_from_db(db_wrapper)
        db_wrapper.cursor.execute(f"DELETE FROM flight_orders WHERE {self.table}_id = {self.oid}")
        db_wrapper.connection.commit()

    def make_manual(self, ticket_price, aircraft_id, destination, duration, origin, db_wrapper):
        # make a place holder passenger
        self.make_from_db(None, ticket_price, aircraft_id, destination, duration, origin, [])

        # generate the real one
        return self.__save_and_regenerate_with_id(db_wrapper)

    def assign_aircraft(self, aircraft, db_wrapper):
        db_wrapper.cursor.execute(f"UPDATE {self.table} "
                                  f"SET aircraft_id = {aircraft.oid} "
                                  f"WHERE {self.table}_id = {self.oid}")


    def add_passenger(self):
        pass

