`use strict`

function longWords(arr, num){
  let retVal = [];
  for (let x in arr){
    let len = arr[x].length;
    if (len > num){
      retVal.push(arr[x]);
    }
  }
  return retVal;
}

console.log(longWords(["My","name","is","Brak"], 99));
console.log(longWords(["Hello", "my", "name", "is", "Inigo", "Montoya"], 4));
