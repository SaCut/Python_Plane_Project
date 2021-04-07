# To keep run.py cleaner - holds all the code related to displaying and handling menus
from people.passenger import Passenger
from flight_trip import FlightTrip

# This prints the main menu
def print_main_menu():
    print(f"\n1. Passengers\n"
          f"2. Flights\n"
          f"3. Aircraft\n"
          f"4. Staff\n"
          f"0. exit\n")
    pass

# This handles the input for the main menu
# it sets the flag variable for use in deciding what menu to display
def handle_main_menu(num):
    # These values are the same as the menu selection values
    if num == 0:
        return "exit"
    elif num == 1:
        return "passengers"
    elif num == 2:
        return "flights"
    elif num == 3:
        return "aircraft"
    elif num == 4:
        return "staff"

# Displays and handles the passengers menu
def passengers_menu(db_wrapper, passenger_dict, dict_flights):
    while True:
        print(f"\n1. Create passenger\n"
              f"2. List passengers not on any flight\n"
              f"3. List passengers on a flight\n"
              f"0. exit\n")

        user_in = num_input("Please enter a number between 0 and 3\n", 3)
        if user_in == 0:
            break
        elif user_in == 1:
            print("Creating passenger")

            # make a passenger and add it to the dict
            p = Passenger().make_manual("ex", "passenger", "tax", "passport", db_wrapper)
            passenger_dict[p.oid] = p

        elif user_in == 2:
            print("List the passengers not in a flight so assistant can add them")
            for p in passenger_dict.values():
                print(p)

        elif user_in == 3:
            flight_no = int(input("Please enter a flight ID:\n"))
            try:
                print(f"Passengers on flight {flight_no}:")
                flight_passengers = dict_flights[flight_no].passenger_list
                for passenger in flight_passengers:
                    print(f"{passenger.first_name} {passenger.last_name} - {passenger.passport_number}\n")
            except KeyError:
                print("Flight not found")


# Displays and handles the flights menu
def flights_menu(db_wrapper, flight_dict):
    while True:
        print(f"\n1. Create Flight (Trip)\n"
          f"2. List Flights (Trip)\n"
          f"0. exit\n")

        user_in = num_input("Please enter a number between 0 and 2\n", 2)
        if user_in == 0:
            break
        elif user_in == 1:
            print("Creating a new Flight")

            # make a flight_trip and add it to the dict
            t = FlightTrip().make_manual(210, None, "destination", 24, "origin", db_wrapper)
            flight_dict[t.oid] = t
        elif user_in == 2:
            print("List of flights!")
            for f in flight_dict:
                print(f)

# Prints the aircraft menu (currently nothing to add)
def aircraft_menu():
    print("In the aircraft menu")

# Prints the staff menu (currently nothing to add)
def staff_menu():
    print("In the staff menu")

# Universal input manager, takes an input message and an end index and returns the number entered as an int
def num_input(input_msg, end_index):
    user_input = input(input_msg)
    while not user_input.isdigit() or int(user_input) > end_index:
        user_input = input(f"Please enter a number between 0 and {end_index}:\n")
    return int(user_input)

# Allows the user to enter text information, following the given prompt
def text_input(input_msg):
    exit_prompt = " Or enter 'done' to exit. "
    # user_input = input(input_msg)
    while True:
        user_input = input(input_msg + exit_prompt)  # ask the user for input

        # exit it without returning here
        if user_input == "done":
            break

        confirm_msg = "You entered: '" + user_input + "'. Do you wish to continue? (y/n) "

        user_conf = input(confirm_msg)

        if user_conf.lower() == "y" or user_conf.lower == "yes":
            return user_input
        elif user_conf.lower ==  "done":
            break  # exit it without returning here
