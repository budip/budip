<template>
  <div id="app">
    <Navbar />
    <router-view />
  </div>
</template>


<script setup>
import Navbar from './components/Navbar.vue'
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

router-view {
  flex-grow: 1;
}

</style>