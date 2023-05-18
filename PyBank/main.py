#Import os and csv
import os
import csv

#Open and read csv file
pybank = os.path.join("Resources","budget_data.csv")
with open (pybank, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Set the header
    cvs_header = next(csv_reader)
    print(f"Header: {csv_header}")

#Set variables
    total_months = 0
    total_profit_loss = 0
    monthly_changes = []
    previous_profit_loss = 0
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

#Loop through each row 
    for row in csv_reader:
        #Calculate the total number of months 
        total_months += 1

        #Calculate the total net amount of "Profit/Loss" over the entire period
        total_profit_loss += int(row[1])
        
     #Calculate the change in "Profit/Loss" between months over the entire period
        if total_months > 1:
            monthly_change = int(row[1]) - previous_profit_loss
            monthly_changes.append(monthly_change)
            # Check if the current monthly change is the greatest increase or greatest decrease
            if monthly_change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = monthly_change
            elif monthly_change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = monthly_change
        previous_profit_loss = int(row[1])

# Calculate the average change in "Profit/Loss" between months over the entire period
    average_change = sum(monthly_changes) / len(monthly_changes)



print("Financial Analysis")
print("-----------------------------------")    
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
    