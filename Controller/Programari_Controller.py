from klambicarz.Model.Programare_Model import Programare_Model
from klambicarz.Validator import Programare_Validator

class Programari_Controller(object):
    def __init__(self):
       self.__programare_model=Programare_Model()
       self.__validator=Programare_Validator

    def deleteProgramariByParcareAndAfterSysdate(self,id_parcare):
        self.__programare_model.deleteProgramariByParcareAndAfterSysdate(id_parcare)

    def addProgramareWithDay(self, id_parcare, nr_inmatriculare,year,month,day,hour,tip_incarcare):
        self.__programare_model.insertProgramare(id_parcare,nr_inmatriculare,year,month,day,hour,tip_incarcare)

    def addProgramareToday(self,parkingId,hour,carNo,fastStyle):
        self.__programare_model.insertProgramareToday(parkingId,hour,carNo,fastStyle)

    def getProfitByDay(self):
        results=self.__programare_model.getProfitByDay()
        return results

    def getProfitByWeek(self):
        results=self.__programare_model.getProfitByWeek()
        return results

    def getProfitByMonth(self):
        results=self.__programare_model.getProfitByMonth()
        return results

    def getReservationsSpecificDate(self,year,month,day,hour):
        results=self.__programare_model.getReservationsSpecificDate(year,month,day,hour)
        return results

    def getReservationsToday(self,hour):
        results=self.__programare_model.getReservationsToday(hour)
        return results