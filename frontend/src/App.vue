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
/* Ensures full height layout */
html, body {
  height: 100%;
  margin: 0;
}

/* Make the wrapper fill the screen */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Let main content expand */
router-view {
  flex-grow: 1;
}

</style>