"use strict"

// Ajax Functions Go Here

// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received    
function ajaxGetRequest(path, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
        callback(this.response);
    }
  };
  request.open("GET", path);
  request.send();
}

function ajaxPostRequest(path, data, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
      callback(this.response);
    }
  };
  request.open("POST", path);
  request.send(data);
}

// All Javascript Code Goes Here

function getData() {
  ajaxGetRequest("/scatter_plot", showScatterPlot);
  ajaxGetRequest("/pie_chart", showPieChart);
  ajaxGetRequest("/line_plot", showLinePlot);
}

function showScatterPlot(response){
  let y_val = JSON.parse(response);
  let x_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];
  let trace = [{
    x: x_val, 
    y: y_val,
    mode: "markers",
    type: "scatter"
  }];
  let layout = {
    'title' : "Tows by Day of the Month",
    'xaxis' : {"title": "Day of the Month"},
    'yaxis' : {"title": "# Tows"}
  };
  Plotly.newPlot('plot-scatter', trace, layout);
}

function showPieChart(response) {
  let data = JSON.parse(response);
  let label_list = [];
  let values_list = [];
  for (let [key, value] of Object.entries(data)) {
    label_list.push(key);
    values_list.push(value);
  }
  let trace = [{
     values: values_list, 
     labels: label_list,
     type: "pie"
   }];
  let layout = {
    title: "Tows by District",
    // height: 400,
    // width: 500
  };
  Plotly.newPlot('plot-pie', trace, layout);
}

function showLinePlot(response) {
  let jsondata = JSON.parse(response);
  let data = [];
  let x_val = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  for (let [key, value] of Object.entries(jsondata)){
    let trace = {
      x: x_val,
      y: value,
      type: 'scatter',
      mode: 'lines',
      name: key
    };
    data.push(trace);
  }
  let layout = {
    title:'Tows by Month and Description',
    'xaxis' : {"title": "Month"},
    'yaxis' : {"title": "# Tows"}
  };
  Plotly.newPlot('plot-line', data, layout);
}