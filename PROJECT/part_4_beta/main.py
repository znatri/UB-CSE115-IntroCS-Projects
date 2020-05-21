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


def load_data():
    csv_file = 'cached_data.csv'
    if not os.path.isfile(csv_file):
        query_str = "?$limit=10000"
        url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
        data = cache.get_data(url)
        data = cache.minimize_dictionaries(
            data, ['tow_date', 'tow_description', 'police_district'])
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

    y_val = backend.count_by_day(data)  # no. of tows on each day
    x_val = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
    ]

    trace = [{"x": x_val, "y": y_val, "mode": "markers", "type": "scatter"}]

    layout = {
        'title': "Tows by Day of the Month",
        'xaxis': {
            "title": "Day of the Month"
        },
        'yaxis': {
            "title": "# Tows"
        }
    }

    json_data = {'trace': trace, 'layout': layout, 'plot': 'plot-scatter'}

    json_blob = json.dumps(json_data)
    print("\nSharing # Tows by Day...")
    return json_blob


@bottle.route('/pie_chart')
# police districts responsible for tows
def district_data():
    data = readCSV()
    districtCount = {}

    for i in data:  # retrieves dictionaries
        district = i.get('police_district')
        if district not in districtCount:  # checks if tow_description in dict exists in our list
            districtCount[district] = 1
        else:
            districtCount[district] += 1

    label_list = []
    values_list = []

    for (key, value) in districtCount.items():
        label_list.append(key)
        values_list.append(value)

    trace = [{"values": values_list, "labels": label_list, "type": "pie"}]

    layout = {"title": "Tows by District"}

    json_data = {'trace': trace, 'layout': layout, 'plot': 'plot-pie'}

    json_blob = json.dumps(json_data)
    print("\nSharing % Tows by District...")
    return json_blob


@bottle.route('/line_plot')
# cars were towed and how those reasons change
def tow_by_description():
    data = readCSV()
    tow_description = backend.list_descriptions(data)
    month_count = {}
    for item in tow_description:
        sorted_data = backend.get_matches(data, 'tow_description', item)
        month_count[item] = backend.count_by_month(sorted_data)

    data = []
    x_val = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
        'Nov', 'Dec'
    ]

    for (key, value) in month_count.items():
        trace = {
            "x": x_val,
            "y": value,
            "type": 'scatter',
            "mode": 'lines',
            "name": key
        }
        data.append(trace)

    layout = {
        'title': 'Tows by Month and Description',
        'xaxis': {
            "title": "Month"
        },
        'yaxis': {
            "title": "# Tows"
        }
    }

    json_data = {'trace': data, 'layout': layout, 'plot': 'plot-line'}

    json_blob = json.dumps(json_data)
    print("\nSharing # Tow Description by Month...")
    return json_blob


load_data()
bottle.run(host="0.0.0.0", port=8080, debug=True)
