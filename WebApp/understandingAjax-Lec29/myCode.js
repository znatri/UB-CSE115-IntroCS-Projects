// Requesting data from server
// url "path", data "jsonBlobRecievedFromServer"
function ajaxGetRequest(url, func){
    // Copy & paste
}

function acceptData(jsonBlob){ // Executed by AjaxGetFuntion
    let data = JSON.parse(jsonBlob
    // Do stuff here
}

function getData(){ // Executed by HTML on Load
    ajaxGetRequest("static_data", acceptData);
    // static_data path triggers function in python on server
    // as soon as data is recieved ajaxGetRequest executes acceptData()
}

// Sending data to server
function ajaxPostRequest(url, data, callback){

}

