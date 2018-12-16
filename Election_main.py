import os
import csv

path = 'resources/election_data.csv'

#creating emtpy lists and variables
votes = []
total_votes = []
khan = []
khan_votes = []
correy = []
correy_votes = []
li = []
li_votes = []
tooley = []
tooley_votes = []
vote_count = {}

#with open budget data set.
with open(path,newline='') as datafile:
    csvreader = csv.reader(datafile , delimiter=',')

    #removing first row
    csv_header = next(csvreader)
    
    #counting the total of rows in a sheet
    for row in csvreader:
        #append months into months list
        votes.append(row[0])
        #append pnl into pnl list
        if row[2] == "Khan":
            khan.append(row[2])
        if row[2] == "Correy":
            correy.append(row[2])
        if row[2] == "Li":
            li.append(row[2])
        if row[2] == "O'Tooley":
            tooley.append(row[2])
  
    #counting votes
    total_votes = len(votes)
    khan_votes = len(khan)
    correy_votes = len(correy)
    li_votes = len(li)
    tooley_votes = len(tooley)
    vote_count['Khan'] = len(khan)
    vote_count['Correy'] = len(correy)
    vote_count['Li'] = len(li)
    vote_count['Tooley'] = len(tooley)

    #winner = max(khan_votes,correy_votes,li_votes,tooley_votes)
    winner2 = max(vote_count, key=vote_count.get)
    
    #print the results in terminal
    print("---------------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------------")
    print(f'Khan: {format(khan_votes/total_votes, ".3%")} ({khan_votes})')
    print(f'Correy: {format(correy_votes/total_votes, ".3%")} ({correy_votes})')
    print(f'Li: {format(li_votes/total_votes, ".3%")} ({li_votes})')
    print(f"O'Tooley: {format(tooley_votes/total_votes, '.3%')} ({tooley_votes})")
    print("---------------------------")
    print(f"Winner:{winner2}")
    print("---------------------------")

#creating a txt doc.
output = "Election_results.txt"

with open(output,"w") as outputfile:

    #entering inform line-by-line. '\n' creates a newline
    outputfile.write("Election_results")
    outputfile.write('\n' '-----------------------------')
    outputfile.write('\n' f'Total Votes: {total_votes}')
    outputfile.write('\n' "-----------------------------")
    outputfile.write('\n' f'Khan: {format(khan_votes/total_votes, ".3%")} ({khan_votes})')
    outputfile.write('\n' f'Correy: {format(correy_votes/total_votes, ".3%")} ({correy_votes})')
    outputfile.write('\n' f'Li: {format(li_votes/total_votes, ".3%")} ({li_votes})')
    outputfile.write('\n' f"O'Tooley: {format(tooley_votes/total_votes, '.3%')} ({tooley_votes})")
    outputfile.write('\n' "-----------------------------")
    outputfile.write('\n' f"Winner:{winner2}")
    outputfile.write('\n' "-----------------------------")
