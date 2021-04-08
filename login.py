# As an airport Assistant, I want to be able to assign and/or change a plane to my flight_trip, and input my password, so I can handle the problem

# file to handle logging auth
from db_wrapper import DbWrapper
import hashlib, os

class Login:
    def __init__(self):
        self.database = DbWrapper()

    def attempt_login(self):
        attempts = 5
        
        while attempts > 0:
            print(f"Attempts left: {str(attempts)}")
            username = input("Insert user name: ")
            
            all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
            all_unames = [list(uname)[0] for uname in all_unames]

            if username in all_unames:

                # retrieving the salt from the database
                get_salt = self.database.cursor.execute(f"SELECT salt FROM login_credentials WHERE username = '{username}'").fetchone()
                get_salt = list(get_salt)[0].encode('utf-8')

                # retrieving the hashed password from the database
                get_pswd = self.database.cursor.execute(f"SELECT password FROM login_credentials WHERE username = '{username}'").fetchone()
                get_pswd = list(get_pswd)[0]

                run_pswd = input("Insert password: ")

                # hashing the user-given password
                check_pswd = self.hash_password(username, run_pswd)

                if check_pswd == get_pswd:
                    return True # returns True when the password is correct
                else:
                    attempts -= 1
                    print(f"Incorrect password\n{str(attempts)} attempts remaining.")
                    continue

            else:
                print("Username not found\n")
                continue

        print("Login unsuccessful\n")
        return False # return False if the correct password has not been inserted

    def new_account(self):
        username = input("Insert new user name: ")
        password = input("Insert new password: ")
        salt = os.urandom(10) # this is a binary string encoded in utf-8

        salt = self.bin_to_str(salt)

        all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
        all_unames = [list(uname)[0] for uname in all_unames]

        if username not in all_unames: # if there is no similar username

            hash_pswd = self.hash_password(username, password)


            self.database.cursor.execute(f"INSERT INTO login_credentials (username, salt, password) VALUES ('{username}', '{salt}', '{hash_pswd}');")

            self.database.connection.commit()

            return True # returns True when the credentials have been created

        else:
            print("Sorry, that username is already in use")
            return False # returns False if the credentuals haven't been created


    def is_username(self, username):
        username = str(username)

        all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
        all_unames = [list(uname)[0] for uname in all_unames]

        if username in all_unames:
            return True
        else:
            return False

    def bin_to_str(self, binary):
        string = str(binary) # replace() requires a string
        string = string.replace("'", "k")
        string = string.replace("/", "j")
        string = string.replace("\\", "n")
        string = string.replace("\"", "o")

        return string


    def hash_password(self, username, password):
        username = str(username)
        password = str(password)

        all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
        all_unames = [list(uname)[0] for uname in all_unames]

        if username in all_unames:
            # retrieving the salt from the database
            get_salt = self.database.cursor.execute(f"SELECT salt FROM login_credentials WHERE username = '{username}'").fetchone()
            get_salt = get_salt.salt



        # hashing the password
        hash_pswd = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), get_salt.encode("utf-8"), 1000)
        hash_pswd = self.bin_to_str(hash_pswd)

        # print(hash_pswd)

        return hash_pswd

    def right_password(self, username, password):
        username = str(username)
        password = str(password)

        # retrieving the hashed password from the database
        get_pswd = self.database.cursor.execute(f"SELECT password FROM login_credentials WHERE username = '{username}'").fetchone()
        get_pswd = get_pswd.password

        print("2")

        # hashing the user-given password
        check_pswd = self.hash_password(username, password)        

        print(check_pswd)
        print(get_pswd)


        if check_pswd == get_pswd:
            return True # returns True when the password is correct

        else:
            return False # returns False when the password is wrong


if __name__=='__main__':
    log_object = Login()
    log_object.new_account()
