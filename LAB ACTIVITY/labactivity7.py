# Part A (2 points) - basic Python sorting
def sortIt(listArr):
  listArr.sort()

# empty_list=[ ]
# sortIt(empty_list)      # emptyList will still have the value [ ]
# print(empty_list)

# test_list=[5, -10, 2, -2, 0]
# sortIt(test_list)      # testList will have the value [ -10, -2, 0, 2, 5 ]
# print(test_list)

# Part C (5 points) - Python key selector & custom sorting functions

def shooting_pct(kv):
    attempts = kv.get("shot attempts")
    shots = kv.get("shots made")
    val = shots/attempts
    return val

# shooting_pct({"shot attempts" : 10, "shots made": 5, "minutes": 42}) # would evaluate to 0.5
# shooting_pct({"shot attempts" : 1, "shots made": 1, "minutes": 2}) # would evaluate to 1.0

def shooting_sort(lstArr):
    lstArr.sort(key=shooting_pct)

# nba = [ {"shot attempts" : 184, "shots made": 130, "minutes": 681},
#         {"shot attempts" : 635, "shots made": 271, "minutes": 1059} ]

# shooting_sort(nba) # the order of nba's entries will now be reversed.
# print(nba)
