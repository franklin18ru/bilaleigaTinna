import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess
from data_access import leasesDataAccess
from data_access import customerDataAccess

class FinishOrder:
    def __init__(self,carname,start,end):
        self.carDataAccess = carsDataAccess.CarsDataAccess()
        self.customersDataAccess = customerDataAccess.CustomerDataAccess()
        self.leaseDataAccess = leasesDataAccess.LeasesDataAccess()
        self.licensePlate = self.getLicensePlate(carname,start,end)
    def getLicensePlate(self,carname,start,end):
        self.availablecars = self.carDataAccess.getAvailableCars(start,end)
        for key,value in self.availablecars.items():
            if value[1] == carname:
                return key
    def addCostumerToData(self,name,ssn,email,phone):
        self.customersDataAccess.addCustomer(name,ssn,email,phone)

    def addLeaseToData(self,name,ssn,leaseStart,leaseEnd,licensePlate):
        self.leaseDataAccess.addLease(name,ssn,leaseStart,leaseEnd,licensePlate) 

    def checkIfCustomerExists(self,ssn):
        for key,value in self.customersDataAccess.customers.items():
            if key == ssn:
                return True
        return False