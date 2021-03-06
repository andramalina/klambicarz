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

    def insertProgramare(self, id_parcare, nr_inmatriculare,year,month,day,hour,tip_incarcare):
        self.db.commit()
        print("TIP")
        print(tip_incarcare)

        week=0
        while(week<70):
            sql_select = "select max(id_programare) from programare"
            self.cursor.execute(sql_select)
            result = self.cursor.fetchone()
            id_programare = result[0] + 1
            sql_insert="insert into programare values(%s,%s,%s,date_add(date(concat_ws('-',%s,%s,%s)),interval %s day),time(concat_ws(':',%s,00,00)),time(concat_ws(':',%s,00,00)),%s)"
            if(tip_incarcare=="fast"):
                leaveHour=int(hour)+1
            else:
                leaveHour=int(hour)+2
            val = (id_programare, id_parcare, nr_inmatriculare, year,month,day,week,hour, leaveHour, tip_incarcare)
            self.cursor.execute(sql_insert, val)
            self.db.commit()
            week=week+7

    def insertProgramareToday(self, id_parcare,hour,nr_inmatriculare,tip_incarcare):
        self.db.commit()
        week=0
        while(week<70):
            sql_select = "select max(id_programare) from programare"
            self.cursor.execute(sql_select)
            result = self.cursor.fetchone()
            id_programare = result[0] + 1

            sql_insert = "insert into programare values(%s,%s,%s,date_add(date(sysdate()),interval %s day),time(concat_ws(':',%s,00,00)),time(concat_ws(':',%s,00,00)),%s)"
            if (tip_incarcare == "fast"):
                leaveHour = int(hour) + 1
            else:
                leaveHour = int(hour) + 2
            val = (id_programare, id_parcare, nr_inmatriculare, week, hour, leaveHour, tip_incarcare)
            self.cursor.execute(sql_insert, val)
            self.db.commit()
            week=week+7

    def deleteProgramariByParcareAndAfterSysdate(self, id_parcare):
        self.db.commit()
        sql_delete="delete from programare where id_parcare=%s and data_programare>=date(sysdate())"
        val=(id_parcare,)
        self.cursor.execute(sql_delete,val)
        self.db.commit()

    def getProfitByDay(self):
        self.db.commit()
        sql_select="select pro.data_programare,120*(count(case when pro.tip_incarcare='normal' then 1 end)) as normal1, 240*(count(case when pro.tip_incarcare='fast' then 1 end)) as fast1, 120*(count(case when pro.tip_incarcare='normal' then 1 end)) + 240*(count(case when pro.tip_incarcare='fast' then 1 end)) as total from programare pro group by pro.data_programare"
        self.cursor.execute(sql_select)
        records = self.cursor.fetchall()
        return records

    def getProfitByWeek(self):
        self.db.commit()
        sql_select = "select year(pro.data_programare), week(pro.data_programare),120*(count(case when pro.tip_incarcare='normal' then 1 end)) as normal1, 240*(count(case when pro.tip_incarcare='fast' then 1 end)) as fast1, 120*(count(case when pro.tip_incarcare='normal' then 1 end)) + 240*(count(case when pro.tip_incarcare='fast' then 1 end)) as total from programare pro group by year(week(pro.data_programare)), week(pro.data_programare)"
        self.cursor.execute(sql_select)
        records = self.cursor.fetchall()
        return records

    def getProfitByMonth(self):
        self.db.commit()
        sql_select = "select year(pro.data_programare),month(pro.data_programare),120*(count(case when pro.tip_incarcare='normal' then 1 end)) as normal1, 240*(count(case when pro.tip_incarcare='fast' then 1 end)) as fast1, 120*(count(case when pro.tip_incarcare='normal' then 1 end)) + 240*(count(case when pro.tip_incarcare='fast' then 1 end)) as total from programare pro group by month(pro.data_programare),year(pro.data_programare)"
        self.cursor.execute(sql_select)
        records = self.cursor.fetchall()
        return records

    def getReservationsSpecificDate(self,year,month,day,hour):
        self.db.commit()
        sql_select="select pro.id_programare, m.nr_inmatriculare, par.id_parcare from programare pro inner join masina m inner join parcare par on pro.nr_inmatriculare = m.nr_inmatriculare and pro.id_parcare = par.id_parcare where pro.data_programare = date(concat_ws('-',%s,%s,%s)) and pro.ora_sosire = time(concat_ws(':',%s,00,00))"
        val=(year,month,day,hour)
        self.cursor.execute(sql_select,val)
        records=self.cursor.fetchall()
        print(records)
        return records

    def getReservationsToday(self,hour):
        self.db.commit()
        sql_select="select pro.id_programare, m.nr_inmatriculare, par.id_parcare from programare pro inner join masina m inner join parcare par on pro.nr_inmatriculare = m.nr_inmatriculare and pro.id_parcare = par.id_parcare where pro.data_programare = date(sysdate()) and pro.ora_sosire = time(concat_ws(':',%s,00,00))"
        val=(hour,)
        self.cursor.execute(sql_select,val)
        records=self.cursor.fetchall()
        print(records)
        return records

