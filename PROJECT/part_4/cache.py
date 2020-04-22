import csv
import urllib.request

###############
# PART 2 Code #
###############

def read_csv_header(reader):
    for record in reader:
        return record

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

def write_dictionaries_to_csv(writer, dictLst, lstKeys):
    data = []
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

###############
# PART 3 Code #
###############

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
