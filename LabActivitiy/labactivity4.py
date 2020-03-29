import math

# PART B

def smaller(lst1, lst2):
  retVal = []
  for i in range(len(lst1)):
    val1 = lst1[i]
    val2 = lst2[i]
    if val1 > val2 :
      retVal.append(val2)
    elif val2 > val1 :
      retVal.append(val1)
    else:
      retVal.append(val1)
  return retVal

# print(smaller([7],[6]))
# print(smaller([1,9,2],[4,8,2]))

# PART C

def dist(prev_x, prev_y, cur_coord):
    dist_x = prev_x - cur_coord[0]
    dist_y = prev_y - cur_coord[1]
    ret_val = math.sqrt((dist_x**2) + (dist_y ** 2))
    return ret_val

def race_distance(lst):
  totalDistance = 0
  prev_x = 0
  prev_y = 0
  current_coord = []
  for x in range(len(lst)):
    if x > 0 :
        prev_x = lst[x-1][0]
        prev_y = lst[x-1][1]
    current_coord = lst[x]
    totalDistance = totalDistance + dist(prev_x, prev_y, current_coord)
  return totalDistance

# race_distance([ ])  would evaluate to 0
# race_distance([[1,0]])  would evaluate to 1.0
# race_distance([[2, 5],[1, 4], [7, 9]])  would evaluate to approximately 14.609628


      