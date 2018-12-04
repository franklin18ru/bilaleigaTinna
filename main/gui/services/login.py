import sys
# Add the current directory to `sys.path`.
if sys.path[0] != '':
    sys.path.insert(0, '')
class loginVerification:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        print ("TEST")