# CSE115LLRA Computer Science I:220110202
# Project 1: Module 4
# Made by Hardik Goel
# Date Started: April 22, 2020
# Module 4 due date: May 1, 2020

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
    y_val = backend.count_by_day(data)
    x_val = []
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
    pass

@bottle.route('/line_plot')
# cars were towed and how those reasons change
def tow_description():
    pass


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
bottle.run(host="localhost", port=8080, debug=True)