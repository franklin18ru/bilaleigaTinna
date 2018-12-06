import csv

class GetLeases:
    def __init__(self):
        self.leases = self.getLeases()
    def getLeases(self):
        lease_dictionary = dict()
        with open("data/leases.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                string = line[0]
                ssn = int(string.replace("-",""))
                renter = line[1]
                lease_period = line[2]
                licenseplate = line[3]
                lease_dictionary[ssn] = (renter,lease_period,licenseplate)
            return lease_dictionary