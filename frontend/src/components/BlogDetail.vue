<template>
    <section class="blog-detail-container">
        <div class="content-wrapper">
            <header class="page-header">
                <h2 class="page-title">📝 Blog - Details</h2>
            </header>

            <div v-if="loading" class="loading">Loading...</div>
            <div v-else-if="blogPost">
                <h2 class="post-title">{{ blogPost.title }}</h2>
                <p class="date">{{ formatDate(blogPost.created_at) }}</p>
                <div class="content" v-html="renderMarkdown(blogPost.content)"></div>
                
                <div class="button-container">
                    <router-link to="/blog" class="action-btn back-btn">← Back to Blog</router-link>
                    <router-link :to="`/blog/${blogPost.id}/edit`" class="action-btn edit-btn">✏️ Edit Post</router-link>            
                </div>        
            </div>
            <div v-else class="error">Blog post not found.</div>
        </div>
    </section>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { marked } from 'marked';

const route = useRoute();
const blogPost = ref(null);
const loading = ref(true);

onMounted(async () => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/blog/posts/${route.params.id}/`);
        if (!response.ok) throw new Error("Post not found");
        blogPost.value = await response.json();
    } catch (error) {
        console.error("Error fetching blog post:", error);
        blogPost.value = null;
    } finally {
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

const renderMarkdown = (content) => {
    return marked(content);
};
</script>
  
<style scoped>
/* 🔹 Consistent Layout with About & Blog Pages */
.blog-detail-container {
    padding: 60px 0;
    /* background: #f8f9fa; */
}

/* 🔹 Matches About Page */
.content-wrapper {
    max-width: 900px;
    margin: 30px auto 40px; /* Top margin adjustment */
    text-align: left;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

/* 🔹 Page Header */
.page-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 25px;
    padding-bottom: 12px;
    border-bottom: 3px solid #ddd;
}

.page-title {
    font-size: 28px;
    font-weight: bold;
}

/* 🔹 Loading/Error Messages */
.loading, .error {
    font-size: 18px;
    color: #555;
    text-align: center;
}

/* 🔹 Blog Post Title */
.post-title {
    font-size: 24px;
    color: #222;
    font-weight: bold;
    margin-bottom: 10px;
}

/* 🔹 Date Formatting */
.date {
    font-size: 14px;
    color: #888;
    font-style: italic;
}

/* 🔹 Content Styling */
.content {
    font-size: 16px;
    line-height: 1.6;
    margin-top: 20px;
    margin-bottom: 50px;
}

.content h1, .content h2, .content h3 {
    color: #222;
}

.content code {
    background: #f4f4f4;
    padding: 5px;
    border-radius: 5px;
}

.content pre {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
}

/* 🔹 Button Container */
.button-container {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
}

/* 🔹 Button Styles (Matches Blog Page) */
.action-btn {
    padding: 10px 15px;
    font-size: 14px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 5px;
    display: inline-block;
    transition: background 0.3s ease-in-out;
}

/* Edit Button */
.edit-btn {
    background: #ead9a5;
    color: #4e4d4d;
}

.edit-btn:hover {
    background: #e0a800;
}

/* Back Button */
.back-btn {
    background: #8bb0d9;
    color: white;
}

.back-btn:hover {
    background: #0056b3;
}
</style>