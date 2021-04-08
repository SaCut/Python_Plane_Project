from flask import Flask, render_template, redirect, url_for, request
import login as lg
from db_wrapper import DbWrapper
from menus import *
from people.staff import Staff
app = Flask(__name__)

log = lg.Login()
global db_wrapper

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
    return render_template("flight.html", len=len(dict_flights), dict_flights=dict_flights)


@app.route("/flight_info/<f_id>")
def flight_info(f_id):
    return render_template("flight_info.html", len=len(dict_flights[int(f_id)].passenger_list), f_id=int(f_id), dict_flights=dict_flights)



@app.route("/flight_new/")
def flight_new():
    return render_template("flight_new.html")


@app.route("/passengers/")
def passengers():
    return render_template("passengers.html")


@app.route("/aircraft/")
def aircraft():
    return render_template("aircraft.html")


@app.route("/staff/")
def staff():
    return render_template("staff.html", len=len(dict_staff), dict_staff=dict_staff)


@app.route("/staff_info/<staff_id>",)
def staff_info(staff_id):
    return render_template("staff_info.html", staff_id=staff_id)


@app.route("/staff_new/", methods=["GET", "POST"])
def staff_new():
    if request.method == "POST":
        try:
            s = Staff().make_manual(request.form["firstname"], request.form["secondname"], request.form["age"], db_wrapper)
            dict_staff[s.oid] = s
            return redirect(url_for("staff"))
        except:
            return redirect(url_for("staff_new"))
    return render_template("staff_new.html")


if __name__ == '__main__':
    # Essential db loading code
    db_wrapper = DbWrapper()
    dict_passengers = db_wrapper.load_all_passengers()
    dict_flights = db_wrapper.load_all_flights(dict_passengers)
    dict_aircraft = db_wrapper.load_all_aircraft()
    dict_staff = db_wrapper.load_all_staff()

    app.run(debug=True)
