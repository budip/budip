import { createRouter, createWebHistory } from 'vue-router'

import Home from '../components/Home.vue'
import Blog from '../components/Blog.vue'
import BlogDetail from '../components/BlogDetail.vue'
import CreateBlog from '../components/CreateBlog.vue'
import EditBlog from '../components/EditBlog.vue'
import About from '../components/About.vue'
import Space from '../components/Space.vue'
import AIChat from '../components/AIChat.vue'
import ExploreTopics from '../components/ExploreTopics.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/blog', component: Blog },
  { path: '/blog/:id', component: BlogDetail, props: true },
  { path: '/create', component: CreateBlog },
  { path: '/edit/:id', component: EditBlog, props: true },
  { path: '/about', component: About },
  { path: '/space', component: Space },
  { path: '/ai', component: AIChat },
  { path: '/explore', component: ExploreTopics },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router