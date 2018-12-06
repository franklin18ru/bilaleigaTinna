import csv

class  GetUsers:
    def __init__(self):
        self.users = self.getUsers()

    def getUsers(self):
        user_dictionary = dict()
        with open( "bilaleigaTinna/data/users.csv" , "r" ) as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                ssn = int(line[0])
                password = line[3]
                user_dictionary[ssn] = password  
        return user_dictionary

