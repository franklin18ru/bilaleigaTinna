from data_access import carsDataAccess
class GetCars():
    def __init__(self, leaseStart, leaseEnd):
        self.leaseStart = leaseStart
        self.leaseEnd = leaseEnd
        self.cars1 = carsDataAccess.CarsDataAccess()
        self.availableCars = self.cars1.getAvailableCars(self.leaseStart, self.leaseEnd)

    def getCarsByType(self, carType):
        self.cars = []
        for item in self.availableCars:
            if item in carType:
                self.cars.append(item)
        





# def makeOrderCustomer(customerName, customerSSN, customer, email, phoneNr):
