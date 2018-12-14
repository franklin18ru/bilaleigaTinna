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
        for item in self.carDataAccess.cars:
            if item[0] == licensePlate.upper():
                self.licensePlate = item[0]
                return item
                
            
    def getCarOrder(self,licensePlate):
        for item in self.leaseDataAccess.leases:
            if item[4] == licensePlate.upper() and item[5] == "active":
                self.orderStart = item[2]
                self.orderEnd = item[3]
                return [item]
    #lease_list.append([ssn, renter,leaseStart,leaseEnd,licensePlate,state])
                
    #lease_dictionary[ssn] = (renter,leaseStart,leaseEnd,licensePlate,state)
    #cars_dictionary[licenseplate] = (typef,brand,model,seats)
    def returnCar(self):
        self.carDataAccess.returnCar(self.licensePlate,self.orderStart,self.orderEnd)

        
                
