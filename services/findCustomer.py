import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import customerDataAccess

class FindCustomer:
    def __init__(self,input):
        self.customersDataAccess = customerDataAccess.CustomerDataAccess()
        self.customer = self.searchDataForCustomer(input)
        #if self.customer == False:
        #   print out error message
    def searchDataForCustomer(self,input):
        for key,value in self.customersDataAccess.customers.items():
            if input == key or input == value[0]:
                return [key,value]
        return False