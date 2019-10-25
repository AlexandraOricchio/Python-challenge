import os
import csv

datapath=os.path.join("..","PyPoll","election_data.csv")

with open(datapath, 'r', newline="") as datafile:
    datareader= csv.reader(datafile,delimiter=',')
    dataheader=next(datareader)
    # print(datareader)
    # print(dataheader)

    #count total votes made in this data set
    #create list of candidates column from data set
    vote_count=0
    data_candidate_list=[]
    for row in datareader:
        vote_count=vote_count+1 
        cand=row[2]
        data_candidate_list.append(cand)   

    #create a list of lists to identify unique candidates, their vote count and percentage of votes overall
    results_list=[[x,"{:.3%}".format(int(data_candidate_list.count(x))/vote_count),data_candidate_list.count(x)] for x in set(data_candidate_list)]
    # print(results_list)

    #create list of vote counts per candidate
    candidate_votes_list=[]
    for i in range(len(results_list)):
        candidate_votes = results_list[i][2]
        candidate_votes_list.append(candidate_votes)
    # print(candidate_votes_list)

    #identify largest value of vote counts and use indices to identify which candidate's results list match 
    max_votes=max(candidate_votes_list)
    max_index=candidate_votes_list.index(max(candidate_votes_list))
    winner=results_list[max_index]
    # print(max_votes)
    # print(max_index)
    # print(winner)
   
    print("Election Results")
    print("-" * 35)
    print(f"Total Votes: {vote_count}")
    print("-" * 35)
    for i in range(len(results_list)):
            print(f"{results_list[i][0]}: {results_list[i][1]} ({results_list[i][2]})")
    print("-" * 35)
    print(f"Winner: {winner[0]}")
    print("-" * 35)

output_path=os.path.join("..","PyPoll","PyPoll_Results.txt")
with open(output_path, 'w', newline="") as resultfile:
    resultfile.write("Election Results\n")
    resultfile.write("-" * 35 + "\n")
    resultfile.write(f"Total Votes: {vote_count}\n")
    resultfile.write("-" * 35 + "\n")
    for i in range(len(results_list)):
            resultfile.write(f"{results_list[i][0]}: {results_list[i][1]} ({results_list[i][2]})\n")
    resultfile.write("-" * 35 + "\n")
    resultfile.write(f"Winner: {winner[0]}\n")
    resultfile.write("-" * 35 + "\n")

