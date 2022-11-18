# Import Modules
import os
import csv

# Set Path for CSV File
csvpath = os.path.join("Resources", "election_data.csv")

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Variables
    total_votes = 0
    candidates_list = []
    votes_won = {}

# Find Total Votes
# Find candidates who recieved votes
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            votes_won[row[2]] = 0
        votes_won[row[2]] += 1


# Find percent of votes each candidate recieved
# votes_won / total_votes for each candidate
# Split votes_won dict into list

# Find Winner print (Diana DeGette)
max_value = max(votes_won.values())

max_key = max(votes_won, key=votes_won.get)


# Print
print("Election Results:")
print("Total Votes:", total_votes)
print("Votes Won by Candidate:", votes_won)
print("Winner:", max_key)
