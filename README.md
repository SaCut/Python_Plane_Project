# Python Plane Project
- This is a repo for the first group project in the Sparta Global training
- The project is written in Python
- The team members are Adedunni Adebusuyi, Benjamin Ranson, Isobel Fitt-Conway, Saverio Cutrupi

### Tools
- Trello
- Git and GitHub
- Python
- SQL

### Workflow
- Agile methodology
- Scrum framework

## Files and Functionality
### [abstract_db_record.py](abstract_db_record.py)
The base/parent class for all database objects.

### [app.py](app.py)
This handles which web pages should be served to the user.

### [db_wrapper.py](db_wrapper.py)
Manages the connection between the SQL database and Python code. Saving and loading to and from the database is handled here.

### [flight_trip.py](flight_trip.py)
An object. Each instance contains information about a flight, hence the name.

### [login.py](login.py)
Handles the staff login.

### [menus.py](menus.py)
Holds all the code used for displaying and handling the menus used in `run.py`. Created solely to keep `run.py` neat.

### [run.py](run.py)
This is the 'main' part of the programme from the user's perspective. This is where they interact with the UI (graphical or otherwise) to create and manage passengers, flights, and aircrafts.

### [test_plane_project.py](test_plane_project.py)
The unit tests are run from this file.

### [aircraft](./aircraft)
A package for all the aircraft classes.

[aircraft.py](./aircraft/aircraft.py) -
The parent class for all the aircraft classes.

[helicopter.py](./aircraft/helicopter.py) -
A child of `Aircraft`. It currently inherits all its properties.

[plane.py](./aircraft/plane.py) -
A child of `Aircraft`. It currently inherits all its properties and also extends them with the variable `plane_model`.

### [GUI](GUI)
A folder for the GUI files

[GUI.py](./GUI/GUI.py) -
Where the graphical user interface is managed.

### [people](./people)
A package for all people classes.

[passenger.py](./people/passenger.py) -
A child of the `Person` class, specifically for passengers.

[people.py](./people/people.py) -
Holds the `Person` class. It's the parent for all people classes.

[staff.py](./people/staff.py) -
A child of the `Person` class, specifically for staff members.

### [templates](templates)
Holds the template html files for use with [!!put the use here!!].

[base.html](./templates/base.html) -
This works as the 'parent class' for the other html files.

[flight.html](./templates/flight.html) -
The template for desplaying flights.

[login.html](./templates/login.html) -
The template login form.  

[passengers.html](./templates/passengers.html) -
text here