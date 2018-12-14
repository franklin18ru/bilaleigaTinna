import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess

class FindCar:
    def __init__(self,input):
        self.carDataAccess = carsDataAccess.CarsDataAccess()
        self.car = self.searchDataForCar(input)
        #if self.car == False:
        #   print out error message
    def searchDataForCar(self,input):
        for item in self.carDataAccess.cars:
            if input.upper() == item[0]:
                return item
        return False

    def editCar(self,newdatalist):
        oldlicenseplate = self.car[0]
        Type = self.car[1] 
        oldbrand = self.car[2]
        oldmodel = self.car[3]
        oldseats = self.car[4]
        olddata = [oldlicenseplate,Type,oldbrand,oldmodel,oldseats]
        self.carDataAccess.editCar(olddata,newdatalist)
    def deleteCar(self,licenseplate):
        self.carDataAccess.deleteCar(licenseplate)
        #car_list.append([licenseplate,typef,brand,model,seats])



  