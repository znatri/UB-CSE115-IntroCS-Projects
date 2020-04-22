// All Javascript Code Goes Here

function getData() {
    ajaxGetRequest("/scatter_plot", showScatterPlot);
    // ajaxGetRequest("/pie_chart", showPieChart);
    // ajaxGetRequest("/line_plot", showLinePlot);
}

function showScatterPlot(response){
    let data = JSON.parse(response);
    let trace = [{
      x: data.x, 
      y: data.y,
      data: "Buffalo Pop",
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
}

function showLinePlot() {
    let data = JSON.parse(response);
}