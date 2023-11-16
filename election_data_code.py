import csv

# Specify the path to the CSV file
csv_path = "election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Extract the candidate's name from the current row
        candidate_name = row[2]

        # Increment the total number of votes
        total_votes += 1

        # Update the candidate's votes
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        # Update the winner information
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Calculate the percentage of votes each candidate won
percentage_votes = {name: (votes / total_votes) * 100 for name, votes in candidates.items()}

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Write the election results to a text file
output_file_path = "election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        output_file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")

print(f"Election results written to {output_file_path}")