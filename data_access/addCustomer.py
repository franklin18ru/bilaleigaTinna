import csv

def addCustomer(ssn,name,birthdate):
    newCustomer=[ssn,name,birthdate]
    with open('data/customers.csv', 'a',newline="") as openfile:
        csv_writer = csv.writer(openfile)
        csv_writer.writerow(newCustomer) 