from Aircraft import Aircraft

class Plane(Aircraft):
    def __init__(self, aircraft_id, flight_capacity):
        super().__init__(aircraft_id, flight_capacity)
        self.plane_model = "Plane model placeholder value"