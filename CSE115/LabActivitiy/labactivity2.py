def salesTax(cloth, pyeditor):
  taxoncloth = (cloth * 0.0475)
  taxonpyeditor = (pyeditor * 0.0875)
  totaltax = taxoncloth + taxonpyeditor
  return totaltax

def total_cost(food, cloth, pyeditor):
  subtotal = cloth + pyeditor + food
  tax = salesTax(cloth, pyeditor)
  total = subtotal + tax
  return total

def paintCans(areacovered):
  areapercan = 400
  cansRequired = areacovered//areapercan + 1
  return str(cansRequired) + " cans are needed"

def slide_text(boo):
  boo = boo.replace("is ", "")
  boo = boo.replace("the ", "")
  return(len(boo))