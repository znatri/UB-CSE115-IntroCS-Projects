# Part A (7 points) - writing text files

def list_2_file(filename, lst):
  with open(filename, 'w') as f:
    for item in lst:
      f.write(item+'\n')

# list_2_file("simple.txt", ["Write", "me"])
# list_2_file("simple.txt", ["Write", "me"])

# Part B (4 points) - writing CSV files

import csv

def low_rent(lst, csvfile):
  # lst = [[State Code, MedianEfficiencyRent, Area Name]]
  with open(csvfile, 'a') as f:
    writer = csv.writer(f)
    for item in lst: 
      if item[1] < 576:
        writer.writerow(item)
        
low_rent([ ["NY", 603.0, "Cayuga County, NY"], ["AR", 410.0, "Sevier County"] ], "a.csv")
