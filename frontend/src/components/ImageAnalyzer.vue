<template>
    <div class="image-analyzer-container">
      <p class="analyzer-intro">
        <strong>Upload a photo</strong> and let AI describe what it sees.
      </p>

      <!-- Upload + Button -->
      <div class="flex flex-col gap-2 sm:flex-row sm:items-center sm:gap-4 mb-6">
        <input type="file" accept="image/*" @change="onFileChange" class="file-input" />
        <button
          @click="submitImage"
          class="send-btn"
          :disabled="!imageFile || loading"
        >
          {{ loading ? "Analyzing..." : "Analyze Image" }}
        </button>
      </div>
  
      <!-- Grid Layout -->
      <div class="grid-container" v-if="previewUrl">
        <!-- Left: Image -->
        <div class="image-preview">
          <img :src="previewUrl" alt="Preview" />
        </div>
  
        <!-- Right: Results (only after analyze) -->
        <div
            v-if="parsedResponse.title || parsedResponse.caption || parsedResponse.categories.length"
            class="result-box"
            >
            <h3 class="text-xl font-semibold mb-2">{{ parsedResponse.title }}</h3>

            <p class="text-gray-700 mb-2">
                <strong>Caption:</strong> {{ parsedResponse.caption }}
            </p>

            <p v-if="parsedResponse.categories.length" class="text-gray-600 text-sm mb-1">
                <strong>Categories:</strong> {{ parsedResponse.categories.join(', ') }}
            </p>

            <p v-if="parsedResponse.alt_text" class="text-gray-600 text-sm">
                <strong>Alt Text:</strong> {{ parsedResponse.alt_text }}
            </p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import axios from 'axios'
  
  const imageFile = ref(null)
  const previewUrl = ref(null)
  const responseText = ref('')
  const loading = ref(false)
  
  function onFileChange(event) {
    const file = event.target.files[0]
    if (file) {
      imageFile.value = file
      previewUrl.value = URL.createObjectURL(file)
      responseText.value = ''  // 🧼 Clear previous result!
    }
  }
  
  const parsedResponse = computed(() => {
    try {
      if (!responseText.value.trim().includes('{')) {
        return { title: '', caption: '', categories: [] }
      }
  
      const cleanText = responseText.value
        .replace(/^```json\s*/i, '')
        .replace(/```$/, '')
        .trim()
  
      const parsed = JSON.parse(cleanText)
      return {
        title: parsed.title || '',
        caption: parsed.caption || '',
        categories: parsed.categories || [],
        alt_text: parsed.alt_text || ''
      }
    } catch (e) {
      return { title: '', caption: '', categories: [] }
    }
  })
  
  async function submitImage() {
    if (!imageFile.value) return
  
    loading.value = true
    responseText.value = ''
  
    const formData = new FormData()
    formData.append('image', imageFile.value)
  
    try {
      const response = await axios.post('/api/ai/analyze-image/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      responseText.value = response.data.result
    } catch (error) {
      console.error(error)
      responseText.value = '⚠️ Error analyzing image.'
    } finally {
      loading.value = false
    }
  }
  </script>
  
  <style scoped>
  .image-analyzer-container {
    padding-top: 0px;
  }
  
  .analyzer-intro {
    font-size: 16px;
    color: #444;
    margin-bottom: 16px;
    line-height: 1.6;
  }

  .file-input {
    padding: 6px 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 6px;
  }
  
  .send-btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: #6bb87b;
    color: #fff;
    font-weight: bold;
    font-size: 16px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
  }
  
  .send-btn:hover {
    background-color: #48995e;
  }
  
  .send-btn:disabled {
    background-color: #bbb;
    cursor: not-allowed;
  }
  
  .grid-container {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 24px;
    margin-top: 24px;
    align-items: start;
  }
  
  /* Left: Preview Image */
  .image-preview img {
    width: 200px;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }
  
  /* Right: Results */
  .result-box {
    padding: 20px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  }
  </style>
