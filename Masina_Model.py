import Basic_Model
class Masina_Model(Basic_Model):
    def __init__(self):
        Basic_Model.__init__(self)

    def viewAllMasiniForUser(self, user):
        id = user.get_id_user()
        select = "select * from masina where id_user=%s "
        val = (id)
        self.cursor.execute(select, val)
        self.db.commit()