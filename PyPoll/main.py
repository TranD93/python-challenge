import os
import csv
path = r"C:\Users\tranb\OneDrive\Documents\Bootcamp\Homework\python-challenge\PyPoll"
os.chdir(path)

election_csv = os.path.join("Resources","election_data.csv")

with open (election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Set header
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

     #Set variables
    votes = []
    county = []
    candidates = []
    Diana_DeGette = []
    Diana_DeGette_totalvotes = 0
    Charles_Casper_Stockham = []
    Charles_Casper_Stockham_totalvotes = 0
    Raymon_Anthony_Doane = []
    Raymon_Anthony_Doane_totalvotes = 0

    #Loop through each row and assign
    for row in csv_reader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Calculate the total of votes
    total_votes = (len(votes))

    # Calculate the total votes of each candidate
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidates)
            Charles_Casper_Stockham_totalvotes = len(Charles_Casper_Stockham)
            
        elif candidate == "Diana DeGette":
            Diana_DeGette.append(candidates)
            Diana_DeGette_totalvotes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(candidates)
            Raymon_Anthony_Doane_totalvotes = len(Raymon_Anthony_Doane)

    
    # Calculate the percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_totalvotes / total_votes) * 100), 3)
    Diana_DeGette_percent = round(((Diana_DeGette_totalvotes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_totalvotes / total_votes) * 100), 3)
    
    # If statement to find out the winner 
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        Winner = "Charles_Casper_Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
        Winner = "Diana_DeGette"  
    else:
        Winner = "Raymon_Anthony_Doane"


print("Financial Analysis")
print("-----------------------------------")   
print(f"Total Votes: {total_votes}")
print("-----------------------------------") 
print(f"Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_totalvotes})")
print(f"Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_totalvotes})")
print(f"Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_totalvotes})")
print("-----------------------------------") 
print(f"Winner: {Winner}")