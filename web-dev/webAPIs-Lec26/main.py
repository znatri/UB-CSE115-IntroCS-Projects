import urllib.request
import json

url = "http://api.open-notify.org/iss-now.json" # international space station locator
response = urllib.request.urlopen(url)
content_string = response.read().decode()
content = json.loads(content_string)

for key in content.keys():
    print(key + ": " + str(content[key]))
 
# time = content['timestamp'] / 1000
