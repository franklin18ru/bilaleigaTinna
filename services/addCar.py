import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess

class AddCar:
    def __init__(self,licensePlate,Type,Brand,Model,Seats):
        self.carDataAccess = carsDataAccess.CarsDataAccess()
        self.carDataAccess.addCar(licensePlate,Type,Brand,Model,Seats)