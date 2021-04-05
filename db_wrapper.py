import pyodbc


class DbWrapper:

    # Opens a file called server_info.cfg and pulls connection info from there
    def __init__(self):
        file_lines = open("server_info.cfg", "r").readlines()
        self.ip = file_lines[0].strip("\n")
        self.uname = file_lines[1].strip("\n")
        self.password = file_lines[2].strip("\n")
        self.DbName = file_lines[3].strip("\n")

        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' +
                                         f'SERVER={self.ip};DATABASE={self.DbName};'
                                         f'UID={self.uname};PWD={self.password}')

        self.cursor = self.connection.cursor()

    # Will be used to pull information from the database
    def load_from_db(self, table, **kwargs):
        pass

    # Will be used to store information in the database
    def save_to_db(self, table, **kwargs):
        pass
