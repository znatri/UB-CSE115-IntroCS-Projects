# CSE115LLRA Computer Science I:220110202
# Project 1: Module 3
# Made by Hardik Goel
# Date Started: March 19, 2020
# Module 3 due date: April 6, 2020

import json
import urllib.request
import csv

def get_data(url): # url = link to json file
    response = urllib.request.urlopen(url) # Gets the HTML Code
    jsonblob = response.read().decode() # Reads the HTML Code to get JSON String
    content = json.loads(jsonblob) # Converts JSON String into usable Python Data
    return content

# Testing Code for get_data()
# url = "https://cse.buffalo.edu/~mhertz/courses/cse115/projects/mediumFile.json"
# print(get_data(url))

def minimize_dictionaries(dictList, keyList):
    newList = []
    for dictObj in dictList:
        newDict = {}
        for key in keyList:
            newDict[key] = dictObj.get(key)
        newList.append(newDict)
    return newList
        
# Testing Code for minimize_dictionaries()
# dl = [{'tow_date': '2020-01-20', 'tow_reason': 'AB', 'state': 'NY'},
#        {'city': 'NYC', 'tow_reason': 'ST', 'tow_date': '2015-09-20'}]
# print(minimize_dictionaries(dl, ['tow_reason','tow_date']))

def write_cache(dictList, filename):
    # write a csv file with values of dictionaries
    # csv file should have a header which represent the columns, each column is a key in dictionary
    header = dictList[0].keys() # capture all the keys for header
    recordsList = [] # stores all the records for csv file
    for dictObj in dictList:
        record = []
        for val in dictObj.values():
            record.append(val)
        recordsList.append(record)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header) # write header
        writer.writerows(recordsList) # write records from recordsList

# Testing Code for write_cache()
# url = "https://cse.buffalo.edu/~mhertz/courses/cse115/projects/mediumFile.json"
# data = get_data(url)
# obj = minimize_dictionaries(data, ['tow_reason','tow_date', 'state'])
# write_cache(obj, "testingFile.csv")

def read_cache(filename):
    dictList = []
    keys = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = True
        for record in reader:
            if header == True:
                keys = record
                header = False
            else:
                newDict = {}
                for key, val in zip(keys, record): 
                    newDict[key] = val 
                # for i in range(len(keys)):
                    # newDict[keys[i]] = record[i]
                dictList.append(newDict)
    return dictList

# Testing Code for read_cache()
# print(read_cache('sample.csv'))
# print(read_cache('testingFile.csv'))
