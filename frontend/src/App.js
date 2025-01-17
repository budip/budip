import axios from "axios";
import React, { useState } from "react";
import ReactMarkdown from "react-markdown";

import "./App.css";

const API_URL = process.env.REACT_APP_API_URL;

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user message to the chat
    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setLoading(true);

    try {
      const response = await fetchChatResponse(input);

      setMessages((prev) => [...prev, { role: "assistant", content: response.reply }]);
    } catch (error) {
      console.error("Error communicating with the backend:", error);

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Something went wrong. Please try again." },
      ]);
    } finally {
      setLoading(false);
      setInput("");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        budip ChatBot <small className="App-engine">Engine: gpt-4o</small>
      </header>
      <main className="App-chat-window">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`App-message ${msg.role === "user" ? "App-message-user" : "App-message-ai"}`}
          >
            <strong>{msg.role === "user" ? "You" : "AI"}:</strong>{" "}
            {msg.role === "assistant" ? (
              <ReactMarkdown>{msg.content}</ReactMarkdown>
            ) : (
              <span>{msg.content}</span>
            )}
          </div>
        ))}
        {loading && <div className="App-loading">AI is typing...</div>}
      </main>
      <footer className="App-input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="App-input"
          placeholder="Type your message here..."
          disabled={loading}
        />
        <button
          onClick={handleSend}
          className={`App-button ${loading ? "App-button-disabled" : ""}`}
          disabled={loading}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </footer>
    </div>
  );
};

// Fetch chat response from the backend
export const fetchChatResponse = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/chat`, { message });
    return response.data;
  } catch (error) {
    throw new Error("Failed to fetch response");
  }
};

export default App;