import os
import csv

datapath=os.path.join("..","PyPoll","election_data.csv")

with open(datapath, 'r', newline="") as datafile:
    datareader= csv.reader(datafile,delimiter=',')
    dataheader=next(datareader)
    # print(datareader)
    # print(dataheader)

    print("Election Results")