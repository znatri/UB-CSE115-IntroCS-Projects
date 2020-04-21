# def indexed_list(x):
#     index = len(x)
#     newlist = []
#     for i in range(index):
#         newlist.append(i)
#     return newlist

# indexed_list(['1', '2', '3', '4', '5'])

# def compute_xp(x, boo):
#     if boo == False:
#         return 89397
#     elif boo == True:
#         return 89397+x

# print(compute_xp(10, True))

# def print_list(x):
#     num = len(x)
#     for i in range(0, num):
#         print(f'{x[i]}')
#         print('{}'.format(x[i]))

# print_list(['Hi', 'my', 'name', 'is', 'God'])

# def find_value(x):
#     if 7 in x:
#         print('True')
#         return True
#     else:
#         print('False')
#         return False
        
# find_value([1, 2, 3, 4, 5, 6, 7])
# find_value([1, 2, 4, 5])

# def add_value(x):
#     x.append(10)
#     print(x)

# add_value([1, 2, 3, 4, 5])

# def count_values(x):
#     num = 0
#     length = len(x)
#     for i in range(length):
#         if x[i] > 542:
#             num = num + 1
#     print(num)
#     return num

# count_values([100, 700, 542, 600])

# def get_size(kv):
#     return len(kv)

# kv = {
#     'obj1' : 1,
#     'obj2' : 2,
#     'obj3' : 3,
# }

# def print_values(kv):
#     for key in kv:
#         print(kv.get(key))

# print_values(kv)

# def find_value(kv):
#     for key in kv:
#         if kv.get(key) == 9:
#             return True
#     return False

# kv1 = {
#     'obj1' : 1,
#     'obj2' : 2,
#     'obj3' : 9,
# }

# kv2 = {
#     'obj1' : 1,
#     'obj2' : 2,
#     'obj3' : 3,
# }

# print(find_value(kv1))
# print(find_value(kv2))

# def count_large(kv):
#     count = 0
#     for key in kv:
#         if kv.get(key) > 52.1:
#             count += 1
#     return count

# kv2 = {
#     'obj1' : 1,
#     'obj2' : 70,
#     'obj3' : 52.1,
# }

# print(count_large(kv2))

# def count_lines(filetxt):
#     count = 0
#     with open(filetxt) as f:
#         for line in f:
#             count += 1       
#     return count

# def sum_ints():
#     sum = 0
#     with open("organization.txt") as f:
#         for line in f:
#             sum += int(line)
#     return sum

# def file_to_int_list():
#     retVal = []
#     with open("mess.txt") as f:
#         for line in f:
#             retVal.append(int(line))
#     return retVal

# def csv_sum(csvfile):
#     sum = 0
#     seqList = []
    
#     with open(csvfile, 'r') as f:
#         reader = csv.reader(f)
#         for record in reader:
#             seqList.append(record)

#     valList = []

#     for x in seqList:
#         valList.append(x[2])

#     for x in valList:
#         sum += int(x)
#     return sum

# print(csv_sum("ubinf.csv"))

# # JSON (due week of Apr. 13)
# import json
# import urllib.request

# def to_json(val):
#     retVal = json.dumps(val)
#     return retVal

# def read_json(val):
#     retVal = json.loads(val)
#     return retVal

# def get_y(jsonblob):
#     dictObj = json.loads(jsonblob)
#     pos = dictObj['x'].index(-6) # index of item where x == -6
#     retVal = dictObj['y'][pos] # corrosponding y coord when x == -6
#     return retVal

# def get_value(jsonblob):
#     dictObj = json.loads(jsonblob)
#     val = dictObj.get("attack")
#     return val

# def json_average(jsonblob):
#     lst = json.loads(jsonblob) # list of objects [{}, {}, {}, ..., {}]
#     total = 0
#     count = len(lst)
#     for dictObj in lst:
#         total += dictObj.get("velocity")
#     val = total/count
#     retVal = {"velocity": val}
#     retVal = json.dumps(retVal)
#     return retVal

# def json_filter(jsonblob):
#     lst = json.loads(jsonblob)
#     newLst = []
#     for dictObj in lst:
#         velocity = dictObj.get("velocity")
#         if velocity > 33.28:
#             newLst.append(dictObj)
#     newLst = json.dumps(newLst)
#     return newLst

# HTTP Requests (due week of Apr. 13)

# import urllib.request
# import json

# def get_response():
#     url = "https://fury.cse.buffalo.edu/ps-api/r/patent"
#     data = urllib.request.urlopen(url)
#     strin = data.read().decode()
#     return strin

# print(get_response())

# def variable_get(val):
#     url = "https://fury.cse.buffalo.edu/ps-api/r/" + val
#     data = urllib.request.urlopen(url)
#     content = data.read().decode()
#     return content

# print(variable_get("patent"))

# def query_string():
#     url = "https://fury.cse.buffalo.edu/ps-api/a?x=3&y=5&z=0"
#     response = urllib.request.urlopen(url)
#     content_string = response.read().decode()
#     content = json.loads(content_string)
#     retVal = content.get("answer")
#     return retVal
    
# def query_dict(kv):
#     query = "?"
#     for key, value in kv.items():
#         query += key + "=" + str(value) + "&"
#     query = query[:-1] # remove last '&' from string
#     url = "https://fury.cse.buffalo.edu/ps-api/a" + query
#     response = urllib.request.urlopen(url)
#     content_string = response.read().decode()
#     content = json.loads(content_string)
#     retVal = content.get("answer")
#     return retVal
    
# def flu_season():
#   # https://www.flutrack.org
#   url = "https://fury.cse.buffalo.edu/ps-api/flutrack?time=3" # list of flu tweets over past 3 days
#   response = urllib.request.urlopen(url)
#   content_string = response.read().decode()
#   content = json.loads(content_string)
#   num = len(content) # number of tweet
#   return num

# print(flu_season())


# Custom Sorting (due week of Apr. 20)

# def sort_by_average_rating(moviesList):
#     moviesList.sort(key=ratings)
    
# def ratings(movie):
#     ratingsList = movie.get("ratings")
#     count = 0
#     for rating in ratingsList:
#         count += rating
#     avgRating = count / len(ratingsList)
#     return avgRating
