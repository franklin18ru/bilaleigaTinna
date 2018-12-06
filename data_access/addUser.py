import csv

def addUser(ssn,position,name,password):
    newUser=[ssn,position,name,password]
    with open('data/users.csv', 'a',newline="") as openfile:
        csv_writer = csv.writer(openfile)
        csv_writer.writerow(newUser) 