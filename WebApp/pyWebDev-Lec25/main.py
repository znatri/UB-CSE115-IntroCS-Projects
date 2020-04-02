from bottle import route, run, static_file

@route('/')
def indexPage():
    response = "<html><body><p>"
    response += "Hello from server!"
    response += "</p></body></html>"
    return response

@route('/hello')
def hello():
    return "Hello World!"

@route('/simple.html')
def myFunc1():
    response = static_file("simple.html", root=".") # use static_file to load page content from a file
    return response

@route('/myCode.js')
def myFunc2():
    response = static_file("frontend.js", root=".")
    return response

run(host='localhost', port=8080, debug=True)

