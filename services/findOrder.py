import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_access import leasesDataAccess

class FindOrder:
    def __init__(self,input):
        self.leaseDataAccess = leasesDataAccess.LeasesDataAccess()
        self.lease = self.searchDataForLease(input)
        #if self.customer == False:
        #   print out error message
    def searchDataForLease(self,input):
        self.orders = []
        for  item in self.leaseDataAccess.leases:
            if input == str(item[0]) or input.capitalize() == item[1] or input.upper() == item[4]:
                    self.orders.append(item)
        if len(self.orders) > 0:
            return self.orders
        else:
            return False
    def editOrder(self,newdatalist):
        oldLicense = self.lease[0][4]
        oldStartDate = self.lease[0][2]
        oldEndDate = self.lease[0][3]
        olddata = [oldLicense,oldStartDate,oldEndDate]
        self.leaseDataAccess.editLease(olddata,newdatalist)

    def deleteLease(self,ssn,lease_start, license_plate):
        self.leaseDataAccess.deleteLease(ssn,lease_start,license_plate)
        #lease_list.append([ssn, renter,leaseStart,leaseEnd,licensePlate,state])