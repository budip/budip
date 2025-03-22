<template>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
      <div class="container">
        <router-link class="navbar-brand" to="/">BP Blog</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><router-link class="nav-link" to="/">Home</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/blog">Blog</router-link></li>            
            <li class="nav-item"><router-link class="nav-link" to="/space">Space</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/ai-chat">AI Chat</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/about">About</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  </script>
  
  <style scoped>
  .navbar {
    background-color: #222;
  }
  </style>