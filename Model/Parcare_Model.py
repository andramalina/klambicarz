from Model.Basic_Model import Basic_Model
from Model.Parcare import *
class Parcare_Model(Basic_Model):

    def __init__(self):
        Basic_Model.__init__(self)

    def viewAllParcari(self):
        sql_select = "select * from parcare"   #comanda care va fi apelata in baza de date
        self.cursor.execute(sql_select)     #aici se executa comanda
        records = self.cursor.fetchall()    #de aici va lua fiecare rand din interogare si il va printa

        for row in records:
            print(row)


    def insertParcare(self, parcare):
        id_parcare=parcare.get_id_parcare()         #luam fiecare atribut al userului folosing getteri
        locatie=parcare.get_locatie()
        status=parcare.get_status()
        capacitate=parcare.get_capacitate()
        sql_insert = "insert into parcare values (%s,%s,%s,%s)"      #din nou comanda pentru baza de date
        val=(id_parcare,locatie,status,capacitate)             #vectorul de valori ce vor fi parametri pentru
        self.cursor.execute(sql_insert,val)                             #valorile de mai sus (fiecare %s e de fapt un
        self.db.commit()                                                #obiect din val)

    def updateStatus(self,status,id_parcare):
        sql_update="update parcare set status=%s where id_parcare=%s"
        val=(status,id_parcare)
        self.cursor.execute(sql_update,val)
        self.db.commit()