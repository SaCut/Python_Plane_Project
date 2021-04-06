# file to handle logging auth
from db_wrapper import DbWrapper

def login():
    pass

def sign_up():
    pass

uname = hash(input("Insert user name: ") + "username") # should return an int # test
pswd = hash(input("Insert password: ") + "password") # should return an int # test

database = DbWrapper()

# database.cursor.execute(f"INSERT INTO login_credentials (username, user_password) VALUES ({uname}, {pswd});")

# database.connection.commit()

try:
    get_pswd = database.cursor.execute(f"SELECT user_password FROM login_credentials WHERE username = {uname};")
    print(get_pswd.fetchone())
except:
    print("Username not found")

# if get_hashes == 