import os
import csv

datapath=os.path.join("..","PyPoll","election_data.csv")

with open(datapath, 'r', newline="") as datafile:
    datareader= csv.reader(datafile,delimiter=',')
    dataheader=next(datareader)
    # print(datareader)
    # print(dataheader)

    vote_count=0
    candidate_list=[]
    count0=0
    count1=0
    count2=0
    count3=0

    for row in datareader:
        vote_count=vote_count+1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        elif row[2] == candidate_list[0]:
            count0=count0+1
        elif row[2]== candidate_list[1]:
            count1=count1+1
        elif row[2]==candidate_list[2]:
            count2=count2+1
        elif row[2]==candidate_list[3]:
            count3=count3+1
    
    percent0="{:.3%}".format(count0/vote_count)
    percent1="{:.3%}".format(count1/vote_count)
    percent2="{:.3%}".format(count2/vote_count)
    percent3="{:.3%}".format(count3/vote_count)
    
    candidate_counts=[count0, count1, count2,count3]
    most_counts=max(candidate_counts)
    candidate_index=candidate_counts.index(max(candidate_counts))
    winner=candidate_list[candidate_index]
   
    print(candidate_list)
    print(candidate_counts)
    print(most_counts)
    print(winner)
    
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {vote_count}")
    print("--------------------")
    print(f"{candidate_list[0]}: {percent0} ({count0})")
    print(f"{candidate_list[1]}: {percent1} ({count1})")
    print(f"{candidate_list[2]}: {percent2} ({count2})")
    print(f"{candidate_list[3]}: {percent3} ({count3})")
    print("--------------------")
    print(f"Winner: {winner}")
    print("--------------------")