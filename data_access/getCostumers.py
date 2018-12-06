import csv

class GetCostumers:
    def __init__(self):
        self.costumers = self.getCostumers()

    def getCostumers(self):
        costumer_dictionary = dict()
        with open("data/costumers.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                string = line[0]
                ssn = int(string.replace("-",""))
                name = line[1]
                birthdate = line[2]
                costumer_dictionary[ssn] = (name,birthdate)
            return costumer_dictionary

