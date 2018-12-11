import csv
import os


class LeasesDataAccess:
    def __init__(self):
        self.leases = self.getAllLeases()
    def getAllLeases(self):
        lease_dictionary = dict()
        with open("data/leases.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                string = line[0]
                ssn = int(string.replace("-",""))
                renter = line[1]
                leaseStart = line[2]
                leaseEnd = line[3]
                licensePlate = line[4]
                lease_dictionary[ssn] = (renter,leaseStart,leaseEnd,licensePlate)
            return lease_dictionary

    def deleteLease(self,ssn,leaseStart,licensePlate):
        # moving the data to a temp file but if any line matches the given input it
        # does not go to the temp file
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if ssn == line[0] and leaseStart == line[2] and licensePlate == line[4]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")

    def addLease(self,ssn,renter,leasestart,leaseend,licensePlate):
        newLease=[ssn,renter,leasestart,leaseend,licensePlate]
        with open('data/cars.csv', 'a',newline="") as openfile:
                csv_writer = csv.writer(openfile)
                csv_writer.writerow(newLease) 
    
    def editLease(self,old_start,old_end,new_start,new_end,name,ssn,licensePlate):
        # take in all arguments if the argument is the same as in the data itself then  #
        # keep it as is, you need to create a temporary file in order to edit and rewrite #
        # the original file to edit #
        # Can't edit customer or car only edit lease period #
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if ssn == line[0] and name == line[1] and licensePlate == line[4] and old_start == line[2] and old_end == line[3]:
                        new_line = [line[0],line[1],new_start,new_end,line[4]]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")
    

    def moveFromTempFile(self,fileName):
        # the data back to the original file
        filetowrite = "data/"+fileName+".csv"
        with open("data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open(filetowrite,"w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

            # removing the temp file
            os.remove("data/tempfile.csv")