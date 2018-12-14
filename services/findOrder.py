import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import leasesDataAccess

class FindCustomer:
    def __init__(self,input):
        self.leaseDataAccess = leasesDataAccess.LeasesDataAccess()
        self.lease = self.searchDataForLease(input)
        #if self.customer == False:
        #   print out error message
    def searchDataForLease(self,input):
        for key,value in self.leaseDataAccess.leases.items():
            if input == key or input == value[0] or input == value[4]:
                return [key,value]
        return False