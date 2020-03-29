import csv

# Part A (7 points) - reading text files

def file_2_list(filename):
  retVal = []
  with open(filename, 'r') as f:
    for line in f:
      line = line.rstrip('\r\n')
      retVal.append(line)
  return retVal

def count_greater(filename, num):
  count = 0
  with open(filename, 'r') as f:
    for line in f:
      val = float(line)
      if val > num:
        count = count + 1
  return count

# Part B (4 points) - reading CSV files

def state_high(filename):
  retVal = {}
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    for record in reader:
      statecode = record[6]
      median = float(record[1])
      if statecode not in retVal.keys():
        retVal[statecode] = median
      else:
        current_median = retVal.get(statecode)
        if median > current_median:
          retVal[statecode] = median
  return retVal

# Part C (4 points) - advanced file reading

def max_diffs(txtfile, csvfile):
  retVal = {}
  statelst = []
  with open(txtfile, 'r') as f:
    for line in f:
      line = line.rstrip('\r\n')
      statelst.append(line)
  for i in range(len(statelst)):
    statecode = statelst[i]
    retVal[statecode] = 0
  with open(csvfile, 'r') as f:
    reader = csv.reader(f)
    for record in reader:
      statecode = record[6]
      diff = float(record[5]) - float(record[1]) # $4bedroom - $efficiency
      current_diff = retVal.get(statecode)
      if statecode in statelst and diff > current_diff:
        retVal[statecode] = diff
  return retVal
