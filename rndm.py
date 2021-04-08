from db_wrapper import DbWrapper

db_wrapper = DbWrapper()
dict_passengers = db_wrapper.load_all_passengers()
dict_flights = db_wrapper.load_all_flights(dict_passengers)
dict_aircraft = db_wrapper.load_all_aircraft()
dict_staff = db_wrapper.load_all_staff()

for i in dict_passengers.values():
    print(dir(i))