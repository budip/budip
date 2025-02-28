// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { Configuration, OpenAIApi } = require('openai');
require('dotenv').config();

// Validate API key
if (!process.env.OPENAI_API_KEY) {
  console.error('Error: Missing OPENAI_API_KEY in environment variables.');
  process.exit(1); // Exit if the API key is not set
}

// Initialize OpenAI API
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Create an Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static('public')); // Serve static files like index.html

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Server is healthy!' });
});

// Chat endpoint
app.post('/chat', async (req, res) => {
  const { message } = req.body;

  // Validate input
  if (!message || typeof message !== 'string') {
    return res.status(400).json({ error: 'Invalid or missing "message" in request body.' });
  }

  try {
    // Call OpenAI API
    const response = await openai.createChatCompletion({
      model: 'chatgpt-4o-latest',
      messages: [{ role: 'user', content: message }],
    });

    // Respond with OpenAI's reply
    res.json({ response: response.data.choices[0].message.content });
  } catch (error) {
    console.error('Error connecting to OpenAI API:', error.message);

    // Send error response to the client
    res.status(500).json({ error: 'Failed to process your request.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});