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
                lease_start = line[2]
                lease_end = line[3]
                licenseplate = line[4]
                lease_dictionary[ssn] = (renter,lease_start,lease_end,licenseplate)
            return lease_dictionary