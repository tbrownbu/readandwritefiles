import csv

infile = open('steps.csv','r')
outfile= open('avg_steps.csv', 'w')

every_month = ['Discard','January','Febuary','March','April','May','June','July','August','September','October','November','December']
csv_file = csv.reader(infile,delimiter=",")
infile.readline()
month = 1
day = 0 
total_steps = 0
for line in csv_file:
    if line[0] == str(month):
        total_steps += int(line[1])
        day +=1 
    
    else:
        avg_steps = format(total_steps/day,'.2f')
        outfile.write(every_month[int(month)] + ',' + str(avg_steps) + '\n')
        month = line[0]
        total_steps=int(line[1])
        day = 1

avg_steps = format(total_steps/day, '.2f')
outfile.write(every_month[int(month)] + ',' + str(avg_steps) + '\n')
outfile.close()