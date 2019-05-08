from Model.Basic_Model import Basic_Model
from Model.User import *
class User_Model(Basic_Model):
    #constructor User_Model ce mosteneste clasa Basic_Model unde facem conexiunea la baza de date
    def __init__(self):
        Basic_Model.__init__(self)

    def viewAllUsers(self):
        sql_select = "select * from user"   #comanda care va fi apelata in baza de date
        self.cursor.execute(sql_select)     #aici se executa comanda
        records = self.cursor.fetchall()    #de aici va lua fiecare rand din interogare si il va printa

        for row in records:
            print(row)


    def insertUser(self, user):
        id_user=user.get_id_user()         #luam fiecare atribut al userului folosing getteri
        nume=user.get_nume()
        password=user.get_password()
        tip=user.get_tip()
        nr_telefon=user.get_nr_telefon()
        username=user.get_username()
        sql_insert = "insert into user values (%s,%s,%s,%s,%s,%s)"      #din nou comanda pentru baza de date
        val=(id_user,username,nume,nr_telefon,tip,password)             #vectorul de valori ce vor fi parametri pentru
        self.cursor.execute(sql_insert,val)                             #valorile de mai sus (fiecare %s e de fapt un
        self.db.commit()                                                #obiect din val)
        print("am insertat")

    def verify_user(self,username,password):
        print("yuhuu",username,password)
        sql_select="select tip from user where username=%s and password=%s"
        val=(username,password)
        self.cursor.execute(sql_select,val)
        records=self.cursor.fetchone()
        return records