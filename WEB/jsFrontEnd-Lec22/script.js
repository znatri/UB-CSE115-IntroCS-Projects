let myDiv = document.getElementById('div1');
myDiv.innerHTML = "<h1>Content from Javascipt</h1>";


// Using Plot.ly Library
let data = [{
  x:[1930, 1940, 1950, 1960], 
  y:[573076, 575901, 580132, 532759],
  data: "Buffalo Pop"
}];

let layout = {
  title : "Buffalo Population",
  xaxis : {"title": "year"},
  yaxis : {"title": "population"}
};

Plotly.newPlot('myplot', data, layout);

function additionCalculator(){
    let a = document.getElementById("input_one").value;
    let b = document.getElementById("input_two").value;
    let sum = Number(a) + Number(b);
    document.getElementById("sum").innerHTML = sum;
}