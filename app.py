from flask import Flask, render_template, redirect, url_for, request
import login as lg

app = Flask(__name__)

log = lg.Login()

# creating an app instance
@app.route("/flight/")
def flight():
    return render_template("flight.html")

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

@app.route("/passengers/")
def passengers():
    return render_template("passengers.html")

@app.route("/flight/")
def flight():
    return render_template("flight.html")

# create two more routes, add the functionality for email and password


if __name__=='__main__':
    app.run(debug=True)
