import { createRouter, createWebHistory } from 'vue-router'
import YoutubeHome from './components/youtube-service/YoutubeHome.vue'
import TopComponent from './components/TopComponent.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'TopComponent',
      component: TopComponent
    },    {
      path: '/youtubeHome',
      name: 'YoutubeHome',
      component: YoutubeHome
    },
  ]
})

export default router
