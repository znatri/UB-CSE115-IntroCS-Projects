# CSE115LLR
# Project 1: Module 2
# Made by Hardik Goel
# Date: March 9, 2020
# Module 2 due date: March 27, 2020

# dictObj is a single dictionary/object 
# lstKeys is a list of keys
# dictLst is list of dictionaries

import csv

def read_csv_header(reader):
    # retVal = []
    # header = True
    for record in reader:
        # if header == True:
            # retVal = record
        return record
        # header = False
    # return retVal

def read_data(reader, lstKeys):
    retVal = [] # lst of dictionaries [{}, {}, ..., {}]
    for record in reader:
        dictObj = {} # holds key-value pairs extracted from parameter list and csv file
        for i in range(len(lstKeys)): # go through each key in keylist and retrieve value from record
            key = lstKeys[i]
            value = record[i] # extract the value from list from the corrosponding column
            dictObj[key] = value
        retVal.append(dictObj)
    return retVal

def write_csv_header(writer, dictObj):
    writer.writerow(dictObj.keys())
    # header = []
    # for key in dictObj.keys():
    #     header.append(key)
    # writer.writerow(header)

def write_dictionaries_to_csv(writer, dictLst, lstKeys):
    data = []
    # for dictObj, key in zip(dictLst, lstKeys):
    for dictObj in dictLst:
        record = []
        for key in lstKeys:
            if key in dictObj:
                value = dictObj.get(key)
                record.append(value)
        data.append(record)
    for record in data:
        writer.writerow(record)


# sampleData = [{'tow_reason': 'IL', 'tow_date': '2013-06-18'}, {'tow_date': '2014-09-25', 'tow_reason': 'GA'}]
# writerfilename = "output.csv"
# with open(writerfilename, 'w') as f:
#     csv_w = csv.writer(f)
#     write_csv_header(csv_w, {'tow_date': '2020-01-20', 'tow_reason': 'AB'})
#     write_dictionaries_to_csv(csv_w, sampleData,['tow_reason','tow_date'])

# readerfilename = "mediumDataFile.csv"
# with open(readerfilename) as f:
#     csv_r = csv.reader(f)
#     lst_header = read_csv_header(csv_r)
#     print(read_data(csv_r, lst_header))