class FindCustomer:
    def __init__(self, leitarstrengur):
        import csv
        self.leitarstrengur = leitarstengur.capitalize()
        with open('data/leases.csv', 'r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for row in csv_reader:
                if self.leitarstrengur == row[0]:
                    return(row)
                elif self.leitarstrengur == row[4]:
                    return(row)
                elif self.leitarstrengur == row[1]:
                    return(row)