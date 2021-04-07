from aircraft import Aircraft
from db_wrapper import DbWrapper


class Plane(Aircraft):
    def __init__(self):
        super().__init__()
        self.plane_model = "Plane model placeholder value"

    def save_and_regenerate_with_id(self, db_wrapper):
        super().save_and_regenerate_with_id(db_wrapper)
        p = Plane().make_from_db(self.get_max_id(db_wrapper), self.flight, self.flight_capacity, "plane")
        return p
