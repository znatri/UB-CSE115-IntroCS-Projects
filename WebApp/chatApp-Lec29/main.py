import bottle 
import json

@bottle.route('/')
def html_file():
    response = bottle.static_file('index.html', root=".")
    return response

@bottle.route('/chat.js')
def js_file():
    response = bottle.static_file("chat.js", root=".")
    return response

@bottle.route('/ajax.js')
def ajax_file():
    response = bottle.static_file("ajax.js", root=".")
    return response

@bottle.route('/static_data')
def data_served():
    response = {"key": "JSON is just a str"}
    jsonblob = json.dumps(response)
    return jsonblob

bottle.run(host="localhost", port=8080, debug=True)