class loginVerification:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    
    def verify(self):
        userDict = {1808972759: "theking", 2710982359: "thepleb"}
        for key, value in userDict.items():
            if self.__username == key and self.__password == value:
                return True
            else:
                return False


