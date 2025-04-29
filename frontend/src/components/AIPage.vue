<template>
    <section class="ai-container">
      <div class="container">
        <!-- Header (copied from About.vue) -->
        <div class="about-header">
          <h2 class="page-title">🧠 AI Tools</h2>
        </div>
  
        <!-- Tabs -->
        <div class="tabs-navbar">
          <a @click="selectedTab = 'chat'" :class="{ active: selectedTab === 'chat' }">🤖 Chat</a>
          <a @click="selectedTab = 'image'" :class="{ active: selectedTab === 'image' }">🖼️ Image Analyzer</a>
        </div>
  
        <!-- Tab Content -->
        <div class="tab-content">
          <AIChat v-if="selectedTab === 'chat'" />
          <ImageAnalyzer v-if="selectedTab === 'image'" />
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import AIChat from './AIChat.vue'
  import ImageAnalyzer from './ImageAnalyzer.vue'
  
  const selectedTab = ref('chat')
  </script>
  
  <style scoped>
  .ai-container {
    padding: 20px 20px;
    text-align: center;
  }
  
  .container {
    max-width: 900px;
    margin: 0 auto;
    text-align: left;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .about-header {
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 2px solid #ddd;
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  
  .page-title {
    font-size: 24px;
    font-weight: bold;
  }
  
  .tabs-navbar {
    display: flex;
    gap: 35px;
    border-bottom: 2px solid #eee;
    margin-bottom: 24px;
    padding-bottom: 8px;
  }
  
  .tabs-navbar a {
    font-size: 18px;
    font-weight: 600;
    color: #444;
    text-decoration: none;
    border-bottom: 3px solid transparent;
    padding-bottom: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .tabs-navbar a.active {
    color: #222;
    border-bottom-color: #6bb87b;
  }
  </style>