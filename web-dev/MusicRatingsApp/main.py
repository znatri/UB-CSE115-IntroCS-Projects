import json
import bottle
import ratings

@bottle.route('/')
def index():
  return bottle.static_file("index.html", root="client/")

@bottle.route('/<js_file>.js')
def javascript_file(js_file):
  print("Getting JavaScript file: " + js_file)
  code_js = bottle.static_file(js_file+".js", root="client/")
  return code_js

def json_song_data() :
  song_list = ratings.get_songs()
  ret_val = json.dumps(song_list)
  return ret_val

@bottle.route('/songs')
def get_songs():
  ret_val = json_song_data()
  return ret_val

@bottle.post('/add_song')
def add_song():
  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  ratings.add_song(content)
  ret_val = json_song_data()
  return ret_val

@bottle.post('/rate_song')
def rate_song():
  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  ratings.rate_song(content)
  ret_val = json_song_data()
  return ret_val

bottle.run(host="0.0.0.0", port=8080, quiet=True)