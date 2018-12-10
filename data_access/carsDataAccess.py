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

    

    def editCar(self,olddatalist,newdatalist):
        # take in all arguments if the argument is the same as in the data itself then  #
        # keep it as is, you need to create a temporary file in order to edit and rewrite #
        # the original file to edit #
        # if license plate is edited then all the lease under that license plate must be edited #
        old_licensePlate = olddatalist[0]
        old_type = olddatalist[1]
        old_brand = olddatalist[2]
        old_model = olddatalist[3]
        old_seats = olddatalist[4]
        old_availability = olddatalist[5]
        new_licensePlate = newdatalist[0]
        new_type = newdatalist[1]
        new_brand = newdatalist[2]
        new_model = newdatalist[3]
        new_seats = newdatalist[4]
        new_availability = newdatalist[5]
        with open("data/cars.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if old_licensePlate == line[0] and old_type == line[1] and old_brand == line[2] and old_model == line[3] and old_seats == line[4] and old_availability == line[5]:
                        new_line = [new_licensePlate,new_type,new_brand,new_model,new_seats,new_availability]
                        csv_writer.writerow(new_line)
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

        if old_licensePlate == new_licensePlate:
            pass
        else:
            self.editCarLeases(old_licensePlate,new_licensePlate)


    def editCarLeases(self,old_licensePlate,new_licensePlate):
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if old_licensePlate == line[4]:
                        new_line = [line[0],line[1],line[2],line[3],new_licensePlate]
                        csv_writer.writerow(new_line)
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




























    #def checkIfCarIsAvailable(self,leaseStart,leaseEnd,licensePlate):
    #def getTypeCars(self,Type):
        # Get all available type cars #
        # Put all types in dict, license plate is the key, then check if the car is Available
    #def getAllAvailableCars(self,):
        # Pending further inspection #

    #def returnCar(self):





    # from timedate import date, timedelta
    # start
    # end
    # timedelta = start-end
    # for x in range(delta.days+1):
    # start+timedelta(x)
