import os
import csv

# Path to collect data from the csv file in the Resources folder
pybank_csv = os.path.join("resources", "budget_data.csv")

# Read the csv file and create a list of dictionaries
with open(pybank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #identify and store the header row
    header = next(csvfile, None)
    # Create some empty lists to start with
    profit_loss = []
    month = []
    prof_loss_change = []
    
    # loop through the 2 columns and polulate the lists
    for row in csvreader:
        profit_loss.append(float(row[1]))
        month.append(row[0])

    
    print("Financial Analysis")
    print("-----------------------------") 
    print(f"Total Months: {len(month)}")
    print(f"Total: ${round(sum(profit_loss),0)}")

    # This loop is to find the difference in the Profit/ Loss column and get total change
    # Also find the greatest increase and decrease in Profit/ Loss
    prof_loss_change = [profit_loss[i] - profit_loss[i-1] for i in range(1,len(profit_loss))]     
    avg_change = sum(prof_loss_change)/len(prof_loss_change)
    #create new variables to store the greatest change in profit/loss
    great_inc = max(prof_loss_change) 
    great_dec = min(prof_loss_change)
    # create variables to store dates corresponding to the greatest change in profit/loss
    great_inc_date = str(month[prof_loss_change.index(great_inc)+1])
    great_dec_date = str(month[prof_loss_change.index(great_dec)+1])

    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc})")
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec})")
    print("------")
    
# create a new textfile to write the results to
pybank_txt = os.path.join("analysis", "pybank.txt")
#open the file and begin the writing process
with open(pybank_txt, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("-----------------------------" + "\n")
    txtfile.write("Total Months: " +str(len(month)) + "\n")
    txtfile.write("Total: $" +str(round(sum(profit_loss),0)) + "\n")
    txtfile.write("Average Change: $" + str(round(avg_change,2)) + "\n")
    txtfile.write("Greatest Increase in Profits: "+ str(great_inc_date) + "($" + str(great_inc) + ")" + "\n")
    txtfile.write("Greatest Decrease in Profits: "+ str(great_dec_date) + "($" + str(great_dec) + ")" + "\n")
    txtfile.write("-------" + "\n") 

   
    
    








