#TASKS: import the csv file(s)
import csv
import os

#I thought it would be fun to see if I could promt for the file name and then use that for the script and output.
#Seems to work and makes the code flexible so that you wouldn't have to edit the code to run it on different files.
csv_name_short = input('Please place the file to analyze in this directory and enter the filename without filetype: ')

#creates a filename to grab to read the budget data
csv_name = csv_name_short + '.csv'

#creates a name for the output data text file
output_name = csv_name_short + 'summary.txt'

budget_path = os.path.join(csv_name)

#set initial variables
total = 0
months = 0
rev_change_total = 0
greatest_increase = 0
greatest_decrease = 0
previous_revenue = 0

#open the csv and sum up all the monthly revenue

with open(budget_path, newline='') as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")
    next(budget_reader)

    for row in budget_reader:
        months = months + 1
        total = total + int(row[1])
        
        #it was not clear from the isntructions whether the "average change in revenue between months"
        #was referring to the difference from month 1 to month 2 (for example April revenue - March revenue)
        #or whether it was referring to just the average of each month's revenue. I calculated the average 
        #of the differences (so the average of all the Month 2- Month 1)

        rev_change = int(row[1]) - previous_revenue
        
        rev_change_total = rev_change_total + rev_change
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

        #set the previous_revenue variable to be the current row's revenue, to be used next loop
        previous_revenue = int(row[1])

#calculates the average change in revenue between months based on the sum of the previous changes
average_change = int(rev_change_total / int(months - 1))

# create and print to a text file
text_output = open(output_name, 'w')

text_output.write('Financial Analysis\n')
text_output.write('------------------\n')
text_output.write("Total Months: " + str(months) + '\n')
text_output.write("Total Revenue Gained: $" + str(total) + '\n')
text_output.write('Average Revenue Change: $' + str(average_change) + '\n')
text_output.write('Greatest Increase in Revenue: ' + greatest_increase_month + ' ($' + str(greatest_increase) + ')\n')
text_output.write('Greatest Decrease in Revenue: ' + greatest_decrease_month + ' ($' + str(greatest_decrease) + ')\n')

text_output.close()

#output to the terminal
print('Financial Analysis')
print('------------------')
print("Total Months: " + str(months))
print("Total Revenue Gained: $" + str(total))
print('Average Revenue Change: $' + str(average_change))
print('Greatest Increase in Revenue: ' + greatest_increase_month + ' ($' + str(greatest_increase) + ')')
print('Greatest Decrease in Revenue: ' + greatest_decrease_month + ' ($' + str(greatest_decrease) + ')')
