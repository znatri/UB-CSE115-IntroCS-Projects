import bottle 
import json
import chat

@bottle.route('/')
def send_HTML():
    response = bottle.static_file('index.html', root=".")
    return response

@bottle.route('/chat.js')
def send_JS():
    response = bottle.static_file("chat.js", root=".")
    return response

@bottle.route('/ajax.js')
def ajax_file():
    response = bottle.static_file("ajax.js", root=".")
    return response

@bottle.route('/chat')
def send_chat():
    messages = chat.get_chat()
    return messages

@bottle.post('/send')
def recieve_chat():
    content = bottle.request.body.read().decode() # get json blob 
    content = json.loads(content)
    chat.add_message(content['message']) # add incoming message to chat log
    return send_chat() # send current chat to user

bottle.run(host="localhost", port=8080, debug=True)