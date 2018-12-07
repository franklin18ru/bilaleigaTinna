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
                string = line[0]
                ssn = int(string.replace("-",""))
                name = line[1]
                birthdate = line[2]
                phone = line[3]
                email = line[4]
                customer_dictionary[ssn] = (name,birthdate,phone,email)
            return customer_dictionary
        
    def addCustomer(self,ssn,name,birthdate,phone,email):
        newCustomer=[ssn,name,birthdate,phone,email]
        with open('data/customers.csv', 'a',newline="") as openfile:
            csv_writer = csv.writer(openfile)
            csv_writer.writerow(newCustomer) 

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
        with open("data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/customers.csv","w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("data/tempfile.csv")

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
        with open("data/tempfile.csv","r") as openfile:
            csv_reader = csv.reader(openfile)
            with open("data/leases.csv","w",newline="") as writingfile:
                csv_writer = csv.writer(writingfile)
                for line in csv_reader:
                    csv_writer.writerow(line)

        # removing the temp file
        os.remove("data/tempfile.csv")

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

    
    # def editCustomer((old_Customerdata)(new_Customerdata)):
        # take in all arguments if the argument is the same as in the data itself then  #
        # keep it as is, you need to create a temporary file in order to edit and rewrite #
        # the original file to edit #