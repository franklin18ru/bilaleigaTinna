import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess
class GetCars():
    def __init__(self, leaseStart, leaseEnd):
        self.leaseStart = leaseStart
        self.leaseEnd = leaseEnd
        self.cars1 = carsDataAccess.CarsDataAccess()
        self.availableCars = self.cars1.getAvailableCars(self.leaseStart, self.leaseEnd)

    def getCarsByType(self, carType):
        self.cars = []
        for key, value in self.availableCars.items():
            if value[0] in carType:
                self.cars.append(value[1])
        





# def makeOrderCustomer(customerName, customerSSN, customer, email, phoneNr):
