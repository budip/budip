import { createRouter, createWebHistory } from 'vue-router'

import Home from '../components/Home.vue'
import Blog from '../components/Blog.vue'
import BlogDetail from '../components/BlogDetail.vue'
import CreateBlog from '../components/CreateBlog.vue'
import EditBlog from '../components/EditBlog.vue'
import About from '../components/About.vue'
import Space from '../components/Space.vue'
import AIPage from '../components/AIPage.vue'
import Console from '../components/Console.vue'
import ExploreTopics from '../components/ExploreTopics.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/blog', component: Blog },
  { path: '/blog/:id', component: BlogDetail, props: true },
  { path: '/blog/:id/edit', component: EditBlog, props: true },
  { path: '/blog/new', component: CreateBlog },
  { path: '/edit/:id', component: EditBlog, props: true },
  { path: '/about', component: About },
  { path: '/space', component: Space },
  { path: '/ai', name: 'AI Tools', component: AIPage },
  { path: '/explore', component: ExploreTopics },
  { path: '/console', name: 'Console', component: Console },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router