import csv

def addCostumer(ssn,name,birthdate):
    newCostumer=[ssn,name,birthdate]
    with open('data/costumers.csv', 'a',newline="") as openfile:
        csv_writer = csv.writer(openfile)
        csv_writer.writerow(newCostumer) 