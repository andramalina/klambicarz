class Masina:
    def __init__(self, nr_inmatriculare, id_user):
        self.nr_inmatriculare = nr_inmatriculare
        self.id_user = id_user

    #getter method
    def get_nr_inmatriculare(self):
        return self.nr_inmatriculare

    def get_id_user(self):
        return self.id_user


    #setter method

    def set_nr_inmatriculare(self, nr_inmatriculare):
        self.nr_inmatriculare = nr_inmatriculare

    def set_id_user(self, id_user):
        self.id_user = id_user
