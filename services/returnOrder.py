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
        for item in self.leaseDataAccess.leases:
            if item[4] == licensePlate and item[5] == "active":
                self.orderStart = item[2]
                self.orderEnd = item[3]
                return [self.leaseDataAccess.leases]
    #lease_list.append([ssn, renter,leaseStart,leaseEnd,licensePlate,state])
                
    #lease_dictionary[ssn] = (renter,leaseStart,leaseEnd,licensePlate,state)
    #cars_dictionary[licenseplate] = (typef,brand,model,seats)
    def returnCar(self):
        self.carDataAccess.returnCar(self.licensePlate,self.orderStart,self.orderEnd)

        
                
