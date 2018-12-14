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
    def editCustomer(self,newdatalist):
        oldname = self.customer[1][0]
        oldssn = self.customer[0]
        oldemail = self.customer[1][1]
        oldphone = self.customer[1][2]
        olddata = [oldname,oldssn,oldemail,oldphone]
        self.customersDataAccess.editCustomer(olddata,newdatalist)
        
    def deleteCustomer(self,name,ssn):
        self.customersDataAccess.deleteCustomer(name,ssn)
        self.customersDataAccess.deleteCustomerLeases(name,ssn)


    #John Newman,1510924339,Johnnyboi@gmail.com,584-12345
    #1510924339,John Newman,2018.12.10,2018.12.18,KO646