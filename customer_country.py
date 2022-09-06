import csv

def main():

    outfile = open('Customer_country.csv', 'w')
    infile = open('customers.csv', 'r')
    csv_file = csv.reader(infile, delimiter =',')

    outfile.write('Full Name,Country')

    for customer in infile:
        outfile.write(customer[1] + ',' + customer[2] + ',' + customer[4]+ '\n')

    outfile.close()

main()
