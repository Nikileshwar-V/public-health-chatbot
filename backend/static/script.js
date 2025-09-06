function addMessage(message, sender) {
  let chatbox = document.getElementById("chatbox");
  let msgHTML = "";

  if (sender === "user") {
    msgHTML = `
      <div class="message-row user-row">
        <div class="message user-msg">${message}</div>
        <img src="/static/images/user.png" class="avatar">
      </div>`;
  } else {
    msgHTML = `
      <div class="message-row bot-row">
        <img src="/static/images/bot.png" class="avatar">
        <div class="message bot-msg">${message}</div>
      </div>`;
  }

  chatbox.innerHTML += msgHTML;
  chatbox.scrollTop = chatbox.scrollHeight;
}

async function sendMessage() {
  let input = document.getElementById("userInput");
  let message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");

  let response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  });
  let data = await response.json();

  data.responses.forEach(botMsg => addMessage(botMsg, "bot"));
  input.value = "";
}

document.getElementById("userInput").addEventListener("keypress", function(e) {
  if (e.key === "Enter") sendMessage();
});
