# Part C (20 points) - Working with dictionaries

def balance(dictObj, num):
  sum = 0
  for val in dictObj.values():
    if val > num:
      sum = sum + val
  return sum

# print(balance({'jody':1,'pat':91,'kelly':100,'corey':89}, 90))
# print(balance({'jody':1,'pat':89,'kelly':13}, 90))