// All Javascript Code Goes Here

function getData() {
    ajaxGetRequest("/scatter_plot", showScatterPlot);
    ajaxGetRequest("/pie_chart", showPieChart);
    ajaxGetRequest("/line_plot", showLinePlot);
}

function showScatterPlot(response) {
    let data = JSON.parse(response);
}

function showPieChart(response) {
    let data = JSON.parse(response);
}

function showLinePlot() {
    let data = JSON.parse(response);
}