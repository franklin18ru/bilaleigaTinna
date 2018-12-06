import csv

class GetCustomers:
    def __init__(self):
        self.customers = self.getCustomers()

    def getCustomers(self):
        customer_dictionary = dict()
        with open("data/customers.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                string = line[0]
                ssn = int(string.replace("-",""))
                name = line[1]
                birthdate = line[2]
                customer_dictionary[ssn] = (name,birthdate)
            return customer_dictionary

