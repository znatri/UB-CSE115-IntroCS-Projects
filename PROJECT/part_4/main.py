# CSE115LLRA Computer Science I:220110202
# Project 1: Module 4
# Made by Hardik Goel
# Date Started: April 22, 2020
# Module 4 due date: May 1, 2020

import bottle
import json
import cache
import backend
import os.path

def load_data( ):
  csv_file = 'cached_data.csv'
  if not os.path.isfile(csv_file):
    query_str = "?$limit=10000"
    url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
    data = cache.get_data(url)
    data = cache.minimize_dictionaries(data, ['tow_date', 'tow_description', 'police_district'])
    cache.write_cache(data, csv_file)

@bottle.route('/')
def load_html():
    return bottle.static_file("index.html", root=".")

def readCSV():
    data = cache.read_cache("cached_data.csv")
    return data

@bottle.route('/script.js')
def load_js():
    print("Sharing JavsScript File...")
    return bottle.static_file("script.js", root=".")

@bottle.route('/scatter_plot')
# tows on each day of the month
def tows_by_day():
    data = readCSV()
    json_data = backend.count_by_day(data) # no. of tows on each day 
    json_blob = json.dumps(json_data)
    print("\nSharing # Tows by Day...")
    return json_blob

@bottle.route('/pie_chart')
# police districts responsible for tows
def district_data():
    data = readCSV()
    districtCount = {}
    for i in data: # retrieves dictionaries
        if i.get('police_district') not in districtCount: # checks if tow_description in dict exists in our list
            districtCount[i.get('police_district')] = 1
        else:
            districtCount[i.get('police_district')] += 1
    json_blob = json.dumps(districtCount)
    print("\nSharing % Tows by District...")
    return json_blob

@bottle.route('/line_plot')
# cars were towed and how those reasons change
def tow_by_description():
    data = readCSV()
    tow_description = backend.list_descriptions(data)
    json_data = {}
    for item in tow_description:
        sorted_data = backend.get_matches(data, 'tow_description', item)
        json_data[item] = backend.count_by_month(sorted_data)
    json_blob = json.dumps(json_data)
    print("\nSharing # Tow Description by Month...")
    return json_blob

load_data()
bottle.run(host="0.0.0.0", port=8080, debug=True)