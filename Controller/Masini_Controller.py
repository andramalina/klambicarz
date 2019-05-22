from Model.Masina_Model import Masina_Model
from Validator import Masina_Validator
class Masini_Controller(object):
    def __init__(self):
        self.__masina_model=Masina_Model()
        self.__validator=Masina_Validator

    def findMasina(self,nr_inmatriculare):
        results=self.__masina_model.findMasina(nr_inmatriculare)
        if(results==None):
            return False
        else:
            return True