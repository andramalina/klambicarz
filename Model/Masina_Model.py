
from Model.Basic_Model import *
class Masina_Model(Basic_Model):
    def __init__(self):
        Basic_Model.__init__(self)

    def viewAllMasiniForUser(self, user):
        id = user.get_id_user()
        id=5
       # self.cursor=self.db.cursor(prepared=True)
        select = "select * from masina where id_user = %s"
        val = (id,)
        self.cursor.execute(select, id)
        self.db.commit()

    def findMasina(self, nr_inmatriculare):
        sql_select="select * from masina where nr_inmatriculare=%s"
        val=(nr_inmatriculare,)
        self.cursor.execute(sql_select,val)
        records=self.cursor.fetchone()
        return records