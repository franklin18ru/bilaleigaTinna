import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import customerDataAccess

class GetCostumers:
    def __init__(self):
        self.customersDataAccess = customerDataAccess.CustomerDataAccess()
        self.customers = self.customersDataAccess.customers