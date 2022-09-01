import csv
infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter=',')

for record in csvfile:
        print('ID', record[0])
        print('First Name', record[1])
        print('Last Name', record[2])
        print('City', record[3])
        print('Country', record[4])
        print('Phone Number', record[5])

        input()
        
