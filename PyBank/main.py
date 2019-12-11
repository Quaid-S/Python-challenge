import os, csv

file = os.path.join("Resources", "budget_data.csv")

### Reading the whole file ###
# with open(file, "r") as reader:
#     lines = reader.read()
#     print(lines)
#     print(type(lines))

### Ommiting Header and finding Month Count ###
with open(file, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    data = list(csv_reader)
    month_count = len(data) 
    print(f"Total months: {month_count}")
### Finding Total Profit ###
    total = sum(float(row[1]) for row in data)
    print(f"Total Profit/Loss: {total}")

  

       