from Controller.Users_Controller import Users_Controller
from Model.Basic_Model import Model_Exception

class Ui(object):
    def __init__(self,users_controller):
        self.__users_controller=users_controller

    def mainMenu(self):
        return """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            0. Iesire
            1. Adauga user
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """

    def getNumber(self, msj):
        self.output(msj)
        while True:
            try:
                x = int(input())
                break
            except ValueError:
                self.output("Introduceti un numar.")
        return x

    def ui_save_user(self):
        id_user = self.getNumber("Introduceti nr. utilizatorului:")
        username = input("Introduceti username:")
        nume = input("Introduceti nume:")
        nr_tel = input("Introduceti nr. tel:")
        tip = input("Introduceti tipul (client sau admin):")
        password=input("Introduceti parola:")
        self.__users_controller.save(id_user, username, nume, nr_tel, tip, password)

    def getNumberBtw(self, l, r):
        x = self.getNumber("Introduceti un numar intre " + str(l) + " si " + str(r) + ".")
        while (x < l or x > r):
            self.output("Numarul nu e bun.")
            x = self.getNumber("Introduceti un numar intre " + str(l) + " si " + str(r) + ".")
        return x

    def output(self, msj):
        print(msj)

    def run(self):

        commands = {1: self.ui_save_user}
        while True:
            self.output(self.mainMenu())
            x = self.getNumberBtw(0, len(commands))
            if (x == 0):
                return
            else:
                try:
                    commands[x]()
                except ValueError as msg:
                    self.output(msg)
                except Model_Exception as msg:
                    self.output(msg)