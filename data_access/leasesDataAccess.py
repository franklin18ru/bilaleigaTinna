import csv
import os
from datetime import date, timedelta, datetime


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
                state = line[5]
                lease_dictionary[ssn] = (renter,leaseStart,leaseEnd,licensePlate,state)
            return lease_dictionary

    def deleteLease(self,ssn,leaseStart,licensePlate):
        # moving the data to a temp file but if any line matches the given input it
        # does not go to the temp file
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="\n") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if ssn == line[0] and leaseStart == line[2] and licensePlate == line[4]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")

    def addLease(self,ssn,renter,leasestart,leaseend,licensePlate):
        todaytemp = str(date.today())
        today = todaytemp.replace("-",".")
        if leasestart == today:
            active = "active"
        else:
            active = "inactive"
        with open('data/leases.csv', 'a') as openfile:
            openfile.write("\n"+ssn+","+renter+","+leasestart+","+leaseend+","+licensePlate)
            
    
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
                        if self.checkIfCarIsAvailable(new_start,new_end,licensePlate):
                            # throw error
                            return False
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

    def editState(self):
        today = datetime.date.today()
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if today == line[2]:
                        new_line = [line[0],line[1],line[2],line[3],line[4],"active"]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)
            
    

    def checkIfCarIsAvailable(self,leaseStart,leaseEnd,licensePlate):
        with open("data/leases.csv","r")as checkfile:
            csv_checker = csv.reader(checkfile)
            frame = self.getTimeFrame(leaseStart,leaseEnd)
            for line in csv_checker:
                if line[4] == licensePlate:
                    for day in frame:
                        if line[2] == day or line[3] == day:
                            return False
            return True
    
    # gets all dates between to dates including start and end, you can also skip end #
    def getTimeFrame(self,time1,time2):
        start = date(time1)
        end = date(time2)
        delta = start-end
        frame = []
        for x in range(delta.days+1):
            day = str(start+timedelta(x))
            frame.append(day)
        return frame



    
    