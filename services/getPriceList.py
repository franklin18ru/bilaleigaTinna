from data_access import priceDataAccess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
class GetPriceList:
    def __init__(self):
        self.priceListDataAccess = priceDataAccess.PriceDataAccess()
    def editPriceList(self,newdata):
        self.priceListDataAccess.editPriceList(newdata)
    def checkIfUserHasAuthority(self,username):
        check = self.priceListDataAccess.checkIfUserHasAuthority(username)
        return check