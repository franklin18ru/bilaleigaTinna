import csv

def deleteCustomer(name,ssn):
    with open("data/customers.csv","r+") as openfile:
        csv_reader = csv.reader(openfile)
        next(csv_reader)
        for line in csv_reader:
            if name == line[1]:
                pass
        
deleteCustomer("Baldur","bla")