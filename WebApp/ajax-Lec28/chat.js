console.log("Anything here was run on my computer")

function requestChat() {
  ajaxGetRequest("/chat", renderChat);
}

function renderChat(jsonData){
  console.log("Browser received: " + jsonData)
  let message = JSON.parse(jsonData)
  console.log("After conversion: " + message)

  let chatElem = document.getElementById("chat");
  let text = chatElem.innerHTML;
  //console.log(text)
  text = text + "<br>"
  //console.log(text)
  let chat = text + message.something;
  // console.log(chat)
  chatElem.innerHTML = chat;
  // console.log(chatElem.innerHTML)
}

function sendMessage(){
  let messageElement = document.getElementById("message");
  let message = messageElement.value;
  console.log("Message to send to server: " + message)
  messageElement.value = "";
  let toSend = JSON.stringify(message);
  console.log("Blob that is actually sent:" + toSend);
  ajaxPostRequest("/send", toSend, renderChat);
}