from aircraft import Aircraft


class Plane(Aircraft):
    def __init__(self, oid):
        super().__init__(oid)
        self.plane_model = "Plane model placeholder value"
