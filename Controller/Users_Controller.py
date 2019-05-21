
from Model.User_Model import User_Model
from Model.User import User
from Validator import User_Validator
class Users_Controller(object):
    def __init__(self):
        '''
        Constructor
        Ii dam un User_Model (Care de fapt e ca un repository, e legatura cu BD, cu cămara in care tot bagam borcane)
        si un validator, ca ori de cate ori bagam un user, sa il validam inainte
        '''

        self.__user_model=User_Model()
        self.__validator=User_Validator

    def save(self, id_user, username, nume, nr_telefon, tip, password):
        '''
        Primeste chestiile care definesc un user
        Valideaza chestiile
        Le baga in BD prin Model
        '''
        user = User(id_user, username, nume, nr_telefon, tip, password)
        self.__validator.validate(user)
        self.__user_model.insertUser(user)

    def verify_user(self,username,password):
        results=self.__user_model.verify_user(username,password)

        if (results==None):
            return 'error'
        else:
            return results[0]