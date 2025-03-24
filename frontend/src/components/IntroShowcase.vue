<template>
    <div class="intro-wrapper">
        <h2 class="intro-heading">👋 Welcome!</h2>
        <p>
            This is my <strong>personal full-stack website</strong> — a creative playground where I explore content creation, real-time interaction, AI integration, and space data.
            It brings together multiple custom-built apps into one seamless platform.
        </p>
    
        <p>
            The project includes a <strong>blog</strong>, a <strong>NASA-themed space section</strong>, an <strong>OpenAI-powered chat assistant</strong>,
            and a clean frontend powered by <strong>Vue 3 + Vite</strong>. It's fully containerized with <strong>Docker</strong>, continuously deployed via <strong>GitHub Actions</strong>,
            and hosted on <strong>AWS EC2</strong>.
        </p>
    
        <blockquote class="highlight-quote">
        💡 <em>Not a generic starter template.</em><br>
        This site reflects what I love to build: things that are <strong>useful</strong>, <strong>curious</strong>, and <strong>human-centered</strong>.
        </blockquote>

        <p style="margin-top: 20px;" class="badge-row">
            <img src="https://img.shields.io/badge/Django-3.2-green?style=flat&logo=django" />
            <img src="https://img.shields.io/badge/Vue-3.x-41B883?style=flat&logo=vue.js" />
            <img src="https://img.shields.io/badge/Dockerized-blue?style=flat&logo=docker" />
            <img src="https://img.shields.io/badge/Deployed-GitHub%20Actions-blueviolet?style=flat&logo=githubactions" />
        </p>    
    </div>
  </template>
  
  <script setup>
  // No logic needed for this section yet
  </script>
  
  <style scoped>
    .intro-wrapper {
    max-width: 920px;
    margin: 12px auto 24px;
    padding: 32px;
    background: #ffffff;
    border-radius: 14px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.05);
    line-height: 1.65;
    font-size: 15px;
    color: #2d3748;
    }

    .intro-heading {
    font-size: 22px;
    font-weight: 600;
    color: #2c5282;
    margin-bottom: 16px;
    }

    .highlight-quote {
    margin-top: 24px;
    padding: 16px 20px;
    background-color: #f0f4f8;
    border-left: 4px solid #4299e1;
    border-radius: 6px;
    font-style: italic;
    color: #4a5568;
    font-size: 14px;
    }

    .badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
    }
  </style>