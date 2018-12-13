from data_access import priceDataAccess

class GetPriceList:
    def __init__(self):
        self.priceListDataAccess = priceDataAccess.PriceDataAccess()
    def editPriceList(self,olddata,newdata):
        self.priceListDataAccess.editPriceList(olddata,newdata)
    def checkIfUserHasAuthority(self,username):
        check = self.priceListDataAccess.checkIfUserHasAuthority(username)
        return check