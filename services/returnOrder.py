import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess
from data_access import leasesDataAccess

class ReturnOrder:
    def __init__(self,licensePlate):
        self.carDataAccess = carsDataAccess.CarsDataAccess()
        self.car = self.getCar(licensePlate)
        self.leaseDataAccess = leasesDataAccess.LeasesDataAccess()
        self.carOrder = self.getCarOrder(licensePlate)
        #order: [ssn,(renter,leaseStart,leaseEnd,licensePlate,state)]
        #car: [licenseplate,(typef,brand,model,seats)]

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
                
    #lease_dictionary[ssn] = (renter,leaseStart,leaseEnd,licensePlate,state)
    #cars_dictionary[licenseplate] = (typef,brand,model,seats)
    def returnCar(self):
        self.carDataAccess.returnCar(self.licensePlate,self.orderStart,self.orderEnd)

        
                
