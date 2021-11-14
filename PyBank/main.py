#### Import dependencies for os.path.join()
import os
import csv

### Read in a .csv file
csv_file=os.path.join("Resources", "budget_data.csv")
output_path=os.path.join("analysis","financial_analysis.csv")

#define variables
month_total=0
change_month=[]
revenue_total=0
greatest_value=0
revenue=[]
revenue_previous=0
greatest_decrease=["",9999999]
greatest_increase=["",0]
change_revenue_list=[]
change_in_revenue=0
total_amount=[]
highest_profit=0
revenue_average=0

with open(csv_file,"r") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    #skip header
    next(csv_reader)
    for row in csv_reader:
        #add months
        month_total +=1
        revenue_total=revenue_total+int(row[1])
        
        change_in_revenue=float(row[1]) - revenue_previous
        revenue_previous =float(row[1])
        change_revenue_list=change_revenue_list+[change_in_revenue]
        change_month=[change_month] + [row[0]]
        
        if change_in_revenue>greatest_increase[1]:
            greatest_increase[1]=change_in_revenue
            greatest_increase[0]=row[0]
    
        if change_in_revenue<greatest_decrease[1]:
            greatest_decrease[1]=change_in_revenue
            greatest_decrease[0]=row[0]
    revenue_average= sum(change_revenue_list)/len(change_revenue_list)


    
with open(output_path,'w', newline='') as csvwrite:
   csvwriter=csv.writer(csvwrite, delimiter=' ')
   csvwriter.writerow(['Financial Analysis'])
   csvwriter.writerow(['------------------------'])
   csvwriter.writerow(['Total Months: %d' % month_total])
   csvwriter.writerow(['Total Revenue: $%d' % revenue_total])
   csvwriter.writerow(['Average Revenue Change: $%d' % revenue_average])
   csvwriter.writerow(['Greatest Increase in Revenue:%s ($%s)' % (greatest_increase[0], greatest_increase[1]) ]) 
   csvwriter.writerow(['Greatest decrease in Revenue:%s ($%s)' % (greatest_decrease[0],greatest_decrease[1]) ])
  
 
print(f'Financial Analysis')
print(f'------------------------')
print("Total Months: %d" % month_total)
print("Total Revenue: $%d " % revenue_total)
print("Average Revenue Change: $%d" % revenue_average)
print("Greatest Increase in revenue: %s ($%s)" % (greatest_increase[0], (greatest_increase[1])))
print("Greatest decrease in revenue:%s ($%s)" % (greatest_decrease[0], (greatest_decrease[1])))
      