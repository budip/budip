<template>
  <section class="nasa-container">
      <div class="content-wrapper">
          <header class="page-header">
              <h2 class="page-title">🛰️ NASA Astronomy Picture of the Day</h2>
          </header>

          <div v-if="apod" class="apod-content">
              <h3 class="apod-title">{{ apod.title }}</h3>
              <p class="apod-date">{{ formatDate(apod.date) }}</p>
              
              <div class="media-container">
                  <img v-if="apod.media_type === 'image'" :src="apod.url" :alt="apod.title" class="apod-image"/>
                  <iframe v-else :src="apod.url" frameborder="0" class="apod-video"></iframe>
              </div>

              <p class="apod-explanation">{{ apod.explanation }}</p>
          </div>

          <div v-else class="loading">Loading...</div>
      </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const apod = ref(null);

onMounted(async () => {
  try {
      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/space/apod/`);
      const data = await response.json();
      apod.value = data;
  } catch (error) {
      console.error("Error fetching APOD data:", error);
  }
});

const formatDate = (dateString) => {
  const options = { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
  };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
</script>

<style scoped>
.nasa-container {
  padding: 0 0;
}

.content-wrapper {
  max-width: 900px;
  margin: 30px auto 40px; 
  text-align: center;
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 25px;
  padding-bottom: 12px;
  border-bottom: 3px solid #ddd;
}

.page-title {
  font-size: 28px;
  font-weight: bold;
  text-align: center;
  width: 100%;
}

.apod-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.apod-title {
  font-size: 22px;
  font-weight: bold;
  color: #222;
  margin-bottom: 5px;
  text-align: center;
}

.apod-date {
  font-size: 16px;
  color: #666;
  font-style: italic;
  margin-bottom: 20px;
}

.media-container {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.apod-image {
  max-width: 50%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
  border: 3px solid #ddd;
  transition: transform 0.3s ease-in-out;
}

.apod-image:hover {
  transform: scale(1.02);
}

.apod-video {
  width: 100%;
  max-width: 700px;
  height: 400px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
}

.apod-explanation {
  font-size: 16px;
  color: #444;
  line-height: 1.6;
  text-align: justify;
  padding: 0 20px;
  max-width: 800px;
}

.loading {
  font-size: 18px;
  font-weight: bold;
  color: #555;
  text-align: center;
}
</style>