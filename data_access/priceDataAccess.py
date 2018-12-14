import csv
import os

class PriceDataAccess:
    def __init__(self):
        self.pricelist = self.getPriceList()

    def getPriceList(self):
        pricelist_list = []
        with open("data/pricelist.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                carType = line[0]
                price = line[1]
                pricelist_list.append([carType,price])
        return pricelist_list
        
    def editPriceList(self,olddatalist,newdatalist):
        #olddata : [[Type,Price]]
        #newdata : [[Type,Price]]
        with open("data/pricelist.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w")as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    for item in olddatalist:
                        if line == item:
                            for new in newdatalist:
                                if new == line:
                                    csv_writer.writerow(line)
                                if item[0] == new[0]:
                                    new_line=[new]
                                    csv_writer.writerow(new_line)
                self.moveFromTempFile("pricelist")

    def checkIfUserHasAuthority(self,username):
        with open("data/users.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                if line[2] == username:
                    if line[1] == "boss":
                        return True
                    else:
                        return False


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
