import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import customerDataAccess

class AddCustomer:
    def __init__(self,name,ssn,email,phone):
        self.customersDataAccess = customerDataAccess.CustomerDataAccess()
        self.customersDataAccess.addCustomer(name,ssn,email,phone)
        self.customer = self.searchDataForCustomer(input)
    def searchDataForCustomer(self,input):
        for key,value in self.customersDataAccess.customers.items():
            if input == key or input == value[0]:
                return [key,value]
        return False