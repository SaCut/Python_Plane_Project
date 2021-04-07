import pyodbc
from people.passenger import Passenger
from flight_trip import FlightTrip
from aircraft.aircraft import Aircraft


class DbWrapper:

    # Opens a file called server_info.cfg and pulls connection info from there
    def __init__(self):
        try:
            file_lines = open("server_info.cfg", "r").readlines()
            self.ip = file_lines[0].strip("\n")
            self.uname = file_lines[1].strip("\n")
            self.password = file_lines[2].strip("\n")
            self.db_name = file_lines[3].strip("\n")

            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' +
                                             f'SERVER={self.ip};DATABASE={self.db_name};'
                                             f'UID={self.uname};PWD={self.password}')

            self.cursor = self.connection.cursor()
        except FileNotFoundError:
            print(f"server_info.config not found!")
            exit(1)


    """ Passenger Functions"""
    # Will be used to pull information from the database
    def load_all_passengers(self):
        dict_passengers = {}
        self.cursor.execute("SELECT * FROM passengers")
        temp_passenger_list = self.cursor.fetchall()

    # Generate passenger objects
        for val in temp_passenger_list:
            passenger = Passenger()
            passenger.make_from_db(val[0], val[1], val[2], val[3], val[4])
            dict_passengers[val[0]] = passenger

        return dict_passengers

    # save all passengers to the database
    def save_all_passengers(self, dict_passengers):

        for passenger in dict_passengers.values():

            # If passenger doesnt exist
            self.cursor.execute(f"SELECT * FROM passengers where passenger_id = {passenger.pid}")
            if len(self.cursor.fetchall()) is None:
                self.save_single_passenger(passenger, dict_passengers)

        return dict_passengers

    # allows the creation of a single passenger in the db and adds it to the dict
    def save_single_passenger(self, passenger, passenger_dict):
        first_name = passenger.first_name
        last_name = passenger.last_name
        tax_number = passenger.tax_number
        passport_number = passenger.passport_number

        self.cursor.execute(
            f"INSERT INTO passengers "
            + f"VALUES ('{first_name}', '{last_name}', '{tax_number}', '{passport_number}');")

        self.connection.commit()

        # Update the dictionary so that this is always correct
        self.cursor.execute("SELECT MAX(passenger_id) FROM passengers")
        pid = self.cursor.fetchone()[0]
        psg = Passenger()
        psg.make_from_db(pid, first_name, last_name, tax_number, passport_number)
        passenger_dict[pid] = psg

        return passenger_dict

    # Remove a single passenger
    def delete_single_passenger(self, passenger, passenger_dict):
        passenger_dict.pop(passenger.pid)
        self.cursor.execute(f"DELETE FROM flight_orders WHERE passenger_id = {passenger.pid}")
        self.connection.commit()
        self.cursor.execute(f"DELETE FROM passengers WHERE passenger_id = {passenger.pid}")
        self.connection.commit()


    """ Flight functions """
    # Get all passengers on a flight using flight_order
    def get_flight_passengers(self, flight_id, passenger_list):
        self.cursor.execute(f"SELECT passenger_id FROM flight_order WHERE flight_id = {flight_id}")
        flight_passengers = []
        for entry in self.cursor.fetchall():
            flight_passengers.append(passenger_list[entry[0]])

        return flight_passengers

    # Load all FlightTrip objects
    def load_all_flights(self, passenger_dict):
        flight_dict = {}
        self.cursor.execute("SELECT * FROM flight_trip_table")
        temp_flight_list = self.cursor.fetchall()
        for val in temp_flight_list:
            flight = FlightTrip()
            flight.make_from_db(val[0], val[1], val[2], val[3], val[4], val[5], self.get_flight_passengers(val[0], passenger_dict))
            flight_dict[val[0]] = flight

        return flight_dict

    # Save all FlightTrip objects in the database
    def save_all_flights(self, flight_dict):

        for flight in flight_dict.values():
            self.cursor.execute(f"SELECT * FROM flight_trip_table where flight_id = {flight.flight_id}")
            if len(self.cursor.fetchall()) is None:
                self.save_single_flight(flight, flight_dict)

        return flight_dict

    # Save a single flight trip object and add it to the dict
    def save_single_flight(self, flight, flight_dict):
        ticket_price = flight.ticket_price
        aircraft_id = flight.aircraft_id
        destination = flight.destination
        duration = flight.duration
        origin = flight.origin

        self.cursor.execute(
            f"INSERT INTO flight_trip_table "
            + f"VALUES ('{ticket_price}', '{aircraft_id}', '{destination}', '{duration}, {origin}');")

        self.connection.commit()

        self.cursor.execute(f"DELETE FROM flight_orders WHERE flight_id = {flight.flight_id}")
        self.connection.commit()

        for passenger in flight.passenger_list:
            self.add_single_flight_order(passenger, flight)

        # Update the dictionary so that this is always correct
        self.cursor.execute("SELECT MAX(flight_id) FROM flight_trip_table")
        fid = self.cursor.fetchone()[0]
        flt = FlightTrip()
        flt.make_from_db(fid, ticket_price, aircraft_id, destination, duration, origin, flight.passenger_list)
        flight_dict[fid] = flt
        return flight_dict

    # delete a single flight trip from the dict
    def delete_single_flight(self, flight_trip, dict_flights):
        dict_flights.pop(flight_trip.flight_id)
        self.cursor.execute(f"DELETE FROM flight_orders WHERE flight_id = {flight_trip.flight_id}")
        self.connection.commit()
        self.cursor.execute(f"DELETE FROM flight_trip_table WHERE flight_id = {flight_trip.flight_id}")
        self.connection.commit()

    # add a single flight order to the flight_order table
    def add_single_flight_order(self, passenger, flight):
        self.cursor.execute(f"INSERT INTO flight_orders VALUES ({passenger.pid}, {flight.flight_id})")
        self.connection.commit()


    """ Aircraft functions """
    def load_all_aircraft(self):
        aircraft_dict = {}
        self.cursor.execute("SELECT * FROM aircraft")
        temp_aircraft_list = self.cursor.fetchall()
        for val in temp_aircraft_list:
            aircraft = Aircraft()
            flight.make_from_db(val[0], val[1], val[2], val[3], val[4], val[5], self.get_flight_passengers(val[0], passenger_dict))
            flight_dict[val[0]] = flight

        return flight_dict

        pass

    def save_all_aircraft(self, aircraft_dict):
        pass

    def save_single_aircraft(self, aircraft, aircraft_dict):
        pass


    """ Staff functions """
    def load_all_staff(self, staff_dict):
        pass

    def save_all_staff(self, staff_dict):
        pass

    def save_single_staff(self, staff, staff_dict):
        pass


if __name__ == "__main__":
    db = DbWrapper()
    psg = db.load_all_passengers()
    db.load_all_flights(psg)
