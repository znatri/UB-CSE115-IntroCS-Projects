from bottle import route, run

@route('/')
def indexPage():
    response = "<html><body><p>"
    response += "Hello from server!"
    response += "</p></body></html>"
    return response

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)