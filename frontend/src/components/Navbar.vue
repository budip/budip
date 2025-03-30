<template>
  <nav class="navbar navbar-dark bg-dark full-width-nav">
    <div class="container nav-container">
      <router-link class="navbar-brand" to="/">BP Blog</router-link>
      <ul class="navbar-nav d-flex flex-row gap-3 mb-0">
        <li class="nav-item"><router-link class="nav-link" to="/">Home</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/blog">Blog</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/space">Space</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/ai">AI Tools</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/about">About</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.navbar {
  background-color: #222;
  padding: 0.5rem 1rem;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.navbar-nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  padding-left: 0;
  list-style: none;
  margin: 0;
}

.nav-link {
  color: #fff;
  padding: 0.5rem 0.75rem;
  text-decoration: none;
}

.nav-link:hover {
  color: #ccc;
}
</style>