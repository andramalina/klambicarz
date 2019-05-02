from Model.Basic_Model import Basic_Model
from Model.Programare import *


class Programare_Model(Basic_Model):
    def __init__(self):
        Basic_Model.__init__(self)

    def viewAllProgramari(self):
        # comanda care va fi apelata in baza de date
        sql_select = "select * from programare"
        # aici se executa comanda
        self.cursor.execute(sql_select)
        # de aici va lua fiecare rand din interogare si il va printa
        records = self.cursor.fetchall()

        for row in records:
            print(row)

    def insertProgramare(self, programare):
        id_programare = programare.get_id_programare()
        id_parcare = programare.get_id_parcare()
        nr_inmatriculare = programare.get_nr_inmatriculare()
        data_programare = programare.get_data_programare()
        ora_sosire = programare.get_ora_sosire()
        ora_plecare = programare.get_ora_plecare()
        tip_incarcare = programare.get_tip_incarcare()
        sql_insert = "insert into programare values (%s,%s,%s,%s,%s,%s,%s)"
        val = (id_programare, id_parcare, nr_inmatriculare, data_programare, ora_sosire, ora_plecare, tip_incarcare)
        self.cursor.execute(sql_insert, val)
        self.db.commit()
