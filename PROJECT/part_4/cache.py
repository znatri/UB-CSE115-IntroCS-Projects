import csv
import json
import urllib.request

###############
# PART 2 Code #
###############

def read_csv_header(reader):
    for record in reader:
        return record

def read_data(reader, listKeys):
    retVal = []
    for record in reader:
        object = {} 
        for i in range(len(listKeys)): 
            key = listKeys[i]
            value = record[i]
            object[key] = value
        retVal.append(object)
    return retVal

def write_csv_header(writer, object):
    writer.writerow(object.keys())

def write_dictionaries_to_csv(writer, objectList, lstKeys):
    data = []
    for object in objectList:
        record = []
        for key in lstKeys:
            if key in object:
                value = object.get(key)
                record.append(value)
        data.append(record)
    for record in data:
        writer.writerow(record)

###############
# PART 3 Code #
###############

def get_data(url):
    response = urllib.request.urlopen(url)
    jsonblob = response.read().decode()
    content = json.loads(jsonblob)
    return content

def minimize_dictionaries(dictList, keyList):
    newList = []
    for dictObj in dictList:
        newDict = {}
        for key in keyList:
            newDict[key] = dictObj.get(key, 'District A')
        newList.append(newDict)
    return newList

def write_cache(dictList, filename):
    header = dictList[0].keys()
    recordsList = []
    for dictObj in dictList:
        record = []
        for val in dictObj.values():
            record.append(val)
        recordsList.append(record)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(recordsList)

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
                dictList.append(newDict)
    return dictList

