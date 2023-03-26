# Part A (40 points) - file writing
import csv

def state_data(lst, filename, statecode):
    # lst is a nested list with each list [Area Name, 1-Bedroom, 2-Bedroom, State Code] index 1 and 2 are floats
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for record in lst:
            if record[3] == statecode:
                writer.writerow(record)

# state_data([ ], "empty.csv", "AL")
# state_data([["Montgomery", 702, 830, "AL"],["Anchourage, HUD Metro", 991, 1305, "AK"] ], "a.csv", "AK")

# Part B (20 points) - Working with JSON
import json

def process_inputs(jsonblob):
    data_list = json.loads(jsonblob)
    sum = 0
    for item in data_list:
        sum += item 
    retVal = {
        "number" : len(data_list),
        "added" : sum
    }
    return retVal

# print(process_inputs('[ 4, 1 ]'))
