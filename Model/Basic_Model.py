import mysql.connector


class Basic_Model:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",  # your host, usually localhost
                                          user="root",  # your username
                                          passwd="98765432!",  # your password
                                          db="klambi_db")  # name of the data base
        self.cursor = self.db.cursor()
