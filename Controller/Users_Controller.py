
from Model.User_Model import User_Model
from Model.User import User

class Users_Controller(object):
    def __init__(self,user_model,validator):
        '''
        Constructor
        Ii dam un User_Model (Care de fapt e ca un repository, e legatura cu BD, cu cămara in care tot bagam borcane)
        si un validator, ca ori de cate ori bagam un user, sa il validam inainte
        '''

        self.__user_model=user_model
        self.__validator=validator

    def save(self,id_user, username, nume, nr_telefon, tip, password):
        '''
        Primeste chestiile care definesc un user
        Valideaza chestiile
        Le baga in BD prin Model
        '''
        user=User(id_user, username, nume, nr_telefon, tip, password)
        self.__validator.validate(user)
        self.__user_model.insertUser(user)
