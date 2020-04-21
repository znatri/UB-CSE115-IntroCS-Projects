# Lists
# a = ['car', 'bike', 'boat'] # Index starts from 0
# length = 0

# print("Printing list...")
# for x in a:
#     print(x.upper())
#     length += len(x)
# print('Done!')

# print(f'Length of string: {length}')

# def implode(x):
#   li = ''
#   for i in x:
#     li = li + i
#   print(li)

# implode(['a','b','c'])

# def explode(x):
#   li = []
#   for i in x:
#     li.append(i)
#   print(li)

# explode('abc')

# def square(x):
#     newlist = []
#     for i in x:
#         newlist.append(i**2)
#     print(newlist)

# square([1,2,3,4,5])
# square([-1])
# square()

# def keep_long_strings(lst):
#     newlist = []
#     for i in lst:
#         if len(i) > 4:
#             newlist.append(i)
#     print(newlist)

# keep_long_strings(['abc','avcde','a','abcdef'])

# def countMappings(x, val):
#     count = 0
#     for key in x.keys(): # //dictionary//.keys() return all the keys 
#         if x.get(key) == val:
#             count += 1
#     return count

# lst = {'obj1' : 'a', 'obj2' : 'b', 'obj3' : 'c', 'obj4' : 'a'}
# print(countMappings(lst, 'a'))

# lst = {'obj1' : 'k', 'obj2' : 'b', 'obj3' : 'c'}
# print(countMappings(lst, 'a'))

# lst = {}
# print(countMappings(lst, 'a'))

