import csv
import os

class CarsDataAccess:
    def __init__(self):
        self.cars = self.getAllCars()

    def getAllCars(self):
        cars_dictionary = dict()
        with open("data/cars.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                licenseplate = line[0]
                typef = line[1]
                brand = line[2]
                model = int(line[3])
                seats = int(line[4])
                cars_dictionary[licenseplate] = (typef,brand,model,seats)
            return cars_dictionary

    def addCar(self,LicensePlate,Type,Brand,Model,Seats):
        newCar=[LicensePlate,Type,Brand,Model,Seats]
        with open('data/cars.csv', 'a',newline="") as openfile:
            csv_writer = csv.writer(openfile)
            csv_writer.writerow(newCar)
    
    
