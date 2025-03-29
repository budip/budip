<template>
  <div class="container">
    <section>
    <!-- 🤖 AI Chat Section -->
    <header class="page-header">
      <h2 class="page-title">🤖 AI Chat</h2>
    </header>

    <div class="chat-box">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        class="chat-message"
        :class="msg.role"
      >
        <p class="chat-text">{{ msg.role === 'user' ? 'You' : 'AI' }}: {{ msg.content }}</p>
      </div>
    </div>

    <div class="input-area">
      <textarea
        v-model="prompt"
        placeholder="Ask me anything..."
        class="prompt-input"
        rows="4"
      ></textarea>
      <button @click="sendPrompt" class="send-btn" :disabled="loading">
        {{ loading ? 'Thinking...' : 'Send' }}
      </button>
    </div>
    </section>

    <!-- 🖼️ Image Analyzer Section -->
    <section class="analyzer-section">
      <ImageAnalyzer />
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ImageAnalyzer from '../components/ImageAnalyzer.vue'

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
      body: JSON.stringify({ prompt: prompt.value }),
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
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.05);
}

.page-header,
.section-title {
  border-bottom: 2px solid #eee;
  padding-bottom: 10px;
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 600;
  color: #333;
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
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.04);
  font-size: 16px;
  line-height: 1.5;
  word-wrap: break-word;
}

.chat-message.user {
  background-color: #e7f1ff;
  align-self: flex-end;
  border-left: 4px solid #3a6ea5;
}

.chat-message.ai {
  background-color: #f7f7f7;
  align-self: flex-start;
  border-left: 4px solid #6bb87b;
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
  border: 1px solid #ccc;
  border-radius: 6px;
  resize: vertical;
  font-size: 16px;
  font-family: inherit;
}

.send-btn {
  align-self: flex-end;
  padding: 10px 20px;
  background-color: #6bb87b;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease-in-out;
}

.send-btn:hover {
  background-color: #48995e;
}

.send-btn:disabled {
  background-color: #bbb;
  cursor: not-allowed;
}

.analyzer-section {
  margin-top: 50px;
  border-top: 1px solid #eee;
  padding-top: 30px;
}
</style>