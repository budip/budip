<template>
  <section class="chat-wrapper">
    <!-- Chat Box -->
    <div ref="chatBoxRef" class="chat-box">
      <template v-if="messages.length">
        <div
          v-for="(msg, index) in messages"
          :key="index"
          class="chat-message"
          :class="msg.role"
        >
          <div class="chat-text" v-if="msg.role === 'user'">
            You: {{ msg.content }}
          </div>
          <div
            class="chat-text"
            v-else
            v-html="DOMPurify.sanitize(marked(`AI: ${msg.content}`))"
          ></div>
        </div>
      </template>
      <template v-else>
        <div class="chat-placeholder">Your conversation will appear here...</div>
      </template>
    </div>

    <!-- Input Area -->
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
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { marked } from 'marked'
import DOMPurify from 'dompurify'

const prompt = ref('')
const messages = ref([])
const loading = ref(false)
const chatBoxRef = ref(null)

const scrollToBottom = () => {
  nextTick(() => {
    if (chatBoxRef.value) {
      chatBoxRef.value.scrollTop = chatBoxRef.value.scrollHeight
    }
  })
}

const sendPrompt = async () => {
  if (!prompt.value.trim()) return

  messages.value.push({ role: 'user', content: prompt.value })
  scrollToBottom()
  loading.value = true

  try {
    const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/ai/chat/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: prompt.value }),
    })

    const data = await res.json()
    messages.value.push({ role: 'ai', content: data.response || 'No response' })
    scrollToBottom()
  } catch (err) {
    messages.value.push({ role: 'ai', content: 'Something went wrong.' })
    console.error(err)
    scrollToBottom()
  } finally {
    prompt.value = ''
    loading.value = false
  }
}
</script>

<style scoped>
.chat-wrapper {
  display: flex;
  flex-direction: column;
  height: 100%;
  max-height: calc(70vh - 30px);
}

/* Chat area */
.chat-box {
  flex-grow: 1;
  overflow-y: auto;
  min-height: 150px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 12px;
  margin-bottom: 12px;
  background-color: #fafafa;
  border: 1px solid #eee;
  border-radius: 6px;
}

/* Empty state */
.chat-placeholder {
  color: #999;
  font-style: italic;
  text-align: center;
  margin-top: auto;
  margin-bottom: auto;
}

/* Message bubbles */
.chat-message {
  padding: 12px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
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

/* Input */
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
</style>
