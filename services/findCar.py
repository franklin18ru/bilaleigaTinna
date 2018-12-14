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

        #car_list.append([licenseplate,typef,brand,model,seats])