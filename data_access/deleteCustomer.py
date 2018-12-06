import csv
import os


def deleteCustomer(name,ssn):
    with open("data/customers.csv","r+") as openfile:
        csv_reader = csv.reader(openfile)
        with open("data/tempfile.csv","w",newline="") as tempfile:
            csv_writer2 = csv.writer(tempfile)
            for line in csv_reader:
                if name == line[1] or ssn == line[0]:
                    continue
                csv_writer2.writerow(line)
            openfile.truncate(0)

    #os.remove("data/tempfile.csv")

            
deleteCustomer("Baldur","bla")