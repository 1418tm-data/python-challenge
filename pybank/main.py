import os
import csv

# Path to collect data from the csv file in the Resources folder
pybank_csv = os.path.join("resources", "budget_data.csv")

with open(pybank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader_total = csv.reader(csvfile, delimiter=',')
    #ignore the header row
    next(csvfile, None)

    total = sum(float(row[1]) for row in csvreader_total)

with open(pybank_csv, 'r') as csvfile_count:    
    
    csvreader_count = csv.reader(csvfile_count, delimiter=',')
    #ignore the header row
    next(csvfile_count, None)
    
    #count number of months
    row_count = sum(1 for row in csvreader_count)    

    

    #total = 0
    #for row in csvreader:
        #total += float(row[1])
    
    
    #print the results
    print(f"Total Months: {row_count}")
    print(f"Total: {total}")
    




