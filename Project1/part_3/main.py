# CSE115LLRA Computer Science I:220110202
# Project 1: Module 3
# Made by Hardik Goel
# Date Started: March 19, 2020
# Module 3 due date: April 6, 2020

import json
import urllib.request

def get_data(url): # url = link to json file
    response = urllib.request.urlopen(url) # Gets the HTML Code
    jsonblob = response.read().decode() # Reads the HTML Code to get JSON String
    content = json.loads(jsonblob) # Converts JSON String into usable Python Data
    return content

# Testing Code for get_data()
# url = "https://cse.buffalo.edu/~mhertz/courses/cse115/projects/mediumFile.json"
# print(get_data(url))
# data = get_data(url)

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