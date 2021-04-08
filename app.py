from flask import Flask, render_template, redirect, url_for, request
import login as lg
from db_wrapper import DbWrapper
app = Flask(__name__)

log = lg.Login()
global db

global dict_passengers
global dict_flights
global dict_aircraft
global dict_staff

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if not log.is_username(request.form["username"]): #check if username is NOT in database
            print("1")
            error = "Invalid username.Please try again"
        
        else: # when username is in database

            # hash password
            psswd = log.hash_password(request.form["username"], request.form["password"])

            if not log.right_password(request.form["username"], request.form["password"]):
                print("2")
                # print((type(request.form["username"]), request.form["password"]))
                error = "Invalid Password. Please try again."
            else:
                print("3")
                return redirect(url_for("home"))

    return render_template("login.html", error=error)


@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/flight/")
def flight():

    return render_template("flight.html")


@app.route("/passengers/")
def passengers():
    return render_template("passengers.html")


@app.route("/aircraft/")
def aircraft():
    return render_template("aircraft.html")


@app.route("/staff/")
def staff():
    return render_template("staff.html")


if __name__ == '__main__':
    # Essential db loading code
    db_wrapper = DbWrapper()
    dict_passengers = db_wrapper.load_all_passengers()
    dict_flights = db_wrapper.load_all_flights(dict_passengers)
    dict_aircraft = db_wrapper.load_all_aircraft()
    dict_staff = db_wrapper.load_all_staff()

    app.run(debug=True)
