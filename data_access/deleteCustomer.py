import csv

def deleteCustomer(name,ssn):
    with open("data/customers.csv","r+") as openfile:
        for line in openfile:
            print(line)
        
deleteCustomer("bla","bla")