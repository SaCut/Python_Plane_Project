list_passengers = []
list_flights = []


def print_main_menu():
    print(f"\n1. Passengers\n"
          f"2. Flights\n"
          f"3. Aircraft\n"
          f"4. Staff\n"
          f"0. exit\n")
    pass


def handle_main_menu(num):
    pass


# Universal input manager
def num_input(input_msg, end_index):
    user_input = input(input_msg)
    while not user_input.isdigit() or int(user_input) > end_index:
        user_input = input(f"Please enter a number between 0 and {end_index}:\n")
    return int(user_input)


if __name__ == "__main__":
    while True:
        print_main_menu()
        user_in = num_input("Please select an option between 0 and 4:\n", 4)
        handle_main_menu(user_in)