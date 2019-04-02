#!/usr/bin/python
from Model.Programare_Model import *
from Model.User_Model import *
from Model.Programare import *
from Model.User import *
from Validator.User_Validator import User_Validator
from Controller.Users_Controller import Users_Controller
from View.Ui import Ui
#userModel=User_Model()
#userModel.viewAllUsers()
#user=User(11,"alinahu","Alinhha","0741226514","client","alina")
#userModel.insertUser(user)
#programareModel = Programare_Model()
#programareModel.viewAllProgramari()
#programare=Programare(5,2,"CJ 79 MMM","2019-03-29","18:00:00","20:00:00","normal")
#programareModel.insertProgramare(programare)

userModel=User_Model()
usersController=Users_Controller(userModel, User_Validator)
ui=Ui(usersController)
ui.run()
