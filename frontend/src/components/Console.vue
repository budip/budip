<template>
    <section class="console-container">
      <div class="container">
        <header class="console-header">
          <h2 class="page-title">🧩 Console</h2>
          <p class="subtitle">View raw API data, system metrics, and upcoming Kafka insights.</p>
        </header>
  
        <div class="api-section">
          <h3 class="section-title">📡 API Data</h3>
          <button class="refresh-btn" @click="fetchApiData" :disabled="loading">
            {{ loading ? 'Loading...' : 'Refresh' }}
          </button>
          <a :href="apiConsoleUrl" target="_blank" rel="noopener noreferrer" class="api-console-link">
            Open API Console
          </a>
  
          <div class="json-box" v-if="apiData">
            <pre>{{ formattedJson }}</pre>
          </div>
  
          <hr class="divider" />
  
          <h3 class="section-title">🛰️ Kafka Status</h3>

            <div v-if="kafkaStatus.connected" class="kafka-info">
            <p class="kafka-connected">🟢 Connected to Kafka</p>

            <!-- Broker Info -->
            <div v-if="kafkaStatus.metrics">
                <p><strong>Broker:</strong> {{ kafkaStatus.metrics.broker }}</p>
                <p><strong>Topics:</strong> {{ kafkaStatus.metrics.topic_count }}</p>
                <p><strong>Partitions:</strong> {{ kafkaStatus.metrics.partition_count }}</p>
            </div>

            <!-- Topic List -->
            <div v-if="kafkaStatus.topics.length">
                <p><strong>Topic List:</strong></p>
                <ul>
                <li v-for="topic in kafkaStatus.topics" :key="topic">{{ topic }}</li>
                </ul>
            </div>
            <div v-else>
                <p>No topics found.</p>
            </div>
            </div>

            <div v-else class="kafka-error">
            🔴 Kafka not available
            <div v-if="kafkaStatus.error">Error: {{ kafkaStatus.error }}</div>
            </div>
          
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios'
  
  const apiConsoleUrl = `${import.meta.env.VITE_API_BASE_URL}/api/posts/`
  const kafkaStatus = ref({ connected: false, topics: [] })
  
  const fetchKafkaStatus = async () => {
    try {
      const res = await axios.get('/api/kafka/status/')
      kafkaStatus.value = res.data
    } catch (err) {
      kafkaStatus.value = {
        connected: false,
        error: 'Unable to connect to Kafka',
      }
    }
  }
  
  onMounted(() => {
    fetchKafkaStatus()
  })
  
  const apiData = ref(null)
  const loading = ref(false)
  
  const fetchApiData = async () => {
    loading.value = true
    try {
      const response = await axios.get('/api/posts/')
      apiData.value = response.data
    } catch (error) {
      console.error('Failed to fetch API data:', error)
      apiData.value = { error: 'Failed to load data' }
    } finally {
      loading.value = false
    }
  }
  
  const formattedJson = computed(() => {
    return JSON.stringify(apiData.value, null, 2)
  })
  </script>
  
  <style scoped>
  .console-container {
    padding: 20px;
  }
  
  .container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.05);
  }
  
  .console-header {
    border-bottom: 2px solid #eee;
    margin-bottom: 24px;
  }
  
  .page-title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 8px;
  }
  
  .subtitle {
    color: #666;
    font-size: 14px;
    margin-bottom: 12px;
  }
  
  .api-section {
    margin-top: 24px;
  }
  
  .section-title {
    font-size: 18px;
    font-weight: 500;
    margin-bottom: 8px;
  }
  
  .refresh-btn {
    background-color: #6bb87b;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    cursor: pointer;
    margin-bottom: 16px;
  }
  
  .refresh-btn:hover {
    background-color: #48995e;
  }
  
  .api-console-link {
    display: inline-block;
    margin-left: 12px;
    padding: 10px 16px;
    background-color: #eaf2ff;
    color: #1d4ed8;
    font-weight: 600;
    font-size: 15px;
    border-radius: 6px;
    text-decoration: none;
    transition: background-color 0.2s ease-in-out;
  }
  
  .api-console-link:hover {
    background-color: #dbeafe;
    color: #1e40af;
  }
  
  .json-box {
    background: #f4f4f4;
    padding: 16px;
    border-radius: 6px;
    max-height: 400px;
    overflow: auto;
    font-family: monospace;
    font-size: 14px;
    white-space: pre-wrap;
    margin-top: 16px;
  }
  
  .divider {
    margin: 32px 0;
    border: none;
    border-top: 1px solid #ddd;
  }
  
  .kafka-connected {
    color: #1a7f37;
    font-weight: 500;
    margin-bottom: 8px;
  }
  
  .kafka-error {
    color: #b91c1c;
    font-weight: 500;
    margin-top: 8px;
  }
  </style>
