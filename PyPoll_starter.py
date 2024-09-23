# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to store candidate votes

# Candidate names list (to store unique candidates)
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1  # Increment the total vote count
        
        candidate_name = row[2]  # Assume the candidate's name is in the 3rd column (index 2)

        # If the candidate is not already in the candidate_votes dictionary, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1  # Add a vote to the candidate's count

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal and text file)
    output = (
        "Election Results\n"
        "----------------------------\n"
        f"Total Votes: {total_votes}\n"
        "----------------------------\n"
    )
    print(output)
    txt_file.write(output)

    # Loop through the candidates to determine vote percentages and print results
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Print and save each candidate's vote count and percentage
        candidate_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_output)
        txt_file.write(candidate_output)

        # Determine the winning candidate and winning vote count
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Generate and print the winning candidate summary
    winning_summary = (
        "----------------------------\n"
        f"Winner: {winning_candidate}\n"
        "----------------------------\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)