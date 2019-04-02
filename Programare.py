import datetime


class Programare():
    def __init__(self, id_programare, id_parcare, nr_inmatriculare, data_programare, ora_sosire, ora_plecare,
                 tip_incarcare):
        self.id_programare= id_programare
        self.id_parcare=id_parcare
        self.nr_inmatriculare = nr_inmatriculare
        self.data_programare= data_programare
        self.ora_sosire = ora_sosire
        self.ora_plecare = ora_plecare
        self.tip_incarcare = tip_incarcare

    def set_id_programare(self, idProgramare):
        self.id_programare = idProgramare

    def set_id_parcare(self, idParcare):
        self.id_parcare = idParcare

    def set_nr_inmatriculare(self, nrInm):
        self.nr_inmatriculare = nrInm

    def set_data_programare(self, dataProgramare):
        self.data_programare = dataProgramare

    def set_ora_sosire(self, oraSosire):
        self.ora_sosire = oraSosire

    def set_ora_plecare(self, oraPlecare):
        self.ora_plecare = oraPlecare

    def set_tip_programare(self, tipProgramare):
        self.tip_incarcare = tipProgramare

    def get_id_programare(self):
        return self.id_programare

    def get_id_parcare(self):
        return self.id_parcare

    def get_data_programare(self):
        return self.data_programare

    def get_nr_inmatriculare(self):
        return self.nr_inmatriculare

    def get_ora_sosire(self):
        return self.ora_sosire

    def get_ora_plecare(self):
        return self.ora_plecare

    def get_tip_incarcare(self):
        return self.tip_incarcare
