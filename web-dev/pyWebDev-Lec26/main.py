import urllib.request

# Retrieving Content from an HTML page (unstructured data)
url = "https://engineering.buffalo.edu/"
url += "computer-science-engineering.html"
response = urllib.request.urlopen(url) # opens a URL whose content we want
content = response.read().decode() # converts page to a usable str

# print(content)

with open("index.html", 'w') as f:
    f.write(content) 

# Web APIs : Retrieving Structured Data from Webpages in JSON.BLOBs
url2 = "http://api.open-notify.org/iss-now.json" # international space station locator
response2 = urllib.request.urlopen(url2)
content2 = response2.read().decode()

# print(content2)

with open("data.json", 'w') as f:
    f.write(content2)