import Basic_Model

class User_Model(Basic_Model):

    def viewAllUsers(self):
        sql_select = "select * from user"
        self.__cursor.execute(sql_select)
        records = self.__cursor.fetchall()

        for row in records:
            print(row)