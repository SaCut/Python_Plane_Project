import pyodbc


class DbWrapper:

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

    def load_from_db(self, table, **kwargs):
        pass

    def save_to_db(self, table, **kwargs):
        pass

