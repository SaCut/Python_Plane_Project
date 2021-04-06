# These lists will eventually contain Passenger and Flight objects
list_passengers = []
list_flights = []


# This prints the main menu
def print_main_menu():
    print(f"\n1. Passengers\n"
          f"2. Flights\n"
          f"3. Aircraft\n"
          f"4. Staff\n"
          f"0. exit\n")
    pass

# Displays and handles the passengers menu
def passengers_menu():
    while True:
        print(f"\n1. Create Flight (Trip)\n"
          f"2. Edit Flight (Trip)\n"
          f"0. exit\n")

        user_in = num_input("Please enter a number between 0 and 2\n", 2)
        if user_in == 0:
            break
        elif user_in == 1:
            print("Creating passenger")
        elif user_in == 2:
            print("List the passengers not in a flight so assisstant can add them")

# Displays and handles the flights menu
def flights_menu():
    while True:
        print(f"\n1. Create Flight (Trip)\n"
          f"2. Edit Flight (Trip)\n"
          f"0. exit\n")

        user_in = num_input("Please enter a number between 0 and 2\n", 2)
        if user_in == 0:
            break
        elif user_in == 1:
            print("Creating a new Flight")
        elif user_in == 2:
            print("Choose a flight to edit!")

# Prints the aircraft menu (currently nothing to add)
def aircraft_menu():
    print("In the aircraft menu")

# Prints the staff menu (currently nothing to add)
def staff_menu():
    print("In the staff menu")

# This handles the input for the main menu
# it sets the flag variable for use in deciding what menu to display
def handle_main_menu(num):
    global running
    global flag
    # These values are the same as the menu selection values
    if num == 0:
        running = False
    elif num == 1:
        flag = "passengers"
    elif num == 2:
        flag = "flights"
    elif num == 3:
        flag = "aircraft"
    elif num == 4:
        flag = "staff"


# Lists passengers that have not been assigned to a flight
def list_passengers_with_no_flight():
    if len(list_passengers) == 0:
        print("There are no passengers to list")
    else:
        pass

# Lists all flights with important information
def list_flight_info():
    pass

# Universal input manager, takes an input message and an end index and returns the number entered as an int
def num_input(input_msg, end_index):
    user_input = input(input_msg)
    while not user_input.isdigit() or int(user_input) > end_index:
        user_input = input(f"Please enter a number between 0 and {end_index}:\n")
    return int(user_input)


# This is the running code
if __name__ == "__main__":
    # This decides if the while loop is running
    global running
    running = True

    # This decides which menu to display
    global flag
    flag = "main"

    while running:
        if flag == "main":  # If main then we are on the main menu
            print_main_menu()
            user_in = num_input("Please select an option between 0 and 4:\n", 4)
            handle_main_menu(user_in)
        elif flag == "passengers":  # passengers menu
            passengers_menu()
            flag = "main"
        elif flag == "flights":  # flights menu
            flights_menu()
            flag = "main"
        elif flag == "aircraft":  # aircraft menu
            print("a")
            flag = "main"
        elif flag == "staff":  # staff menu
            print("s")
            flag = "main"
