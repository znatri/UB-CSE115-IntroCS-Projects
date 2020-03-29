# WORKING WITH TXT & CSV FILES

import csv
import re

def read_budget_method1(filename):
    retVal = {}
    with open(filename, 'r', newline='') as f: 
        reader = csv.reader(f)  
        headerRow = True
        for line in reader:
            if not headerRow:
                month = line[0]
                val = [line[1], line[2]]
                retVal[month] = val
            headerRow = False      
    return retVal

def read_budget_method2(filename):
    retVal = {}
    with open(filename, 'r' ,newline='') as f: 
        reader = csv.reader(f) # turns file into object
        # next function skips the first (ith element) from file *see definition 
        header = next(reader)
        for line in reader: # gets list from object
            month = line[0]
            val = [int(line[1]), int(line[2])]
            retVal[month] = val       
    return retVal

# Call csv.writer
# To write a record to a csv file use .writerow 
def writeCSV(filename, seq):
    with open(filename, 'w') as f:
        writer = csv.writer(f) # converts file into object
        for record in seq: # gets list from list (nested list)
            writer.writerow(record) #

dt = [ ['abc', 'def'] , ['ghij', 'klmn'] ]
# writeCSV('file1.csv',dt)
# writeCSV('file1.txt',dt[0])
# writeCSV('file1',dt[1])

def retirw_vsc(filename):
    # make a newfile name with R in front
    newFilename = "R"+filename

    # variable to hold initial csv records in a nested list
    seq = []

    # retrieving records from filename into seq list
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            seq.insert(0, line) # adds the latest to the first index

    # reverse order of seq to reversedSeq list
    # reversedSeq = []
    # for x in range(len(seq)):
    #     reversedSeq.append(seq.pop())

    # writing in newFilename in reverse order 
    with open(newFilename, 'w') as f:
        writer = csv.writer(f)
        for record in seq:
            writer.writerow(record)

# retirw_vsc("file1.csv")

def csv_sum(csvfile):
    sum = 0
    seqList = []
    
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            seqList.append(int(record[1]))

    for x in seqList:
        sum += x
    return sum

# print(csv_sum("ubinf.csv"))

def csv_to_list(filename):
    seqList = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            seqList.append(int(record[2]))
    return seqList

def csv_average(filename):
    seqList = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            seqList.append(int(record[1]))
    sum = 0
    for x in seqList:
        sum += x
    average = sum/len(seqList)
    return average

def total_population(csvfielname, citylist):
    seq = []
    sum = 0
    with open(csvfielname, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            for city in citylist:
                if city[0] == record[0] and city[1] == record[1] and city[2] == city[2]:
                    seq.append(record[3])

    for item in seq:
        sum = sum + int(item) 

    return sum

data = [['au', 'port lincoln', '05'], ['jp', 'mobara', '04'], ['in', 'bahua', '36'], ['us', 'altamonte springs', 'FL']]

# print(total_population("worldcitiespop.txt", data))

def average_rating(csvfile, ytid):
    ratings = []
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            if record[0] == ytid:
                ratings.append(record[3])
    sum = 0
    for rating in ratings:
        sum += int(rating)
    
    averagerating = sum/len(ratings)
    return averagerating
