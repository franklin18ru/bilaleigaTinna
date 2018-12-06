import csv
import os


def deleteCustomer(name,ssn):
    # moving the data to a temp file but if any line matches the given input it
    # does not go to the temp file
    with open("data/customers.csv","r+") as openfile:
        csv_reader = csv.reader(openfile)
        with open("data/tempfile.csv","w",newline="") as tempfile:
            csv_writer = csv.writer(tempfile)
            for line in csv_reader:
                if name == line[1] and ssn == line[0]:
                    continue
                csv_writer.writerow(line)
            openfile.truncate(0)

    # the data back to the original file
    with open("data/tempfile.csv","r") as openfile:
        csv_reader = csv.reader(openfile)
        with open("data/customers.csv","w",newline="") as writingfile:
            csv_writer = csv.writer(writingfile)
            for line in csv_reader:
                csv_writer.writerow(line)

    # removing the temp file
    os.remove("data/tempfile.csv")

            
