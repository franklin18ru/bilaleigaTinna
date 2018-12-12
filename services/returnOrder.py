import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess
from data_access import leasesDataAccess

class ReturnOrder:
    def __init(self,licensePlate):
        self.carDataAccess = carsDataAccess.CarsDataAccess()
        self.car = self.getCar(licensePlate)
        self.leaseDataAccess = leasesDataAccess.LeasesDataAccess()
        self.carOrder = self.getCarOrder(licensePlate)
        

    def getCar(self,licensePlate):
        for key,value in self.carDataAccess.cars.items():
            if key == licensePlate:
                self.licensePlate = key
                return [key,value]
                
            
    def getCarOrder(self,licensePlate):
        for key,value in self.leaseDataAccess.leases.items():
            if value[3] == licensePlate and value[4] == "active":
                self.orderStart = value[1]
                self.orderEnd = value[2]
                return [key,value]
                

    def returnCar(self,licensePlate,orderStart,orderEnd):
        self.carDataAccess.returnCar(licensePlate,orderStart,orderEnd)

        
                
