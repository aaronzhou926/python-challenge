import os
import csv

path = 'resources/budget_data.csv'

#creating emtpy lists and variables
months = []
pnl = []
changes = []
max_value = []
min_value = []
max_date = []
min_date = []

#with open budget data set.
with open(path,newline='') as datafile:
    csvreader = csv.reader(datafile , delimiter=',')

    #removing first row
    csv_header = next(csvreader)
    
    #counting the total of rows in a sheet
    for row in csvreader:
        #append months into months list
        months.append(row[0])
        #append pnl into pnl list
        pnl.append(int(row[1]))
      
    #summing profit/loss
    net_total = sum(pnl)
    
    #getting average change & max and min of change values
    for x in range(1,len(pnl)):
        changes.append(pnl[x]-pnl[(x-1)])
        avervge_change = sum(changes)/len(months)
        max_value = max(changes)
        min_value = min(changes)
    
    max_date = str(months[changes.index(max(changes))+1])
    min_date = str(months[changes.index(min(changes))+1])

    #print the results in terminal
    print(f'Total months:{len(months)}')
    print(f'Total:${net_total}')
    print(f'Average change:${format(avervge_change,".2f")}')
    print(f'Greatest increase in profit:{max_date} ${max_value}')
    print(f'Greatest decrease in profit:{min_date} ${min_value}')

#creating a txt doc.
output = "Financial_Analysis.txt"

with open(output,"w") as outputfile:

    #entering inform line-by-line. '\n' creates a newline
    outputfile.write("Financial Analysis Report")
    outputfile.write('\n' '-----------------------------')
    outputfile.write('\n' f'Total months:{len(months)}')
    outputfile.write('\n' f'Total:${net_total}')
    outputfile.write('\n' f'Average change:${format(avervge_change,".2f")}')
    outputfile.write('\n' f'Greatest increase in profit:{max_date} ${max_value}')
    outputfile.write('\n' f'Greatest decrease in profit:{min_date} ${min_value}')
