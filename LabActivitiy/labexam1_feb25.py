# Made by Harik Goel  
# CSE 115 Lab Exam 1
# Date: 25 Feburary 2020
# Time: 2:00 - 2:50

# PART A Inititated

def rgb_to_color(r,g, b):
  color = (65536*r) + (256*g) + b
  return color

# print(rgb_to_color(0, 2, 5)) 
# print(rgb_to_color(123, 10, 7)) 

# PART A Finished

# PART B Inititated

def small_enough(x, a):
  if x > len(a):
    return True
  else:
    return False

# print(small_enough(10, '502s')) 
# print(small_enough(4, 'long'))

# PART B Finished

# PART C Inititated

def expected_mpg(weight):
  mpg = 0 # Default is 0
  weightFactor = 0

  if weight < 3800:
    #Assign equivalent mileage
    mpg = 30
    return mpg
  elif 3800 <= weight < 6500:
    netWeight = (weight-3799)
    weightFactor = 0.002 * netWeight
    mpg = 22 - weightFactor
    return mpg 
  elif weight >= 6500:
    netWeight = weight-6499
    weightFactor = 0.003 * netWeight
    mpg = 15 - weightFactor
    return mpg 

# print(expected_mpg(3999))
# print(expected_mpg(7499))

# PART C Finished