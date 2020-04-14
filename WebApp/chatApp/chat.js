console.log("Anything here was run on my computer");

function loadChat(){
    // HTML directs browser to call when page loaded
    //
    // Will need to connect to server using ajax and download messages
    // when messages (jsonBlob) download call renderchat
    ajaxGetRequest("/chat", renderChat);
}

function sendMessage(){
    // Function called whenever Send button is clicked
    //
    // Should get message from text box & send to server
    // Also needs to add message to chat using renderChat
    let messageText = document.getElementById('"message');
    let message = messageText.value;
    messageText.value = "";
    let dataToSend = JSON.stringify({'message': message});
    // Post request sends message to server and updates json
    ajaxPostRequest('/send', dataToSend, renderChat);
}

function renderChat(jsonBlob){
    let newline = "<br />";
    let chat = "";
    let chatDiv = document.getElementById("chat");
    let messageList = JSON.parse(jsonBlob); // Parse the JSON Blob
    for (let data of messageList){
        chat = chat + data.message + newline;
    }
    chatDiv.innerHTML = chat;
}

