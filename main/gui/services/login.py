from data_access.getUsers import GetUsers

class loginVerification:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    
    def verify(self):
        userInstance = GetUsers()
        userDict = userInstance.__users
        for key, value in userDict.items():
            if self.__username == key and self.__password == value:
                return True
            else:
                return False

