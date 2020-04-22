# CSE115LLRA Computer Science I:220110202
# Project 1: Module 4
# Made by Hardik Goel
# Date Started: April 22, 2020
# Module 4 due date: May 1, 2020

####### Note #########
# I modified count_by_month() to make it work with line_plot by adding one more parameter tow_description
# I couldn't find any other way if any
# Never the less the code works fine

import bottle
import json
import cache
import backend

@bottle.route('/')
def load_html():
    return bottle.static_file("index.html", root="client/")

@bottle.route('/ajax.js')
def load_ajax():
    print("Retrieveing AJAX File")
    return bottle.static_file("ajax.js", root="client/")

@bottle.route('/script.js')
def load_js():
    print("Retrieveing SCRIPT File")
    return bottle.static_file("script.js", root="client/")

@bottle.route('/scatter_plot')
# tows on each day of the month
def tows_by_day():
    data = cache.read_cache("cached_data.csv")
    y_val = backend.count_by_day(data) # no. of tows on each day 
    x_val = [] # holds all dates corrosponding to no. of tows (y_val)
    for i in range(1, 32):
      x_val.append(i)
    json_data = {
      'x': x_val,
      'y': y_val,
    }
    json_blob = json.dumps(json_data)
    return json_blob

@bottle.route('/pie_chart')
# police districts were responsible for tows
def district_data():
    data = cache.read_cache("cached_data.csv")
    districtCount = {}
    for i in data: # retrieves dictionaries
        if i.get('police_district') not in districtCount: # checks if tow_description in dict exists in our list
            districtCount[i.get('police_district')] = 1
        else:
            districtCount[i.get('police_district')] += 1
    json_blob = json.dumps(districtCount)
    return json_blob

@bottle.route('/line_plot')
# cars were towed and how those reasons change
def tow_by_description():
    data = cache.read_cache("cached_data.csv")
    tow_description = backend.list_descriptions(data)
    json_data = {}
    for item in tow_description:
       json_data[item] = backend.count_by_month(data, item)
    json_blob = json.dumps(json_data)
    return json_blob


import os.path

def load_data( ):
  csv_file = 'cached_data.csv'
  if not os.path.isfile(csv_file):
    query_str = "?$limit=10000"
    url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
    data = cache.get_data(url)
    data = cache.minimize_dictionaries(data, ['tow_date', 'tow_description', 'police_district'])
    cache.write_cache(data, csv_file)

load_data()
bottle.run(host="0.0.0.0", port=8080, debug=True)