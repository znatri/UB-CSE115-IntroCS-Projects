import re
import csv

var = "chapt.txt"

# with open(var) as f:
#     for line in f:
#         line = line.rstrip('\r\n')
#         print(line)

# open('filename.extension', 'mode', newline = '')
# newline = '' is not required, it's '' by default
# 'r' is for read mode (Can be omitted, will be chosen by default)
# 'w' is writing mode (erases an existing file)
# 'a' appending mode (appends to last)
# f = open('filename.txt', 'w')

def word_count(filename):
    retVal = {}

    with open(filename) as f:
        for line in f:
            wordlist = re.split("[^A-Za-z]+", line)
            for word in wordlist:
                if word in retVal:
                    val = retVal.get("word", 0)
                    retVal[word] = val + 1

    return retVal

# fileObj.write() to print a str to a file in writing or appending mode
# write() requires a str argument
# to print a integer in a file use str() to convert it to a string first
# f.write(str(7))
def write(filename, contents):
    with open(filename, 'w') as f:
        for items in contents:
            f.write(items+'\n')
