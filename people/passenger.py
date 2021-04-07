# As an airport Assistant, I want to be able to create a passenger with a name and Passport number, so that I can add them to a flight
# User should be able to create a new object of the Passenger class
# A passenger should only be created if all information is provided
# class Passenger (inherits from Person)
from people.people import Person


class Passenger(Person):
    def __init__(self):
        super().__init__()
        self.passport_number = None

    # helpful for debugging
    def __str__(self):
      return f"{self.pid}. {self.first_name} {self.last_name} {self.tax_number} {self.passport_number}"

    def make_from_db(self, pid, first_name, last_name, tax_no, passport_no):
      super().init_person_data(pid, first_name, last_name, tax_no)
      self.passport_number = passport_no

    def make_manual(self, first_name, last_name, tax_no, passport_no, db_wrapper, passenger_dict):
        # make a place holder passenger
        self.make_from_db(None, first_name, last_name, tax_no, passport_no)

        # generate the real one
        db_wrapper.save_single_passenger(self, passenger_dict)
