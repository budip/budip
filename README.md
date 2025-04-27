# BP's Digital Lab

**Welcome!**

This is my personal full-stack website — a creative playground where I explore content creation, real-time interaction, AI integration, and space data visualization.

The platform brings together multiple custom-built applications into a seamless experience, including:

- A dynamic **blog**
- A **NASA-themed space exploration section**
- An **OpenAI-powered chat assistant**
- An **advanced AI Image Analyzer** that can recognize uploaded images, describe them in natural language, and suggest real-world product pricing where applicable

The backend is powered by **Django**, fully containerized with **Docker**, automatically deployed through **GitHub Actions**, and hosted on **AWS EC2** for scalability and reliability. The frontend is built with **Vue 3** and **Vite** for a fast and clean user experience.

> <br>Not a generic starter template. This site reflects what I love to build: things that are useful, curious, and human-centered.<br><br>

<br>

## 🧩 What's Inside

This site is made up of four core apps:

### 🌐 Home

The landing page that introduces the site and links to featured content.

### 📝 Blog

A fully functional blog system where I write and share my thoughts, ideas, and updates. It supports:

- Markdown-style posts
- Post creation/editing via the frontend
- Django backend with API integration

### 🚀 Space (NASA)

A space-themed section featuring:

- Data exploration and visuals related to NASA APIs
- Astronomy and space science content
- ISS and planetary info integration

### 🤖 AI (Chat)

An interactive AI chat assistant powered by OpenAI, built using:

- Django Rest Framework for backend API
- Vue 3 with Vite for frontend experience
- Chat-style interface that allows prompt/response exchange
- Seamless backend integration via fetch and CORS

### 🖼️ AI Image Analyzer

An AI-powered image analysis tool integrated into the assistant. Built with OpenAI’s vision model to help users understand their images safely and privately — no training or data storage involved.

- **OpenAI Vision Model** – Uses one of the most advanced LLMs to analyze images
- **Image Preprocessing** – Custom image reducer for efficient and fast analysis
- **Custom Prompt & Agent** – Handles specific image-related tasks with tailored logic
- **Outputs:**
  - Image description
  - Alternative text (alt text)
  - Category classification
  - Concise summary
  - Product Detection and Price Suggestions:
    If the uploaded image contains a recognizable product, the system automatically detects it, fetches real-time pricing from multiple stores, and suggests nearby purchasing options.

<br>

## ⚙️ Technologies Used

- **Frontend**: Vue 3, Vite, TailwindCSS
- **Backend**: Django, Django REST Framework
- **AI Integration**: OpenAI API
- **Containerized**: Docker + Docker Compose
- **Database**: PostgreSQL
- **CI/CD**: GitHub Actions for full build/test/deploy pipeline
- **Deployment**: Hosted on AWS EC2

<br>

## 🚀 CI/CD & Deployment

This project uses **GitHub Actions** for continuous integration and deployment. Key steps in the pipeline include:

- Linting and code checks on every commit
- Automated tests for backend and frontend
- Docker image builds for all services
- Deployment to AWS EC2 using SSH and Docker Compose

Every push to `main` triggers a clean end-to-end deployment, ensuring the site is always up to date with the latest code.

<br>

## 💻 Folder Structure Overview

<small>

```text
project/
├── backend/               # Django app with blog, space, ai
│   ├── apps/
│   ├── manage.py
│   ├── project/
│   └── staticfiles/
├── frontend/              # Vue 3 + Vite frontend
│   ├── src/components/
│   ├── main.js
│   ├── vite.config.js
│   └── ...
├── .github/workflows/     # GitHub Actions CI/CD config
├── docker-compose.yml
├── public/                # Static fallback content
└── README.md
```

</small>

<br>

## 👤 Author

**Budi Prasetya Chen**  
Engineer • Explorer • Creator

📫 Email: bpchen@gmail.com  
🌐 LinkedIn: https://www.linkedin.com/in/budi-prasetya/  
📺 YouTube: https://www.youtube.com/@budiprasetya  
🌌 NASA Social Participant  
💬 OpenAI API Explorer
