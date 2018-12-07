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
    
    def deleteCar(self,licenseplate):
        # moving the data to a temp file but if any line matches the given input it
        # does not go to the temp file
        self.deleteCarLeases(licenseplate)
        with open("data/cars.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if licenseplate == line[0]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        with open("data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/cars.csv","w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("data/tempfile.csv")

    def deleteCarLeases(self,licenseplate):
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if licenseplate == line[4]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        with open("data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/leases.csv","w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("data/tempfile.csv")

    

    #def editCar(self):


    #def getAllAvailableCars(self):
