import csv
import os

class PriceDataAccess:
    def __init__(self):
        self.pricelist = self.getPriceList()
    def getPriceList(self):
        pricelist_dictionary = dict()
        with open("data/pricelist.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                carType = line[0]
                price = line[1]
                pricelist_dictionary[carType] = price
        return pricelist_dictionary
    #def editPriceList(self,olddatalist,newdatalist):
    #   with open("data/pricelist.csv","r+") as openfile:
    #       csv_reader = csv.reader(openfile)
    #       with open("data/tempfile.csv","w")as tempfile:
    #           for line in csv_reader:
    #               if something is changed
    #                   change
    #               csv.writerow(line)


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
