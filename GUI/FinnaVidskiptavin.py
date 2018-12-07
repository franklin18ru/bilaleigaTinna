def FindCustomer(leitarstrengur):
    import csv
    leitarstrengur = leitarstengur.capitalize()

    with open('data/leases.csv', 'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for row in csv_reader:
            if leitarstrengur == row[0]:
                return(row)
            elif leitarstrengur == row[1]:
                return(row)