import csv

infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter =',')
infile.readline()

for record in csvfile:
    salary= int(record[3])
    bonus= float(record[4])
    
    total_pay = (salary + (salary * bonus))
    #total_pay = (record[3]) + (int(record[3]) * float(record[4]))
    
    print('Employee id:', record[0])
    print('First Name:', record[1])
    print('Last Name:', record[2])
    print('Salary: $', format(salary, ',.2f'), sep="")
    print('Bonus:', record[4])
    print('Total Pay: $',format(total_pay,',.2f'),sep="")
    print("Press enter for the next customer.")

    input()