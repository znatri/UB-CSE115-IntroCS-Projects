"use strict"

// Ajax Functions Go Here

// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received    
function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

// All Javascript Code Goes Here

function getData() {
    let routes_list = ["/scatter_plot", "/pie_chart", "/line_plot"];
    for (let route of routes_list) {
        ajaxGetRequest(route, plotGraph);
    }
}

function plotGraph(response) {
    let data = JSON.parse(response);
    Plotly.newPlot(data.plot, data.trace, data.layout);
}