import csv

class  GetUsers:
    def __init__(self):
        self.__users = self.getusers()

    def getusers(self):
        user_dictionary = dict()
        with open("users.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                ssn = line[0]
                position = line[1]
                name = line[2]
                password = line[3]
                user_dictionary[password] = (name, ssn, position)
                print(line)
        return user_dictionary
    

instance = GetUsers()
