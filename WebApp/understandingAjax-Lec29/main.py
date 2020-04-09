import bottle 
import json

@bottle.route('/content')
def html_file():
    response = bottle.static_file('index.html', root=".")
    return response

@bottle.route('myCode.js')
def js_file():
    response = bottle.static_file("myCode.js", root=".")
    return response

@bottle.route('/static_data')
def data_served():
    response = {"key": "JSON is just a str"}
    jsonblob = json.dumps(response)
    return jsonblob

bottle.run(host="localhost", port=8080, debug=True)