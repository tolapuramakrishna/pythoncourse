import csv

with open('customers.csv','r') as fpreader:
    csreader = csv.DictReader(fpreader)

    with open('newcustomers.csv','w') as fpwriter:
        columns = ['first','last']
        csvwriter = csv.DictWriter(fpwriter,fieldnames=columns,delimiter=',',lineterminator='\n')
        csvwriter.writeheader()
        for row in csreader:
            del row['email']
            csvwriter.writerow(row)
        print("work done- csv eport over")