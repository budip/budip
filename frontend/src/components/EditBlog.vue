<template>
    <section class="edit-blog-container">
        <div class="content-wrapper">
            <header class="page-header">
                <h2 class="page-title">📝 Blog - Edit Post</h2>
            </header>        

            <form @submit.prevent="updatePost">
                <div class="form-group">
                    <label for="title">Title:</label>
                    <input type="text" id="title" v-model="title" required />
                </div>
        
                <div class="form-group">
                    <label for="content">Content (Markdown Supported):</label>
                    <textarea id="content" v-model="content" required></textarea>
                </div>
        
                <div class="button-container">
                    <button type="submit" class="action-btn save-btn">💾 Save Changes</button>
                    <button type="button" class="action-btn cancel-btn" @click="cancelEdit">❌ Cancel</button>
                    <button type="button" class="action-btn delete-btn" @click="deletePost">🗑️ Delete</button>
                </div>
            </form>
      
            <div v-if="successMessage" class="success-message">
                ✅ Blog post updated! <router-link :to="`/blog/${postId}`">View post</router-link>
            </div>
        </div>
    </section>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const postId = route.params.id;

const title = ref('');
const content = ref('');
const successMessage = ref(null);

onMounted(async () => {
    try {
        const response = await fetch(`/api/posts/${postId}/`);
        if (!response.ok) throw new Error("Post not found");
        const post = await response.json();
        title.value = post.title;
        content.value = post.content;
    } catch (error) {
        console.error("Error fetching blog post:", error);
    }
});

const updatePost = async () => {
  try {
    const response = await fetch(`/api/posts/${postId}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: title.value,
        content: content.value
      })
    });

    if (!response.ok) {
      throw new Error("Failed to update post");
    }

    successMessage.value = "Blog post updated!";
    setTimeout(() => router.push(`/blog/${postId}`), 2000);
  } catch (error) {
    console.error("Error updating blog post:", error);
  }
};

const deletePost = async () => {
  if (!confirm("Are you sure you want to delete this post?")) return;

  try {
    const response = await fetch(`/api/posts/${postId}/`, {
      method: 'DELETE',
    });

    if (response.ok) {
      router.push('/blog');
    } else {
      throw new Error("Failed to delete post");
    }
  } catch (error) {
    console.error("Error deleting blog post:", error);
  }
};

const cancelEdit = () => {
    router.push(`/blog/${postId}`);
};
</script>
  
<style scoped>
.edit-blog-container {
    padding: 0 0;
}

.content-wrapper {
    max-width: 900px;
    margin: 30px auto 40px;
    text-align: left;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

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

.button-container {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
}

.success-message {
    margin-top: 15px;
    padding: 10px;
    background: #d4edda;
    color: #155724;
    border-radius: 5px;
    text-align: center;
}

.action-btn {
    padding: 10px 15px;
    font-size: 14px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 5px;
    display: inline-block;
    transition: background 0.3s ease-in-out;
}

.save-btn {
    background: #ccd9e8;
    color: #4e4d4d;
    border: none;
    cursor: pointer;
}

.save-btn:hover {
    background: #5598e0;
}

.cancel-btn {
    background: #dad8d8;
    color: #4e4d4d;
    border: none;
    cursor: pointer;
}

.cancel-btn:hover {
    background: #ea8591;
}

.delete-btn {
  background: #f8d7da;
  color: #721c24;
  border: none;
  cursor: pointer;
}

.delete-btn:hover {
  background: #f5c6cb;
}
</style>