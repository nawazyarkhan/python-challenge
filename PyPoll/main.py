#### Import dependencies for os.path.join()
import os
import csv
import collections
from collections import Counter

### Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []

### Read in a .csv file
csv_file=os.path.join("Resources", "election_data.csv")

with open(csv_file,"r") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    
    #skip header
    next(csv_reader)
    for row in csv_reader:
         voters_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

   
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
  
    
# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# -->>  Export a text file with the results
election_file = os.path.join("analysis", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")    