<template>
    <div class="container">
        <header class="page-header">
            <h2 class="page-title">📝 Blog</h2>
            <router-link to="/blog/new" class="new-post-btn">+ New Post</router-link>
        </header>
  
        <div v-if="loading" class="loading">Loading blog posts...</div>
  
        <div v-else class="post-list">
            <div v-for="post in blogPosts" :key="post.id" class="blog-post">
                <router-link :to="`/blog/${post.id}`" class="post-title">{{ post.title }}</router-link>
                <p class="date">{{ formatDate(post.created_at) }}</p>
                <p class="content-preview">{{ truncateText(post.content, 200) }}</p>
            </div>
        </div>
    </div>
</template>
  
<script setup>
    import { ref, onMounted } from 'vue';

    const blogPosts = ref([]);
    const loading = ref(true);

    onMounted(async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/blog/posts/');
            blogPosts.value = await response.json();
            loading.value = false;
        } catch (error) {
            console.error("Error fetching blog posts:", error);
            loading.value = false;
        }
    });

    const formatDate = (dateString) => {
        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric', 
            hour: '2-digit', 
            minute: '2-digit', 
            second: '2-digit', 
            hour12: true 
        };
        return new Date(dateString).toLocaleString(undefined, options);
    };

    const truncateText = (text, length) => {
        return text.length > length ? text.substring(0, length) + '...' : text;
    };
</script>
  
<style scoped>
    .container {
        max-width: 900px; 
        margin: 80px auto 40px; 
        text-align: left;
        background: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    .page-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #ddd;
        padding-bottom: 12px;
        margin-bottom: 25px;
    }

    .page-title {
        font-size: 26px;
        font-weight: bold;
        color: #333;
        display: flex;
        align-items: center;
    }

    .new-post-btn {
        padding: 10px 15px;
        background: #81b58d;
        color: white;
        font-weight: bold;
        text-decoration: none;
        border-radius: 5px;
        transition: background 0.3s ease-in-out;
    }

    .new-post-btn:hover {
        background: #2f8a42;
    }

    .post-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .blog-post {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        border-left: 4px solid #c7949b;
    }

    .blog-post:hover {
        transform: translateY(-2px);
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    .post-title {
        font-size: 20px;
        font-weight: bold;
        color: #4267b2;
        text-decoration: none;
        display: block;
        margin-bottom: 5px;
    }

    .post-title:hover {
        text-decoration: underline;
    }

    .date {
        font-size: 14px;
        color: #666;
        margin-bottom: 10px;
    }

    .content-preview {
        font-size: 16px;
        color: #333;
        line-height: 1.5;
    }
</style>