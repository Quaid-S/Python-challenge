import os, csv

file = os.path.join("Resources", "budget_data.csv")

### Reading the whole file ###
# with open(file, "r") as reader:
#     lines = reader.read()
#     print(lines)
#     print(type(lines))

### Ommiting Header and finding Month Count ###
with open(file, newline='') as csv_file:
    print("Financial Analysis")
    print("=================================")
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    data = list(csv_reader)  ## mav said use dict not list
    month_count = len(data) 
    print(f"Total months: {month_count}")
### Finding Total Profit ###
    total = sum(float(row[1]) for row in data)
    print(f"Total Profit/Loss: {total}")
## Finding Average Change ###
    # for row in data:
        
### Finding Max profit ###
    max_profit = max(float(row[1]) for row in data)
    max_month = ""
    for row in data:
        if row[1] == max_profit:
            max_month = row[0]
    print(f"Greatest increase in profits: {max_month} {max_profit}")
    ### Finding max loss ###
    max_loss = min(float(row[1]) for row in data) 
    print(f"Greatest loss in profits: {max_loss}")
    print("=================================")

### Writing to text file ###
    output_path = os.path.join("../Results/financial_analysis2.txt")
    with open(output_path, "w+", newline="") as data_file:
        lines = ["Financial Analysis \n", "================================= \n", f"Total months: {month_count} \n", f"Greatest increase in profits: {max_month} {max_profit}", f"Total Profit/Loss: {total} \n", f"Greatest loss in profits: {max_loss} \n", f"================================= \n"]
        data_file.writelines(lines) 

