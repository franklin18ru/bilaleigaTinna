import csv

class GetAllCars:
    def __init__(self):
        self.cars = self.getCars()
    def getCars(self):
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
        
