from people.people import Person


class Staff(Person):
    def __init__(self):
        super().__init__(None, "staff")

    def make_from_db(self, oid, first_name, last_name, tickets):
        super().init_person_data(oid, first_name, last_name, tickets)
        return self

    def __save_and_regenerate_with_id(self, db_wrapper):
        first_name = self.first_name
        last_name = self.last_name
        ticket_number = self.ticket_number

        db_wrapper.cursor.execute(
            f"INSERT INTO {self.table} "
            + f"VALUES ('{first_name}', '{last_name}', '{ticket_number}');")

        db_wrapper.connection.commit()

        # Update the dictionary so that this is always correct
        staff = Staff().make_from_db(self.get_max_id(db_wrapper), first_name, last_name, ticket_number)

        return staff

    def make_manual(self, first_name, last_name, tax_no, db_wrapper):
        # make a place holder passenger
        self.make_from_db(None, first_name, last_name, tax_no,)

        # save it and regenerate it
        return self.__save_and_regenerate_with_id(db_wrapper)
