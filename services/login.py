import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import data_access.getUsers as getUsers
class loginVerification:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    
    def verify(self):
        userInstance = getUsers.GetUsers()
        userDict = userInstance.users
        for key, value in userDict.items():
            if self.__username == key and self.__password == value:
                return True
        return False

