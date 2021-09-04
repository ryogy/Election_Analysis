import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

# Vote Counter to initialize votes to zero
total_votes = 0
candidate_options = []

# Dictionary to store votes for each candidate
candidate_votes = {}

# Winning Candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   headers = next(file_reader)

   for row in file_reader:
      # Add votes to total count
      total_votes += 1

      candidate_name = row[2]
      if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)
         # Tracking particular candidate vote count
         candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1

   for candidate_name in candidate_options:
      votes = candidate_votes[candidate_name]
      vote_percentage = (float(votes) / float(total_votes) * 100)
      print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

      # Determine winning candidate
      if (votes > winning_count) and (vote_percentage > winning_percentage):
         winning_count = votes
         winning_percentage = vote_percentage
         winning_candidate = candidate_name 

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
      
         
   
      

          
   

          
      



    
