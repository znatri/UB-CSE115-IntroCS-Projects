// Part C (4 points) - using DOM functions

function testScore(){
    let exam = parseFloat(document.getElementById('exam').value);
    let makeupexam = parseFloat(document.getElementById('makeup').value);
    if (makeupexam > exam){
        return makeupexam;
    } else {
        return exam;
    }
}

function displayResult(val){
  let myDiv = document.getElementById('result');
  let result = val.toString();
  myDiv.innerHTML = result;
}