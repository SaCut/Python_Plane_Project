# As an airport Assistant, I want to be able to assign and/or change a plane to my flight_trip, and input my password, so I can handle the problem

# file to handle logging auth
from db_wrapper import DbWrapper
import hashlib, os

class Login:
    def __init__(self):
        self.database = DbWrapper()
        self.cursor = self.database.cursor

    def attempt_login(self):
        attempts = 5
        
        while attempts > 0:
            print(f"Attempts left: {str(attempts)}")
            username = input("Insert user name: ")
            
            all_unames = self.cursor.execute("SELECT username FROM login_credentials").fetchall()

            if username in all_unames:

                # retrieving the salt from the database
                get_salt = self.cursor.execute(f"SELECT salt FROM login_credentials WHERE username = {username}")

                # retrieving the hashed password from the database
                get_pswd = self.cursor.execute(f"SELECT password FROM login_credentials WHERE username = {username}")

                run_pswd = input("Insert password: ")

                # hashing the user-given password
                check_pswd = hashlib.pbkdf2_hmac('sha256', run_pswd.encode('utf-8'), user.["salt"], 1000)

                if check_pswd == get_pswd:
                    return True # returns True when the password is correct

            else:
                print("Username not found\n")
                continue

            attempts -= 1

        return False # return False if the correct password has not been inserted

    def new_account(self, username=input("Insert new user name: "), password=input("Insert new password: ")):

        all_unames = self.cursor.execute("SELECT username FROM login_credentials").fetchall()

        if username not in all_unames: # if there is no similar username
            user = {
            "username": username,
            "salt": os.urandom(10),
            }

            user["password"] = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), user.["salt"], 1000) # hashing the password

            self.cursor.execute("INSERT INTO login_credentials (username, salt, password) "
                + f"VALUES ({user["username"]}, {user["salt"]}, {user["password"]});")

            self.database.connection.commit()

            return True # returns True when the credentials have been created

        else:
            print("Sorry, that username is already in use")
            return False # returns False if the credentuals haven't been created
