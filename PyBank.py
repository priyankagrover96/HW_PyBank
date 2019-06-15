# Interface with OS
import os

# Import CSV to read the data from the PyBank_HW file
import csv

# Locate CSV path & file in directory
csvpath = os.path.join("budget_data.csv")

#-----------------------------------------------------------------------------------
# Lists to store data
profit = []
monthly_change = []
date = []

# State variables
count = 0
total_profit = 0
initial_profit = 0
total_change_profits = 0

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    # (budget_data.csvpath)

    # Using 'count' to calculate the number of months in this dataset 
    for row in csvreader:
        count = count + 1

        # will need to append when collecting the greatest profit increase & decrease
        date.append(row[0])

        # Append profit info and calculate total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store these monthly changes in a list
        monthly_change.append(monthly_change_profits)

    total_change_profits = total_change_profits + monthly_change_profits
    initial_profit = final_profit

    #Calculate the average change in profits
    average_change_profits = (total_change_profits/count)
    
    #Find the max and min change in profits and the corresponding dates these changes were obeserved
    greatest_increase_profits = max(monthly_change)
    greatest_decrease_profits = min(monthly_change)

    increase_date = date[monthly_change.index(greatest_increase_profits)]
    decrease_date = date[monthly_change.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")