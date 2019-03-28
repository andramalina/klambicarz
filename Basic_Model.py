import mysql.connector
class Basic_Model:
    def __init__(self):
        db = mysql.connector.connect(host="localhost",  # your host, usually localhost
                                     user="root",  # your username
                                     passwd="Andra1998!",  # your password
                                     db="bd1")  # name of the data base
        cursor = db.cursor()