#### Import dependencies for os.path.join()
import os
import csv

### Define PyPoll's variables
votes_total=0
candidates_list=[]
candidate_votes={}
num_of_winner=0
winner_list=[]
winner=""

### Read in a .csv file
csv_file=os.path.join("Resources", "election_data.csv")
with open(csv_file,"r") as csv_file:
           csv_reader=csv.reader(csv_file,delimiter=',')
           #skip header
           next(csv_reader)
           for row in csv_reader:
               votes_total += 1

               candidate=row[2]
   
               if candidate not in candidates_list:
                   candidates_list.append(candidate)
                   candidate_votes[candidate] = 1
        
               candidate_votes[candidate]=candidate_votes[candidate] +1

winner1 = [(value, key) for key, value in candidate_votes.items()]
winner=max(winner1)[1]        
    
#### output file
election_file = os.path.join("analysis", "election_data.txt")
with open(election_file, "w") as outfile:

    print("Election Results")
    print("-------------------------")
    print("Total votes %d" % votes_total)
    print("-------------------------")

    #voter_output1= 
    #voter_output2=
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(votes_total)*100
        if (votes > num_of_winner):
            winner_count = votes
            winner2 = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        #print("Total votes %d" % votes_total)
        #print("-------------------------")
        print(voter_output)
        
        outfile.write(voter_output)
               
    winner_summary = (
        f"Winner: {winner}\n"
        #f"Winner: max(winner1)[1]\n"
    )
    outfile.write("-------------------------\n") 
    print("-------------------------")
    print(winner_summary)
    outfile.write(winner_summary)
    outfile.write("-------------------------\n")    

print("-------------------------")

#print(f"Winner:  {votes_per_candidate[0][0][0]}")
#print("-------------------------")




   