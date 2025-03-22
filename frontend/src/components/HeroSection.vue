<template>
    <header class="hero">
      <div class="overlay"></div> <!-- Dimming effect only on background -->
      <div class="hero-content">
        <h1>Welcome to my website</h1>
        <p>Exploring the future through technology, creativity, and discovery.</p>
        <div class="buttons">
          <a href="blog" class="btn btn-primary">Explore the Blog</a>
          <a href="ai-chat" class="btn btn-outline-light">Try AI Chat</a>
        </div>
      </div>
    </header>
  </template>
  
  <style scoped>
  .hero {
    position: relative;
    width: 100%;
    height: 350px; /* Fixed height */
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    overflow: hidden;
    padding-top: 50px; /* 50px gap between navbar and welcome panel */
  }
  
  /* Background Image - Fixed Zoom & Position */
  .hero::before {
    content: "";
    position: absolute;
    top: -150px; /* Moves background image up */
    left: 50%;
    transform: translateX(-50%); /* Centers the background */
    width: 1920px; /* Keeps a fixed width to prevent resizing */
    height: 500px; /* Adjust height to match the zoom level */
    background: url('/images/honeycomb-bg.png') no-repeat center top;
    background-size: cover; /* Prevents stretching */
    filter: brightness(60%); /* Dim the image */
    z-index: -1; /* Keep it behind content */
  }
  
  /* Overlay to Dim Background */
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.2); /* Semi-transparent overlay */
    z-index: -1;
  }
  
  /* Welcome Panel */
  .hero-content {
    position: relative;
    background: rgba(213, 206, 206, 0.3); /* Semi-transparent light background */
    padding: 25px 40px;
    border-radius: 10px;
    backdrop-filter: blur(5px); /* Soft blur effect on text box only */
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 600px; /* Keep it responsive */
  }
  
  /* Buttons Styling */
  .buttons {
    margin-top: 15px;
    display: flex;
    gap: 20px; /* Increased spacing between buttons */
    justify-content: center;
  }
  
  .btn {
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
  }
  
  .btn-outline-light {
    border: 1px solid rgba(255, 255, 255, 0.6);
    color: white;
  }
  
  .btn-outline-light:hover {
    background: white;
    color: black;
  }
  </style>