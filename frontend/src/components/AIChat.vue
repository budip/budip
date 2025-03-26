<template>
  <div class="container">
      <header class="page-header">
          <h2 class="page-title">🤖 AI Chat</h2>
      </header>

      <div class="chat-box">
          <div v-for="(msg, index) in messages" :key="index" class="chat-message" :class="msg.role">
              <p class="chat-text">{{ msg.role === 'user' ? 'You' : 'AI' }}: {{ msg.content }}</p>
          </div>
      </div>

      <div class="input-area">
          <textarea v-model="prompt" placeholder="Ask me anything..." class="prompt-input" rows="4"></textarea>
          <button @click="sendPrompt" class="send-btn" :disabled="loading">
              {{ loading ? 'Thinking...' : 'Send' }}
          </button>
      </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const prompt = ref('')
const messages = ref([])
const loading = ref(false)

const sendPrompt = async () => {
  if (!prompt.value.trim()) return

  messages.value.push({ role: 'user', content: prompt.value })
  loading.value = true

  try {
      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/ai/chat/`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: prompt.value })
      })

      const data = await res.json()
      messages.value.push({ role: 'ai', content: data.response || 'No response' })
  } catch (err) {
      messages.value.push({ role: 'ai', content: 'Something went wrong.' })
      console.error(err)
  } finally {
      prompt.value = ''
      loading.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 20px auto 40px;
  text-align: left;
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #ddd;
  padding-bottom: 12px;
  margin-bottom: 25px;
}

.page-title {
  font-size: 26px;
  font-weight: bold;
  color: #333;
  display: flex;
  align-items: center;
}

.chat-box {
  max-height: 400px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

.chat-message {
  padding: 12px;
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
  line-height: 1.5;
  font-size: 16px;
}

.chat-message.user {
  background-color: #d8eafd;
  align-self: flex-end;
  border-left: 4px solid #4267b2;
}

.chat-message.ai {
  background-color: #f1f1f1;
  align-self: flex-start;
  border-left: 4px solid #81b58d;
}

.chat-text {
  margin: 0;
  color: #333;
}

.input-area {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.prompt-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  resize: vertical;
  font-size: 16px;
  font-family: inherit;
}

.send-btn {
  align-self: flex-end;
  padding: 10px 20px;
  background-color: #81b58d;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease-in-out;
}

.send-btn:hover {
  background-color: #2f8a42;
}

.send-btn:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}
</style>