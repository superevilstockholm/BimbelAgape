import { createRouter, createWebHistory } from 'vue-router'
import homeView from '@/views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: homeView
  },
  {
    path: '/teachers',
    name: 'teachers',
    component: () => import('@/views/TeachersView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router