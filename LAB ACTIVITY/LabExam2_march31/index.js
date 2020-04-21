// Part A (40 points) - array processing

function sumPositives(lst){
  let sum = 0;
  for (let num of lst){
    if (num > 0){
      sum +=  num;
    }
    else {
      sum += 0;
    }
  }
  return sum;
}

// console.log(sumPositives([5, -6, -7]));
// console.log(sumPositives([0, -1, -6]));

// Part B (20 points) - Working with Objects

function whales(obj, k){
  let data = [];
  for (let key of Object.keys(obj)){
    let val = obj[key];
    if (val > k){
      data.push(key);
    }
  }
  return data;
}

// console.log(whales({'jody':1,'pat':91,'kelly':103,'corey':89}, 70));
// console.log(whales({'jody':1,'pat':90,'kelly':10}, 102));