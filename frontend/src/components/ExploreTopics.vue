<template>
  <section class="explore-topics text-center">
    <div class="container">
      <h2>Explore Topics</h2>
      <h6>coming soon...</h6>
      <div class="topics-container">

        <div class="topic">
          <span class="icon">🌍</span>
          <h3>Travel & Adventure</h3>
          <hr />
          <p>A passion for capturing the essence of travel through photography 
            and videography. From breathtaking landscapes to vibrant cityscapes, 
            every journey is an opportunity to document the beauty, culture, and 
            untold stories of the world.</p>
        </div>

        <div class="topic">
          <span class="icon">⚙️</span>
          <h3>Engineering & Technology</h3>
          <hr />
          <p>A deep passion for software engineering, system architecture, and 
            technology leadership — crafting scalable solutions that drive innovation 
            and push the boundaries of what’s possible.</p>
        </div>

        <div class="topic">
          <span class="icon">🛰️</span>
          <h3>Science & Innovation</h3>
          <hr />
          <p>A passion for exploring space, artificial intelligence, and 
            cloud computing — unraveling the possibilities of technology and 
            its role in shaping the future of scientific discovery.</p>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
  .explore-topics {
      padding: 50px 0;
      background: #f8f9fa;
  }

  .topics-container {
      display: flex;
      justify-content: center;
      gap: 20px;
      align-items: stretch;
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
  }

  .topic {
      flex: 1;
      max-width: 320px;
      min-width: 250px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start; 
      align-items: center;
      padding: 20px;
      border-radius: 10px;
      background: white;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
  }

  .topic:hover {
      transform: translateY(-5px);
      box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
  }

  .icon {
      font-size: 40px;
      margin-bottom: 10px;
  }

  h3 {
      margin: 0;
      font-size: 20px;
      font-weight: bold;
      text-align: center;
  }

  hr {
      width: 50%;
      margin: 10px auto;
      border: none;
      height: 2px;
      background: #ddd;
  }

  p {
      text-align: center;
      font-size: 14px;
      color: #555;
      line-height: 1.6;
  }

  @media (max-width: 900px) {
      .topics-container {
          flex-direction: column;
          align-items: center;
      }

      .topic {
          max-width: 280px;
          min-width: 220px;
      }
  }
</style>