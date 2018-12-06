import csv

def addCar(LicensePlate,Type,Brand,Model,Seats):
    newCar=[LicensePlate,Type,Brand,Model,Seats]
    with open('data/cars.csv', 'a',newline="") as openfile:
        csv_writer = csv.writer(openfile)
        csv_writer.writerow(newCar) 

