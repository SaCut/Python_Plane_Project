from People import Person

class Staff(Person):
    def __init__(self, name, tax_no):
        super().__init__()
        self.name = name
        self.tax_no = tax_no