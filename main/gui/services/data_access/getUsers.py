import csv

class  GetUsers:
    def __init__(self):
        self.__users = self.getUsers()

    def getUsers(self):
        user_dictionary = dict()
        with open( "data/users.csv" , "r" ) as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                ssn = int(line[0])
                password = line[3]
                user_dictionary[ssn] = password 
        print(user_dictionary)  
        return user_dictionary

