import csv

infile = open('customers.csv', 'r')
outfile = open ('customer_country.csv','w')

csv_file = csv.reader(infile, delimiter =',')

next(csv_file)

outfile.write("Full Name, Country\n")

for record in csv_file:
    full_name = record[1] + " " + record [2]
    country = record[4]

    outfile.write(full_name + ',' + country + '\n')

outfile.close()