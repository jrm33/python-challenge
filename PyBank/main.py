# Import Modules
import os
import csv

# Set path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Find first row
    first_row = next(csvreader)

# Variables
    total_month = 0
    total_profit = 0
    avg_profit_change = 0
    row_count = 0
    greatest_increase = 0
    greatest_decrease = 0
    prev_net = int(first_row[1])
    net_change_list = []
    num_changes = 85
    net_change = 0

# Read through data to find total months
# Net total amount of "Profit/Losses" over entire period
# Net change amount
    for row in csvreader: 
        total_month += 1
        total_profit += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)

# Find greatest increase AND decrease (months)


# Average of change
avg_profit_change = round(sum(net_change_list)/(num_changes), 2)


# Print
print("Total Months:", total_month + 1)
print("Total: $", total_profit)
print("Average Change: $", avg_profit_change)
print("Greatest Increase in Profits: $", max(net_change_list))
print("Greatest Decrease in Profits: $", min(net_change_list))
