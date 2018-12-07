import csv
import os

class UserDataAccess:
    def __init__(self):
        self.users = self.getUsers()

    def getUsers(self):
        user_dictionary = dict()
        with open( "data/users.csv" , "r" ) as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                string = line[0]
                ssn = int(string.replace("-",""))
                password = line[3]
                user_dictionary[ssn] = password  
        return user_dictionary

    def addUser(self,ssn,position,name,password):
                newUser=[ssn,position,name,password]
                with open('data/users.csv', 'a',newline="") as openfile:
                        csv_writer = csv.writer(openfile)
                        csv_writer.writerow(newUser)
    
    def deleteUser(self,name,ssn):
        # moving the data to a temp file but if any line matches the given input it
        # does not go to the temp file
        with open("data/users.csv","r+") as openfile:
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
            with open("data/users.csv","w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("data/tempfile.csv")