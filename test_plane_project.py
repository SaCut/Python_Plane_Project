# testing unit
from people.people import Person
from people.passenger import Passenger
from aircraft.aircraft import Aircraft
from flight_trip import FlightTrip
import unittest


class SimpleTest(unittest.TestCase):

    # functions from person
    person = Person()  # create an object of our class

    # def test_add(self):  # naming convention - using 'test' in the name of your function
    #     # will let the interpreter know that this needs to be tested
    #     self.assertEqual(bool(self.test_person.first_name), (not None))

    def test_get_name(self):
        pass

    def test_get_surname(self):
        pass

    def test_get_number(self):
        pass

    # functions from passenger
    passenger = Passenger()

    # def test_get_passport(self):
    #     self.assertEqual(self.test_passenger.get_passport(), "")

    # functions from aircraft
    aircraft = Aircraft(1, 100)

    def test_fly(self):
        pass

    def test_land(self):
        pass

    def fuel_up(self):
        pass

    # functions from flight_trip
    flight_trip = FlightTrip("LGW", "AMS")

    def test_flight_attendees_list_report(self):
        pass

    def test_add_passenger(self):
        pass

    def test_assign_plane(self):
        pass
