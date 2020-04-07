# URL format: protocol://server/path?query_string
# AJAX Tutorial

import bottle
import json

quote_str = '"'

@bottle.route('/')
def index():
  html_file = bottle.static_file("index.html", root=".")
  return html_file

@bottle.route('/chat.js')
def static():
  js_file = bottle.static_file("chat.js", root=".")
  return js_file

@bottle.route('/ajax.js')
def javascript():
  js_file = bottle.static_file("ajax.js", root=".")
  return js_file

@bottle.route('/chat')
def get_chat():
  response = {"something" : "For Wednesday"}
  #print("Sending text: " + response)
  json_blob = json.dumps(response)
  print("Sending as JSON: " + json_blob)
  return json_blob

@bottle.post('/send')
def do_chat():
  content = bottle.request.body.read()
  json_content = content.decode()
  print("Server received blob: " + json_content)
  good_content = json.loads(content)
  print("Blob became: " + good_content)

  if good_content.find("Python") != -1 :
    message = "That is server talk"
  elif good_content.find("JavaScript") != -1 :
    message = "That is browser talk"
  else :
    message = "Boring"

  #json_blob = quote_str + message + quote_str
  json_blob = json.dumps(message)
  print("Sent message:" + json_blob)
  return json_blob

print("Anything printed was run on repl.it")
# Setting quiet=True eliminates output from bottle library
bottle.run(host="0.0.0.0", port=8080)