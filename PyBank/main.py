# Main Script PyBank_Similar to Previous Homework - Stocks
# We need to import the os module to create file paths
import os

# The we import the module that allow reading CSV files
import csv

# Path to the source file in order to collect data from the there
budget_cvs_path = os.path.join("raw_data", "budget_data_1.csv")

# Start a list
months = []
revenue = []
greatest_difference = []
# initialize the counter
total_revenue = 0
total_months = 0

# Open the file and get the data into csv_reader variable
with open(budget_cvs_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
  
# Not reading the Header
    next(csv_reader, None)

# Loop to get the data: Get the total months-->total_months, total revenue-->total_revenue
# Add the months and revenue to a list to be used to calculate the greatest difference, great
# increase and great decrease. 
    for row in csv_reader:
        total_revenue = total_revenue + int(row[1])
        total_months = total_months + 1
        months.append(row[0])
        revenue.append(row[1])
# Loop to get the highest difference between the revenues
    for n in range(len(revenue) - 1):
        greatest_difference.append(int(revenue[n+1])-int(revenue[n]))
# Calculate the average change in revenue between months over the entire period
    average_change = sum(greatest_difference) / len(greatest_difference)
# Calculate the greatest increase in revenue --> Great Increase
    great_increase = max(greatest_difference)
    great_increase_index = greatest_difference.index(great_increase)
# Find the month that correlates with the greatest increase
    great_increase_month = months[great_increase_index + 1]
# Calculate the greatest decrease --> great_decrease 
    great_decrease = min(greatest_difference)
    great_decrease_index = greatest_difference.index(great_decrease)
# Find the month that correlates with the greatest decrease
    great_decrease_month = months[great_decrease_index + 1]

# Printing the results to the Terminal
print("Financial Analysis")
print("--------------------------------")
print("Total Revenue: $" + str(total_revenue))
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + str(great_increase_month) + " ($" + str(great_increase) + ")")
print("Greatest Decrease in Revenue: " + str(great_decrease_month) + " ($" + str(great_decrease) + ")")

# Write the results to a txt file
output_file = open('results.txt','w')
output_file.write("Financial Analysis"+ "\n")
output_file.write("--------------------------------"+ "\n")
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total Revenue: $" + str(total_revenue) + "\n")
output_file.write("Average Revenue Change: $" + str(average_change) + "\n")
output_file.write("Greatest Increase in Revenue: " + str(great_increase_month) + " ($" + str(great_increase) + ")"+ "\n")
output_file.write("Greatest Decrease in Revenue: " + str(great_decrease_month) + " ($" + str(great_decrease) + ")")
output_file.close()

