import os
import csv
import sys

datapath= os.path.join("..","PyBank","budget_data.csv")

with open (datapath, 'r', newline="") as datafile:
    datareader=csv.reader(datafile, delimiter=',')
    # print(datareader)
    dataheader=next(datareader)
    # print(dataheader)

    month_count=0
    net_total=0
    profit_loss_list=[]
    month_list=[]
   

    for row in datareader:
        month_count= month_count+1
        net_total = net_total + int(row[1])
        profit_loss=int(row[1])
        profit_loss_list.append(profit_loss)
        month=row[0]
        month_list.append(month)
        
    profit_loss_chg=[profit_loss_list[i+1]-profit_loss_list[i] for i in range(len(profit_loss_list)-1)]
    increase=max(profit_loss_chg)
    decrease=min(profit_loss_chg)
    increase_index=profit_loss_chg.index(max(profit_loss_chg))
    decrease_index=profit_loss_chg.index(min(profit_loss_chg))
    increase_month=month_list[increase_index+1]
    decrease_month=month_list[decrease_index+1]
    chg_total=sum(profit_loss_chg)
    chg_len=len(profit_loss_chg)
    avg_chg=round(chg_total/chg_len, 2)
    # print(increase_month)
    # print(decrease_month)
    # print(increase_index)
    # print(decrease_index)
    # print(avg_chg)

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_chg}")
    print(f"Greatest Increase in Profits: {increase_month} (${increase})")
    print(f"Greastest Decrease in Profits: {decrease_month} (${decrease})")
    # print(profit_loss_list)
    # print(profit_loss_chg)
    # print(month_list)
    
# with open('budgetresults.text', 'w') as f:
#     sys.stdout = f
