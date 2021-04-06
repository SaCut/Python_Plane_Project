list_passengers = []
list_flights = []


def print_menu():
    pass


#  Universal input manager
def num_input(input_msg, end_index):
    user_input = input(input_msg)
    while not user_input.isdigit() or user_input > end_index:
        user_input = input(f"Please enter a number between 0 and {end_index}")
    return user_input



if __name__ == "__main__":
    while True:
