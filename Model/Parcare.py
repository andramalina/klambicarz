class Parcare:
    def __init__(self, id_parcare, locatie, status, capacitate):
        self.id_parcare=id_parcare
        self.locatie=locatie
        self.status=status
        self.capacitate=capacitate
    def set_id_parcare(self, id_parcare):
        self.id_parcare=id_parcare
    def get_id_parcare(self):
        return self.id_parcare
    def set_locatie(self, locatie):
        self.locatie=locatie
    def get_locatie(self):
        return self.locatie
    def set_status(self, status):
        self.status=status
    def get_status(self):
        return self.status
    def set_capacitate(self, capacitate):
        self.capacitate=capacitate
    def get_capacitate(self):
        return self.capacitate