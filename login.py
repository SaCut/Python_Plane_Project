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
                get_pswd = list(get_pswd)[0].encode('utf-8')

                run_pswd = input("Insert password: ")

                # hashing the user-given password
                check_pswd = hashlib.pbkdf2_hmac('sha256', run_pswd.encode('utf-8'), get_salt, 1000)

                if check_pswd == get_pswd:
                    return True # returns True when the password is correct

            else:
                print("Username not found\n")
                attempts -= 1
                continue

        return False # return False if the correct password has not been inserted

    def new_account(self):
        username = input("Insert new user name: ")
        password = input("Insert new password: ")
        salt = os.urandom(10) # this is a binary string encoded in utf-8

        all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
        all_unames = [list(uname)[0] for uname in all_unames]

        if username not in all_unames: # if there is no similar username
            user = {
            "username": username,
            "salt": salt,
            }

            user["password"] = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), user["salt"], 1000) # hashing the password

            uname = user["username"]
            # removing troublesome characters
            salt = str(user["salt"])
            salt = salt.replace("'", "k")
            salt = salt.replace("/", "j")
            salt = salt.replace("\\", "n")
            salt = salt.replace("\"", "o")

            #removing troublesome characters
            pwd = str(user["password"])
            pwd = pwd.replace("'", "k")
            pwd = pwd.replace("/", "j")
            pwd = pwd.replace("\\", "n")
            pwd = pwd.replace("\"", "o")


            self.database.cursor.execute(f"INSERT INTO login_credentials (username, salt, password) VALUES ('{uname}', '{salt}', '{pwd}');")

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


    def hash_password(self, username, password):
        username = str(username)
        password = str(password)

        all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
        all_unames = [list(uname)[0] for uname in all_unames]

        if username in all_unames:
            # retrieving the salt from the database
            get_salt = self.database.cursor.execute(f"SELECT salt FROM login_credentials WHERE username = '{username}'").fetchone()
            get_salt = get_salt.salt

        # print("1")
        # print(password)
        # print(get_salt)

        # hashing the password
        hash_pswd = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), get_salt.encode("utf-8"), 1000)

        #removing troublesome characters
        hash_pswd = str(hash_pswd) # replace() requires a string
        hash_pswd = hash_pswd.replace("'", "k")
        hash_pswd = hash_pswd.replace("/", "j")
        hash_pswd = hash_pswd.replace("\\", "n")
        hash_pswd = hash_pswd.replace("\"", "o")

        print(hash_pswd)

        return hash_pswd

    def right_password(self, username, password):
        username = str(username)
        password = str(password)

        all_unames = self.database.cursor.execute("SELECT username FROM login_credentials").fetchall()
        all_unames = [list(uname)[0] for uname in all_unames]

        # retrieving the salt from the database
        get_salt = self.database.cursor.execute(f"SELECT salt FROM login_credentials WHERE username = '{username}'").fetchone()
        get_salt = get_salt.salt

        # retrieving the hashed password from the database
        get_pswd = self.database.cursor.execute(f"SELECT password FROM login_credentials WHERE username = '{username}'").fetchone()
        get_pswd = get_pswd.password

        # print("2")
        # print(password)
        # print(get_salt)

        # hashing the user-given password
        check_pswd = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), get_salt.encode('utf-8'), 1000)

        #removing troublesome characters
        check_pswd = str(check_pswd) # replace() requires a string
        check_pswd = check_pswd.replace("'", "k")
        check_pswd = check_pswd.replace("/", "j")
        check_pswd = check_pswd.replace("\\", "n")
        check_pswd = check_pswd.replace("\"", "o")

        # print(check_pswd)

        # print(check_pswd)
        # print(get_pswd)


        if check_pswd == get_pswd:
            return True # returns True when the password is correct

        else:
            return False # returns False when the password is wrong


if __name__=='__main__':
    log_object = Login()
    log_object.new_account()
