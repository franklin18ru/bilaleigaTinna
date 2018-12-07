import csv 

def getCustomerLeases(name,kennitala):
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
                            






