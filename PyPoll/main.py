import csv, os

file = os.path.join("Resources", "election_data.csv")

with open(file, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    data = list(csv_reader)
### Vote Count ###
    vote_count = len(data)
    print("=================================")
    print(f"Total Votes: {vote_count}")
    print("=================================")

    khan_votes = 0
    khan_percent = 0
    correy_votes = 0
    correy_percent = 0
    li_votes = 0
    li_percent = 0 
    otooley_votes = 0 
    otooley_percent = 0

    for row in data:
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

    khan_percent = round(float(khan_votes / vote_count) * 100, 2)
    correy_percent = round(float(correy_votes / vote_count) * 100, 2)
    li_percent = round(float(li_votes / vote_count) * 100, 2)
    otooley_percent = round(float(otooley_votes / vote_count) * 100, 2)
    print(f"khan Votes: {khan_percent}% {khan_votes}")
    print(f"Correy Votes: {correy_percent}% {correy_votes}")   
    print(f"Li Votes: {li_percent}% {li_votes}")
    print(f"O'Tooley Votes: {otooley_percent}% {otooley_votes}")
    print("================================")
    