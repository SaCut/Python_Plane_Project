from aircraft import Aircraft


class Helicopter(Aircraft):
    def __init__(self):
        super().__init__()

    def save_and_regenerate_with_id(self, db_wrapper):
        super().save_and_regenerate_with_id(db_wrapper)
        h = Helicopter().make_from_db(self.get_max_id(db_wrapper), self.flight, self.flight_capacity, "heli")
        return h
