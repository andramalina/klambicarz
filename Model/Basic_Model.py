import mysql.connector


class Basic_Model:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",  # your host, usually localhost
                                          user="root",  # your username
                                          passwd="iuli",  # your password
                                          db="klambi_db")  # name of the data base
        self.cursor = self.db.cursor()


class Model_Exception(Exception):
    pass