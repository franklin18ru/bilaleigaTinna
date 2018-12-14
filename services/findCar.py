import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess

class FindCustomer:
    def __init__(self,input):
        self.carDataAccess = carsDataAccess.CarsDataAccess()
        self.car = self.searchDataForCar(input)
        #if self.car == False:
        #   print out error message
    def searchDataForCar(self,input):
        for key,value in self.carDataAccess.cars.items():
            if input == key:
                return [key,value]
        return False