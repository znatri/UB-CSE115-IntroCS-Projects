function renderChat(response){
    let newline = "<br />";
    let chat = "";
    let chatDiv = document.getElementById("chat");
    let messageList;
    for (let data of messageList){
        chat = chat + data.message + newline;
    }
    chatDiv.innerHTML = chat;
}

function loadChat(){
    // HTML directs browser to call when page loaded
    //
    // Will need to connect to server and download
    // messages
    ajaxGetRequest("/chat", renderChat);
}

function sendMessage(){
    // Function called whenever Send button is clicked
    //
    // Should get message from text box & send to server
    // Also needs to add message

}

