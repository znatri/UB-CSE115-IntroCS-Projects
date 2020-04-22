// All Javascript Code Goes Here

function getData() {
  ajaxGetRequest("/scatter_plot", showScatterPlot);
  ajaxGetRequest("/pie_chart", showPieChart);
  ajaxGetRequest("/line_plot", showLinePlot);
}

function showScatterPlot(response){
  let data = JSON.parse(response);
  let trace = [{
    x: data.x, 
    y: data.y,
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