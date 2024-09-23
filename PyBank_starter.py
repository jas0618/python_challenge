import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
previous_profit_loss = None  # To store the previous row's profit/loss value
months = []
dates = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through the data rows
    for row in reader:
        date = row[0]
        current_profit_loss = int(row[1])
        
        # Count total months and add to the total net profit/loss
        total_months += 1
        total_net += current_profit_loss
        dates.append(date)

        # Calculate the net change (if there's a previous row)
        if previous_profit_loss is not None:
            net_change = current_profit_loss - previous_profit_loss
            net_change_list.append(net_change)

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average change, greatest increase, and greatest decrease
if len(net_change_list) > 0:
    average_change = sum(net_change_list) / len(net_change_list)
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)

    # Find the corresponding months for greatest increase and decrease
    greatest_increase_month = dates[net_change_list.index(greatest_increase) + 1]
    greatest_decrease_month = dates[net_change_list.index(greatest_decrease) + 1]
else:
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = "N/A"
    greatest_decrease_month = "N/A"

# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")