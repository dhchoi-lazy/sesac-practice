function sendMessage() {
    var input = document.getElementById("chat-input");
    var message = input.value.trim();
    if (message !== '') {
        var chatBox = document.getElementById("chat-box");
        var newMessage = document.createElement("p");
        newMessage.innerHTML = message;
        newMessage.classList.add("chat-message", "user-message");
        chatBox.appendChild(newMessage);
        input.value = ""; // Clear the input field after sending a message
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
    }
}

function handleKeyPress(event) {
    // Check if the Enter key is pressed
    if (event.keyCode === 13) {
        event.preventDefault(); // Prevent the form from being submitted
        sendMessage();
    }
}
