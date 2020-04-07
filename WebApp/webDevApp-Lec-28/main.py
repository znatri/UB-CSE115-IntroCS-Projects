import bottle
import urllib.request
import json

# URL format: protocol://server/path?query_string
# AJAX Tutorial

@bottle.route("/")          # IMPORT Index  File
def html_file():
    html_file = bottle.static_file("index.html", root=".")
    return html_file

@bottle.route('/myCode.js') # Import JS File
def js_file():
    js_file = bottle.static_file("myCode.js", root=".")
    return js_file

@bottle.route('/style.css') # IMPORT CSS File
def css_file():
    css_file = bottle.static_file("style.css", root=".")
    return css_file

@bottle.route('/data')
def json_file():
    # response = '{"key": "JSON is just a str"}' 
    retVal = {} # make a dictionary
    retVal['length'] = 10 # assign some key-value pairs
    retVal['width'] = 8
    response = json.dumps(retVal) # convert to json.blob
    return response # send it over the server to client

bottle.run(host="localhost", port=8080, debug=True)