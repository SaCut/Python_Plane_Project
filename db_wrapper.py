import pyodbc
from people.passenger import Passenger
from flight_trip import FlightTrip
from aircraft.aircraft import Aircraft
from people.staff import Staff


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
        except FileNotFoundError as err:
            print(err)
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
            passenger.make_from_db(val[0], val[1], val[2], val[3], val[4], self)
            dict_passengers[val[0]] = passenger

        return dict_passengers

    """ Flight functions """
    # Get all passengers on a flight using flight_order
    def get_flight_passengers(self, flight_id, passenger_list):
        self.cursor.execute(f"SELECT DISTINCT passengers_id FROM tickets t "
                            f"JOIN flight_order f ON t.ticket_number = f.ticket_number "
                            f"WHERE f.flight_trip_id = {flight_id}")
        flight_passengers = []
        for entry in self.cursor.fetchall():
            flight_passengers.append(passenger_list[entry[0]])

        return flight_passengers

    # Load all FlightTrip objects
    def load_all_flights(self, passenger_dict):
        flight_dict = {}
        self.cursor.execute("SELECT * FROM flight_trip")
        temp_flight_list = self.cursor.fetchall()
        for val in temp_flight_list:
            flight = FlightTrip()
            flight.make_from_db(val[0], val[1], val[2], val[3], val[4], val[5], self.get_flight_passengers(val[0], passenger_dict))
            flight_dict[val[0]] = flight

        return flight_dict

    # add a single flight order to the flight_order table
    def create_ticket_and_add(self, passenger, flight):
        # make a new ticket for the flight
        self.cursor.execute(f"INSERT INTO flight_order VALUES ({flight.oid})")
        self.connection.commit()

        # Get the ticket number
        self.cursor.execute(f"SELECT MAX(ticket_number) FROM flight_order")
        uid = self.cursor.fetchone()[0]


        print(uid)
        # Assign the passenger to the ticket in the db
        self.cursor.execute(f"INSERT INTO tickets VALUES ({passenger.oid}, {uid})")
        self.connection.commit()

        # Add the ticket to the passenger ticket list
        passenger.tickets.append(uid)

        # add the passenger to the flight object
        flight.passenger_list.append(passenger)


    def load_all_aircraft(self):
        dict_aircraft = {}
        self.cursor.execute("SELECT * FROM aircraft")
        temp_passenger_list = self.cursor.fetchall()

        # Generate passenger objects
        for val in temp_passenger_list:
            aircraft = Aircraft().make_from_db(val[0], val[1], val[2])
            dict_aircraft[val[0]] = aircraft

        return dict_aircraft

    def load_all_staff(self):
        dict_staff = {}
        self.cursor.execute("SELECT * FROM staff")
        temp_passenger_list = self.cursor.fetchall()

        # Generate passenger objects
        for val in temp_passenger_list:
            staff = Staff().make_from_db(val[0], val[1], val[2], val[3])
            dict_staff[val[0]] = staff

        return dict_staff

    def load_passenger_tickets(self, oid):
        try:
            self.cursor.execute(f"SELECT ticket_number FROM tickets WHERE passengers_id = {oid}")
            temp_ticket_list = self.cursor.fetchall()
            print(temp_ticket_list)
            return temp_ticket_list
        except:
            return []

if __name__ == "__main__":
    db = DbWrapper()
    psg = db.load_all_passengers()
    db.load_all_flights(psg)
