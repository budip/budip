const chatForm = document.getElementById('chat-form');
const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('user-input');

// Function to preprocess Markdown to remove extra empty lines
const preprocessMarkdown = (markdown) => {
  return markdown
    .split('\n') // Split text into lines
    .filter((line, index, lines) => {
      // Keep the line if it's not empty or if the previous line is not empty
      return line.trim() !== '' || (index > 0 && lines[index - 1].trim() !== '');
    })
    .join('\n'); // Rejoin lines
};

// Function to append messages
const appendMessage = (text, sender, isMarkdown = false) => {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${sender}`;

  if (isMarkdown && sender === 'ai') {
    // Preprocess and render Markdown for AI responses
    const preprocessedText = preprocessMarkdown(text);
    const markdownDiv = document.createElement('div');
    markdownDiv.className = 'markdown-content';
    markdownDiv.innerHTML = marked.parse(preprocessedText); // Render Markdown
    messageDiv.appendChild(markdownDiv);
  } else {
    // Plain text for user messages
    messageDiv.textContent = text;
  }

  chatbox.appendChild(messageDiv);
  chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll
};

// Typing indicator
const showTypingIndicator = () => {
  const typingDiv = document.createElement('div');
  typingDiv.className = 'typing-indicator';
  typingDiv.textContent = 'BP is typing...';
  typingDiv.id = 'typing-indicator';
  chatbox.appendChild(typingDiv);
  chatbox.scrollTop = chatbox.scrollHeight;
};

const removeTypingIndicator = () => {
  const typingDiv = document.getElementById('typing-indicator');
  if (typingDiv) typingDiv.remove();
};

// Handle form submission
chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = userInput.value;
  appendMessage(message, 'user'); // Append user's message
  userInput.value = '';

  showTypingIndicator(); // Show typing indicator

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    removeTypingIndicator(); // Remove typing indicator
    appendMessage(data.response, 'ai', true); // Append AI's response with Markdown
  } catch (error) {
    removeTypingIndicator(); // Remove typing indicator
    console.error('Error:', error);
    appendMessage('Failed to connect to the server.', 'ai');
  }
});