class FindCustomer:
    def __init__(self, searchString):
        import csv
        self.searchString = searchString.capitalize()
        with open('data/customers.csv', 'r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for row in csv_reader:
                if self.searchString == row[0]:
                    return(row)
                elif self.searchString == row[4]:
                    return(row)
                elif self.searchString == row[1]:
                    return(row)