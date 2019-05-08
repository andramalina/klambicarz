from klambicarz.Model.Parcare_Model import Parcare_Model
from klambicarz.Validator import Parcare_Validator
class Parcari_Controller(object):
    def __init__(self):
        self.__parcare_model=Parcare_Model()
        self.__validator=Parcare_Validator

    def updateStatus(self, new_status,id_parcare):
        print("ajunsaaam")
        self.__parcare_model.updateStatus(new_status,id_parcare)

    def findParcare(self,id_parcare):
        results=self.__parcare_model.findParcare(id_parcare)
        if(results==None):
            return False
        else:
            return True

    def getParcariWithCapacitiesAndOccupied(self):
        results=self.__parcare_model.getParcariWithCapacitiesAndOccupied()
        return results

    def getTotalCapacityBookedAvailable(self):
        results=self.__parcare_model.getTotalCapacityBookedAvailable()
        return results

    def getAllParcariIdLocatie(self):
        results=self.__parcare_model.getAllParcariIdLocatie()
        return results

    def getParcariAvailableLotsOnSpecificDate(self, year, month, day, hour):
        results=self.__parcare_model.getParcariAvailableLotsOnSpecificDate(year,month,day,hour)
        return results

    def getParcariAvailableLotsToday(self, hour):
        results=self.__parcare_model.getParcariAvailableLotsToday(hour)
        return results

    def getTotalCapacityBookedAvailableForSpecificDate(self,year, month, day, hour):
        results=self.__parcare_model.getTotalCapacityBookedAvailableForSpecificDate(year,month,day,hour)
        return results

    def getTotalCapacityBookedAvailableForToday(self, hour):
        results=self.__parcare_model.getTotalCapacityBookedAvailableForToday(hour)
        return results