import csv
import os

def deleteLease(ssn,leaseStart,licensePlate):
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
    with open("data/tempfile.csv","r") as openfile:
        csv_reader = csv.reader(openfile)
        with open("data/leases.csv","w",newline="") as writingfile:
            csv_writer = csv.writer(writingfile)
            for line in csv_reader:
                csv_writer.writerow(line)

    # removing the temp file
    os.remove("data/tempfile.csv")


