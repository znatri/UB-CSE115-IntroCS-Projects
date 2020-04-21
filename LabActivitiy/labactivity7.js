// Part B (2 points) - basic JavaScript sorting

function sortIt(list){
    list.sort(compareFn);
  }
  
  function compareFn(val1, val2){
    if (val1 < val2){
        return -1;
    } else if (val1 > val2) {
        return 1;
    } else{
        return 0;
    }
  }
  
//   let testList=[5, 10, 2, 1, 2, 0];
//   sortIt(testList);
//   console.log(testList);

function rossTrophy(obj1, obj2){
  // Assign "points", "goals", and "games"
  
  if (obj1.points != obj2.points){
    return -1;
  } else if (obj1.points == obj2.points && obj1.goals != obj2.goals){
    return 1;
  } else if (obj1.points == obj2.points && obj1.goals == obj2.goals){
    return 0;
  }
}

let mcdavid = {"points" : 64, "goals": 22, "games": 43};
let draisaitl = {"points" : 64, "goals": 23, "games": 43};
let madeup = {"points" : 24, "goals": 24, "games": 45};

// console.log(rossTrophy(mcdavid, mcdavid)); // would evaluate to 0
// console.log(rossTrophy(draisaitl, mcdavid)); // would evaluate to any Number greater than 0
// console.log(rossTrophy(madeup, mcdavid)); // would evaluate to any Number less than 0

function rossSort(list){
  list.sort(rossTrophy);
}