const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message");
const chatBox = document.getElementById("chat-box");

function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        sender === "user" ? "user-message" : "bot-message"
    );

    messageDiv.innerHTML = message;

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping() {
    const typing = document.createElement("div");

    typing.classList.add("bot-message");

    typing.id = "typing";

    typing.innerHTML = "🤖 Thinking...";

    chatBox.appendChild(typing);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById("typing");

    if (typing) {
        typing.remove();
    }
}

chatForm.addEventListener("submit", async function (e) {

    e.preventDefault();

    const message = messageInput.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    messageInput.value = "";

    showTyping();

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        removeTyping();

        addMessage(data.response, "bot");

    }

    catch (error) {

        removeTyping();

        addMessage(
            "⚠ Unable to connect. Please try again.",
            "bot"
        );

    }

});