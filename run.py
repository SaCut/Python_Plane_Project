import menus
from db_wrapper import DbWrapper


# These lists will eventually contain Passenger and Flight objects
list_passengers = []
list_flights = []

# Lists passengers that have not been assigned to a flight
def list_passengers_with_no_flight():
    if len(list_passengers) == 0:
        print("There are no passengers to list")
    else:
        pass

# Lists all flights with important information
def list_flight_info():
    pass

# This is the running code
if __name__ == "__main__":
    # This decides if the while loop is running
    global running
    running = True

    # This decides which menu to display
    global flag
    flag = "main"

    # # Essential db loading code
    # db_wrapper = DbWrapper()
    # list_passengers = db_wrapper.load_all_passengers()
    while running:
        db = DbWrapper()
        if flag == "main":  # If main then we are on the main menu
            menus.print_main_menu()
            user_in = menus.num_input("Please select an option between 0 and 4:\n", 4)
            menus.handle_main_menu(user_in)
        elif flag == "passengers":  # passengers menu
            menus.passengers_menu()
            flag = "main"
        elif flag == "flights":  # flights menu
            menus.flights_menu()
            flag = "main"
        elif flag == "aircraft":  # aircraft menu
            menus.aircraft_menu()
            flag = "main"
        elif flag == "staff":  # staff menu
            menus.staff_menu()
            flag = "main"
