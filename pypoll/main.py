import os
import csv
import operator

# Path to collect data from the csv file in the Resources folder
pypoll_csv = os.path.join("resources", "election_data.csv")
# Read the csv file and create a list of dictionaries
with open(pypoll_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #identify and store the header row
    header = next(csvfile, None)
    # Create empty lists to store votes and candidates
    total_votes = []
    candidate_list = []    
    # Fill the lists with the data using the for command
    for row in csvreader:
        total_votes.append(float(row[0]))
        candidate_list.append(row[2])
    # Create a dictionary to store the candidate and the votes they got
    from collections import Counter
    candidate = Counter(candidate_list)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {len(total_votes)}")
    print("-------------------------")
    # Iterate through the dictionary to print the candidate with their votes and % votes
    for k in candidate:
        print(k + ":", format(candidate[k]/len(total_votes)*100,".3f") + "% " +"(" + str(candidate[k]) + ")")
    # Use the operator.itemgetter to get the max value in the dictionary candidate, which is the vote, hence the winner    
    winner = max(candidate.items(), key=operator.itemgetter(1))[0]
          
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    
    # create a new textfile to write the results to
pypoll_txt = os.path.join("analysis", "pypoll.txt")
#open the file and begin the writing process
with open(pypoll_txt, 'w', newline='') as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("Total Votes: " +str(len(total_votes)) + "\n")
    txtfile.write("-------------------------" + "\n")
    for k in candidate:
        txtfile.write(k + ":" + format(candidate[k]/len(total_votes)*100,".3f") + "% " +"(" + str(candidate[k]) + ")" + "\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("Winner: " + winner + "\n")
    txtfile.write("-------------------------" + "\n")
    