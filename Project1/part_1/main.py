# CSE115LLR
# Project 1: Module 1
# Made by Hardik Goel
# Date: March 6, 2020
# Module 1 due date: March 13, 2020

# import data_file # import data set from data_file.py stored in same directory
import os

# data = data_file.data

def get_matches(lst_data, str_key, str_val):
    lst_dict = [] # empty list to store dict
    for i in lst_data: # loop to get each dict from sample data
        if i.get(str_key) == str_val:  # get func to call equivalent value for key and compare it to our val
            lst_dict.append(i) # if key and val match append the dict to lst
    return lst_dict

# print(get_matches(data,'police_district','District A'))

def list_descriptions(lst_data):
    lst_str = [] # empty list to hold strings
    for i in lst_data: # retrieves dictionaries
        if i.get('tow_description') not in lst_str: # checks if tow_description in dict exists in our list
            lst_str.append(i.get('tow_description'))
    return lst_str
    
# print(list_descriptions(data))

def count_by_month(lst_data):
    raw_data = [] # stores all  months (raw data)
    lst_months_count = [] # stores no. of cars towed every month in chronological order (final output)
    for i in lst_data: # iterates over every dictionary to capture towdate, extracts month of tow from string and append to the raw data list
        val = i.get('tow_date') # captures date as a string
        month = int(val[5]+val[6]) # extracts month from the string
        raw_data.append(month) # appends month to list
    for i in range(1, 13): # starts from january till december (1 through 12), also 0 is not a month 13 is not included (Endpoint)
        val = raw_data.count(i) # captures no. of tow in every month by counting no. of months
        lst_months_count.append(val) # appends no. of tow every monnth to a list in chronological order
    return lst_months_count
    

# print(count_by_month(data))

def count_by_day(lst_data):
    raw_data = [] # stores all dates
    lst_day_count = [] # counts all tows on particular dates and appends chornologically from 1 to 31   
    for i in lst_data: # iterates over every dictionary to capture towdate
        val = i.get('tow_date') # captures date as a string
        date = int(val[8]+val[9]) # extracts day from the string
        raw_data.append(date) # appends day to list
    for i in range(1, 32): # starts from 1 till 31
        val = raw_data.count(i) # captures no. of tow on each day
        lst_day_count.append(val) # appends no. of tow every day to a list in chronological order
    return lst_day_count

# print(count_by_day(data))