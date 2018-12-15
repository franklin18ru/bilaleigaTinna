import csv
import os
from datetime import date, timedelta
# Data access that has anything to do with cars #
class CarsDataAccess:
    def __init__(self):
        self.cars = self.getAllCars()
    # get all cars in the system in store them in a dictionary #
    def getAllCars(self):
        car_list = []
        with open("../data/cars.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                licenseplate = line[0]
                typef = line[1]
                brand = line[2]
                model = int(line[3])
                seats = int(line[4])
                car_list.append([licenseplate,typef,brand,model,seats])
            return car_list

    # add a new car to the system #
    def addCar(self,LicensePlate,Type,Brand,Model,Seats):
        with open('../data/cars.csv', 'a',newline="") as openfile:
            openfile.write("\n"+LicensePlate+","+Type+","+Brand+","+Model+","+Seats)

    # delete the car with the given input #
    def deleteCar(self,licenseplate):
        # moving the data to a temp file but if any line matches the given input it
        # does not go to the temp file
        self.deleteCarLeases(licenseplate)
        with open("../data/cars.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("../data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if licenseplate == line[0]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("cars")
        # delete all leases under that license plate #
        self.deleteCarLeases(licenseplate)
        
    # delete all leases under a specific car #
    def deleteCarLeases(self,licenseplate):
        with open("../data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("../data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if licenseplate == line[4]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")

    
    # edits the car in cars file from the given inputs#
    def editCar(self,olddatalist,newdatalist):
        old_licensePlate = olddatalist[0]
        new_licensePlate = newdatalist[0]
        Type = olddatalist[1]
        new_brand = newdatalist[1]
        new_model = newdatalist[2]
        new_seats = newdatalist[3]
        with open("../data/cars.csv","r+",newline="") as openfile:
            csv_reader = csv.reader(openfile)
            with open("../data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if old_licensePlate == line[0]:
                        new_line = [new_licensePlate,Type,new_brand,new_model,new_seats]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("cars")

        # if the license plate is not changed then system does nothing #
        # if the license plate is changed the we need to update the leases #
        # under that license plate #

        if old_licensePlate == new_licensePlate:
            pass
        else:
            self.editCarLeases(old_licensePlate,new_licensePlate)

    # Goes through the lease file and checks if the old license plate is there and #
    # updates the leases under that license plate #
    def editCarLeases(self,old_licensePlate,new_licensePlate):
        with open("../data/leases.csv","r+",newline="") as openfile:
            csv_reader = csv.reader(openfile)
            with open("../data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if old_licensePlate == line[4]:
                        new_line = [line[0],line[1],line[2],line[3],new_licensePlate,line[5]]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")
        

    # Function to move the contents of a tempfile to another file and #
    # then destroy the temp file #
    def moveFromTempFile(self,fileName):
        # the data back to the original file
        filetowrite = "../data/"+fileName+".csv"
        with open("../data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open(filetowrite,"w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("../data/tempfile.csv")












    # takes in a lease period and checks if any other lease period with the same license plate is active #
    # returns false if the car is not available and returns true if the car is available#
    def checkIfCarIsAvailable(self,leaseStart,leaseEnd,licensePlate):
        with open("data/leases.csv","r")as checkfile:
            csv_checker = csv.reader(checkfile)
            frame = self.getTimeFrame(leaseStart,leaseEnd)
            for line in csv_checker:
                if line[4] == licensePlate:
                    for day in frame:
                        if line[2] == day or line[3] == day:
                            return False
            return True

    def getCarsType(self,Type,leaseStart,leaseEnd):
        # Get all available type cars #
        
        # Put all types in dict, license plate is the key, then check if the car is Available
        cars_dictionary = dict()
        with open("data/cars.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                if line[1] == Type:
                     if self.checkIfCarIsAvailable(leaseStart,leaseEnd,line[0]):
                        cars_dictionary[line[0]] = (line[2],line[3],line[4])
            return cars_dictionary

    def getAvailableCars(self,leaseStart,leaseEnd):
        # Get all available type cars  in the system #
        
        # Put all type cars that was chosen in dict, license plate is the key, then check if the car is Available #
        cars_dictionary = dict()
        with open("data/cars.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                if self.checkIfCarIsAvailable(leaseStart,leaseEnd,line[0]):
                    cars_dictionary[line[0]] = (line[1],line[2],line[3],line[4])
            return cars_dictionary


            
    # find the car that the customer is returning and return him in the system by #
    # making the lease activity completed #
    def returnCar(self,licensePlate,leaseStart,leaseEnd):
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if licensePlate == line[4] and leaseStart == line[2] and leaseEnd == line[3]:
                        new_line = [line[0],line[1],line[2],line[3],line[4],"completed"]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")




    # gets all dates between to dates including start and end, you can also skip end #
    def getTimeFrame(self,time1,time2):
        t1 = time1.split(".")
        t2 = time2.split(".")
        start = date(int(t1[0]),int(t1[1]),int(t1[2]))
        end = date(int(t2[0]),int(t2[1]),int(t2[2]))
        delta = end-start
        frame = []
        for x in range(delta.days+1):
            day = str(start+timedelta(x))
            editday = day.replace("-",".")
            frame.append(editday)
        return frame

