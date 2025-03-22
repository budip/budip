<template>
    <section class="create-blog-container">
        <div class="content-wrapper">
            <header class="page-header">
                <h2 class="page-title">📝 Blog - Create New Post</h2>
            </header>        

            <form @submit.prevent="submitPost">
                <div class="form-group">
                    <label for="title">Title:</label>
                    <input type="text" id="title" v-model="title" required />
                </div>
        
                <div class="form-group">
                    <label for="content">Content (Markdown Supported):</label>
                    <textarea id="content" v-model="content" required></textarea>
                </div>
        
                <div class="button-container">
                    <button type="submit" class="action-btn publish-btn">📢 Publish</button>
                    <button type="button" class="action-btn cancel-btn" @click="cancelPost">❌ Cancel</button>
                </div>
            </form>
      
            <div v-if="successMessage" class="success-message">
                🎉 Blog post created! <router-link to="/blog">View all posts</router-link>
            </div>
        </div>
    </section>
</template>
  
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const title = ref('');
const content = ref('');
const successMessage = ref(null);
const router = useRouter();

const submitPost = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/blog/posts/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: title.value, content: content.value })
        });

        if (response.ok) {
            successMessage.value = "Blog post created!";
            title.value = '';
            content.value = '';
            setTimeout(() => router.push('/blog'), 2000);
        } else {
            throw new Error('Failed to create post');
        }
    } catch (error) {
        console.error("Error creating blog post:", error);
    }
};

const cancelPost = () => {
    router.push('/blog');
};
</script>
  
<style scoped>
/* 🔹 Consistent Layout with Blog, Edit, & About Pages */
.create-blog-container {
    padding: 60px 0;
    /* background: #f8f9fa; */
}

/* 🔹 Matches About Page */
.content-wrapper {
    max-width: 900px;
    margin: 30px auto 40px; /* Adjust top margin */
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

/* 🔹 Form Styling */
.form-group {
    margin-bottom: 15px;
}

label {
    font-weight: bold;
    display: block;
    margin-bottom: 5px;
}

input, textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background: #f7f7f7;
    font-size: 16px;
}

textarea {
    height: 400px;
}

/* 🔹 Button Container */
.button-container {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
}

/* 🔹 Success Message */
.success-message {
    margin-top: 15px;
    padding: 10px;
    background: #d4edda;
    color: #155724;
    border-radius: 5px;
    text-align: center;
}

/* 🔹 Buttons */
.action-btn {
    padding: 10px 15px;
    font-size: 14px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 5px;
    display: inline-block;
    transition: background 0.3s ease-in-out;
}

/* Publish Button */
.publish-btn {
    background: #ccd9e8;
    color: #4e4d4d;
    border: none;
    cursor: pointer;
}

.publish-btn:hover {
    background: #5598e0;
}

/* Cancel Button */
.cancel-btn {
    background: #dad8d8;
    color: #4e4d4d;
    border: none;
    cursor: pointer;
}

.cancel-btn:hover {
    background: #ea8591; /* Soft red on hover */
}
</style>