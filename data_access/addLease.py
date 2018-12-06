import csv

def addLease(ssn,renter,leasePeriod,licensePlate):
    newLease=[ssn,renter,leasePeriod,licensePlate]
    with open('data/cars.csv', 'a',newline="") as openfile:
        csv_writer = csv.writer(openfile)
        csv_writer.writerow(newLease) 