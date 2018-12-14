import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import customerDataAccess

class AddCustomer:
    def __init__(self,name,ssn,email,phone):
        self.customersDataAccess = customerDataAccess.CustomerDataAccess()
        self.customersDataAccess.addCustomer(name,ssn,email,phone)