import csv
import os

class CustomerDataAccess:
    def __init__(self):
        self.customers = self.getAllCustomers()

    def getAllCustomers(self):
        customer_dictionary = dict()
        with open("data/customers.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                name = line[0]
                ssn = line[1]
                email = line[2]
                phone = line[3]
                customer_dictionary[ssn] = (name,phone,email)
            return customer_dictionary
        
    def addCustomer(self,name,ssn,phone,email): 
        with open('data/customers.csv', 'a') as openfile:
            openfile.write("\n"+name+","+ssn+","+phone+","+email)
            

    def deleteCustomer(self,name,ssn):
        # moving the data to a temp file but if any line matches the given input it
        # does not go to the temp file
        self.deleteCustomerLeases(name,ssn)
        with open("data/customers.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if name == line[1] and ssn == line[0]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("customers")

    def deleteCustomerLeases(self,name,ssn):
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if name == line[1] and ssn == line[0]:
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")

    def getCustomerLeases(self,name,kennitala):
        lease_dictionary = dict()
        with open("data/leases.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            next(csv_reader)
            for line in csv_reader:
                renter = line[1]
                string = line[0]
                ssn = int(string.replace("-",""))
                if name == renter and int(kennitala) == ssn:
                    leaseStart = line[2]
                    leaseEnd = line[3]
                    licensePlate = line[4]
                    with open("data/cars.csv","r") as secondopenfile:
                        csv_reader2 = csv.reader(secondopenfile)
                        next(csv_reader2)
                        for line2 in csv_reader2:
                            if licensePlate == line2[0]:
                                brandstring = line2[2].replace(" ","")
                                listi = brandstring.split("-")
                                brand = listi[0]
                                subtype = listi[1]
                                lease_dictionary[ssn] = (renter,leaseStart,leaseEnd,licensePlate,brand,subtype)
                                
                                return lease_dictionary

    
    def editCustomer(self,old_Customerdata,new_Customerdata):
        # take in all arguments if the argument is the same as in the data itself then  #
        # keep it as is, you need to create a temporary file in order to edit and rewrite #
        # the original file to edit #
        old_ssn = old_Customerdata[0]
        old_name = old_Customerdata[1]
        new_ssn =  new_Customerdata[0]
        new_name =  new_Customerdata[1]
        new_birthday =  new_Customerdata[2]
        new_phone =  new_Customerdata[3]
        new_email =  new_Customerdata[4]
        with open("data/customers.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if old_Customerdata == line: 
                        new_line = [new_ssn,new_name,new_birthday,new_phone,new_email]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("customers")

        if old_ssn == new_ssn and old_name == new_name:
            pass
        else:
            self.editCostumerLeases(old_ssn,old_name,new_ssn,new_name)
            # edit customer then edit all leases if the ssn or name is edited #

    def editCostumerLeases(self,old_ssn,old_name,new_ssn,new_name):
        with open("data/leases.csv","r+") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/tempfile.csv","w",newline="") as tempfile:
                csv_writer = csv.writer(tempfile)
                for line in csv_reader:
                    if old_name == line[1] and old_ssn == line[0]:
                        new_line = [new_ssn,new_name,line[2],line[3],line[4]]
                        csv_writer.writerow(new_line)
                        continue
                    csv_writer.writerow(line)
                openfile.truncate(0)

        # the data back to the original file
        self.moveFromTempFile("leases")


    
    def moveFromTempFile(self,fileName):
        # the data back to the original file
        filetowrite = "data/"+fileName+".csv"
        with open("data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open(filetowrite,"w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

            # removing the temp file
            os.remove("data/tempfile.csv")