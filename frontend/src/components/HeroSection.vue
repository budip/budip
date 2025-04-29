<template>
    <header class="hero">
      <div class="overlay"></div>
      <div class="hero-content">
        <h1>Welcome to my website</h1>
        <p>Exploring the future through technology, creativity, and discovery.</p>
        <div class="buttons">
          <a href="blog" class="btn btn-primary">Explore the Blog</a>
          <a href="ai" class="btn btn-outline-light">Try AI Chat</a>
        </div>
      </div>
    </header>
  </template>
  
  <style scoped>
  .hero {
    position: relative;
    width: 100%;
    height: 350px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    overflow: hidden;
    padding-top: 0px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  }
  
  .hero::before {
    content: "";
    position: absolute;
    top: -150px;
    left: 50%;
    transform: translateX(-50%);
    width: 1920px;
    height: 500px;
    background: url('/images/honeycomb-bg.png') no-repeat center top;
    background-size: cover;
    filter: brightness(60%);
    z-index: -1;
  }
  
  .overlay {
    position: absolute;
    top: 0;
    left: 50%;
    width:1920px;
    height: 100%;
    transform: translateX(-50%);
    background-color: #f1f5f9;
    background: rgba(0, 0, 0, 0.2);
    z-index: -1;
  }
  
  .hero-content {
    position: relative;
    background: rgba(213, 206, 206, 0.3);
    padding: 30px 40px;
    border-radius: 10px;
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 600px;
  }
  
  .buttons {
    margin-top: 15px;
    display: flex;
    gap: 20px;
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