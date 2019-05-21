from Model.Basic_Model import Basic_Model
from Model.Parcare import *
class Parcare_Model(Basic_Model):

    def __init__(self):
        Basic_Model.__init__(self)

    def getAllParcari(self):
        sql_select = "select * from parcare"   #comanda care va fi apelata in baza de date
        self.cursor.execute(sql_select)     #aici se executa comanda
        records = self.cursor.fetchall()    #de aici va lua fiecare rand din interogare si il va printa

        return records


    def getAllParcariIdLocatie(self):
        sql_select="select id_parcare,locatie,status from parcare"
        self.cursor.execute(sql_select)
        records=self.cursor.fetchall()
        return records

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

    def findParcare(self, id_parcare):
        sql_select="select * from parcare where id_parcare=%s"
        val=(id_parcare,)
        self.cursor.execute(sql_select,val)
        records=self.cursor.fetchone()
        return records

    def getParcariWithCapacitiesAndOccupied(self):
        #sql_select="select pro.id_parcare, par.locatie, par.capacitate, count(*), capacitate-count(*) from  programare pro inner join parcare par on(par.id_parcare=pro.id_parcare) where pro.data_programare=date(sysdate()) group by pro.id_parcare"
        sql_select="select pro.id_parcare, par.locatie, capacitate-count(*) from  programare pro inner join parcare par on(par.id_parcare=pro.id_parcare) where pro.data_programare=date(sysdate()) group by pro.id_parcare"
        self.cursor.execute(sql_select)
        records=self.cursor.fetchall()
        print(records)
        return records

    def getParcariAvailableLotsOnSpecificDate(self,year,month,day,hour):
        sql_select="select par.id_parcare, par.locatie,par.capacitate-count(*) from programare pro right outer join parcare par ON par.id_parcare=pro.id_parcare and pro.data_programare=DATE(CONCAT_WS('-', %s, %s, %s)) and pro.ora_sosire=time(concat_ws(':',%s,00,00)) and par.status=1 group by par.id_parcare"
        val=(year,month,day,hour)
        print("VAL:::")
        print(val)
        self.cursor.execute(sql_select,val)
        records=self.cursor.fetchall()
        print(records)
        return records

    def getParcariAvailableLotsToday(self,hour):
        sql_select = "select par.id_parcare, par.locatie,par.capacitate-count(*) from programare pro right outer join parcare par ON par.id_parcare=pro.id_parcare and pro.data_programare=DATE(sysdate()) and pro.ora_sosire=time(concat_ws(':',%s,00,00)) and par.status=1 group by par.id_parcare"
        val = (hour,)
        print("VAL:::")
        print(val)
        self.cursor.execute(sql_select, val)
        records = self.cursor.fetchall()
        print(records)
        return records

    def getTotalCapacityBookedAvailable(self):
        sql_select1="select count(*) from  programare pro inner join parcare par on(par.id_parcare=pro.id_parcare) where pro.data_programare=date(sysdate())"
        self.cursor.execute(sql_select1)
        records1 = self.cursor.fetchone()
        sql_select2="select sum(capacitate) from parcare"
        self.cursor.execute(sql_select2)
        records2 = self.cursor.fetchone()
        capacitate=records2[0]
        booked=records1[0]
        available=records2[0]-records1[0]
        results=(capacitate,available,booked)
        print(results)
        return results

    def getTotalCapacityBookedAvailableForSpecificDate(self,year, month, day, hour):
        sql_select1 = "select count(*) from  programare pro inner join parcare par on(par.id_parcare=pro.id_parcare) where pro.data_programare=date(concat_ws('-',%s,%s,%s)) and pro.ora_sosire=time(concat_ws(':',%s,00,00))"
        val=(year,month,day,hour)
        self.cursor.execute(sql_select1,val)
        records1 = self.cursor.fetchone()
        sql_select2 = "select sum(capacitate) from parcare"
        self.cursor.execute(sql_select2)
        records2 = self.cursor.fetchone()
        capacitate = records2[0]
        booked = records1[0]
        available = records2[0] - records1[0]
        results = (capacitate, available, booked)
        print(results)
        return results

    def getTotalCapacityBookedAvailableForToday(self, hour):
        sql_select1 = "select count(*) from  programare pro inner join parcare par on(par.id_parcare=pro.id_parcare) where pro.data_programare=date(sysdate()) and pro.ora_sosire=time(concat_ws(':',%s,00,00))"
        val = (hour,)
        self.cursor.execute(sql_select1, val)
        records1 = self.cursor.fetchone()
        sql_select2 = "select sum(capacitate) from parcare"
        self.cursor.execute(sql_select2)
        records2 = self.cursor.fetchone()
        capacitate = records2[0]
        booked = records1[0]
        available = records2[0] - records1[0]
        results = (capacitate, available, booked)
        print(results)
        return results
