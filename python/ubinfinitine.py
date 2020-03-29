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

