import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/youtube-service/YoutubeHome.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/test',
      name: 'home',
      component: Home
    },
    // 他のルートをここに追加できます
  ]
})

export default router
