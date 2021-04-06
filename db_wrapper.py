import pyodbc
from people.passenger import Passenger


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

    # Will be used to pull information from the database
    def load_all_passengers(self):
        list_passengers = []
        self.cursor.execute("SELECT * FROM passengers")
        temp_passenger_list = self.cursor.fetchall()
        for val in temp_passenger_list:
            passenger = Passenger()
            passenger.make_from_db(val[0], val[1], val[2], val[3], val[4])
            list_passengers.append(passenger)

        # for passenger in list_passengers:
        #     print(f"{passenger.pid} {passenger.first_name} {passenger.last_name}")

        return list_passengers

    # Will be used to store information in the database
    def save_all_passengers(self, list_passengers):
        # passenger = Passenger()
        # passenger.make_from_db(None, "Isobel", "Fitt-Conway", "aasdasdas", "98989922")
        # list_passengers.append(passenger)

        for passenger in list_passengers:

            if passenger.pid is None:
                first_name = passenger.first_name
                last_name = passenger.last_name
                tax_number = passenger.tax_number
                passport_number = passenger.passport_number

                self.cursor.execute(
                    f"INSERT INTO passengers "
                    + f"VALUES ('{first_name}', '{last_name}', '{tax_number}', '{passport_number}');")

                self.connection.commit()

        # self.cursor.execute("SELECT * FROM passengers")
        # print(self.cursor.fetchall())

    def load_all_flights(self):
        pass

    def save_all_flights(self):
        pass


if __name__ == "__main__":
    db = DbWrapper()
    db.load_all_passengers()
