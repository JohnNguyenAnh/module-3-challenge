import csv

# Specify the path to the CSV file
csv_path = "budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Extract date and profit/loss from the current row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the net total
        net_total += profit_loss

        # Calculate the change in profit/loss
        if total_months > 0:
            change = profit_loss - previous_profit_loss
            total_change += change

            # Update greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

        # Increment the total number of months
        total_months += 1

# Calculate the average change
average_change = total_change / (total_months - 1) if total_months > 1 else 0

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Write the analysis results to a text file
output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print(f"Analysis results written to {output_file_path}")