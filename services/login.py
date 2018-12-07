import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import data_access.userDataAccess as getUsers
class loginVerification:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    
    def verify(self):
        userInstance = getUsers.UserDataAccess() #Creates an instance of the getUsers file.
        userDict = userInstance.users #Takes the dictionary made in the getUsers file. 
        for key, value in userDict.items():
            if self.__username == key and self.__password == value: # Compared the input made by the user and the users from the database.
                return True
        return False

