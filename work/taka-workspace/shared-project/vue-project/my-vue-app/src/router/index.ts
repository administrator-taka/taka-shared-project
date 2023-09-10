import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import YoutubeHome from '@/components/youtube-service/YoutubeHome.vue'
import TopComponent from '@/components/TopComponent.vue'
const routes: Array<RouteRecordRaw> = [
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

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
