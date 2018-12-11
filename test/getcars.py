import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import carsDataAccess

cars1 = carsDataAccess.CarsDataAccess()
cars = cars1.getAvailableCars("2018.12.10","2018.12.18")
print (cars)