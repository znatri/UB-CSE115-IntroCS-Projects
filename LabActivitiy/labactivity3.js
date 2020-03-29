'use strict';
// Part A (7 points) - simple functions

function salesTax(subtotalclothing, subtotalpy){
  let clothtax = 0.0475*subtotalclothing;
  let pytax = 0.0875*subtotalpy;  
  let totalsalestax = clothtax + pytax;
  return totalsalestax;
}

// console.log(salesTax(0.0, 100.0));
// console.log(salesTax(100.0, 100.0));

function paintCans(areatobepainted){
  let areapercan = 400;
  let cansrequired = Math.floor((areatobepainted/areapercan)) + 1;
 
  return cansrequired+" cans are needed";
}

// console.log(paintCans(800));
// console.log(paintCans(799));

// Part B (4 points) - function calling library functions

function slide_text(valString){
  valString = valString.replace(/is /g, "");
  valString = valString.replace(/the /g, "");
  return valString.length;
}

// console.log(slide_text("This is the line"));
// console.log(slide_text("the issue is your wraithe."));

// Part C (4 points) - function calling user-defined function

function totalCost(subtotalfood, subtotalclothing, subtotalpy){
  let totaltax = salesTax(subtotalclothing, subtotalpy);
  let subtotal = subtotalfood + subtotalclothing + subtotalpy;
  let totalCost = 0;
  if (subtotal > 1000){
    totalCost = subtotal;
  } else {
    totalCost = subtotal + totaltax;
  }
  return totalCost;
}

// console.log(totalCost(5.99, 0.0, 100.0));
// console.log(totalCost(5.99, 100.0, 100.0));