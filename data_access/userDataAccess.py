import csv
import os

class UserDataAccess:
    def __init__(self):
        self.users = self.getAllUsers()

    def getAllUsers(self):
        user_dictionary = dict()
        with open( "../data/users.csv" , "r" ) as openfile:
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
                with open('../data/users.csv', 'a',newline="") as openfile:
                        csv_writer = csv.writer(openfile)
                        csv_writer.writerow(newUser)
    
    def deleteUser(self,name,ssn):
        # moving the ../data to a temp file but if any line matches the given input it
        # does not go to the temp file
        with open("../data/users.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("../data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if name == line[1] and ssn == line[0]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the ../data back to the original file
        self.moveFromTempFile("users")

    def editUser(self,olddatalist,newdatalist):
        # take in all arguments if the argument is the same as in the ../data itself then  #
        # keep it as is, you need to create a temporary file in order to edit and rewrite #
        # the original file to edit #
        new_ssn = newdatalist[0]
        new_position = newdatalist[1]
        new_name = newdatalist[2]
        new_password = newdatalist[3]
        with open("../data/users.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("../data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if olddatalist == line:
                        new_line = [new_ssn,new_position,new_name,new_password]
                        csv_writer.writerow(new_line)
                        continue                        
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the ../data back to the original file
        self.moveFromTempFile("users")


    def moveFromTempFile(self,fileName):
        # the ../data back to the original file
        filetowrite = "../data/"+fileName+".csv"
        with open("../data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open(filetowrite,"w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("../data/tempfile.csv")