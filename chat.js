const form = document.getElementById('chatform');
const input = document.getElementById('userInput');
const chatbox = document.getElementById('chatbox');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const text = input.value;
    input.value = '';

    chatbox.innerHTML += `You: ${text}<br/>`;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'message': text })
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `Bot: ${data['response']}<br/>`;
    });
});
