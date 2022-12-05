import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import SomeDoor from '../components/SomeDoor.vue'
import Trending from '@/components/Trending.vue'
import DetailPage from '@/components/DetailPage.vue'
import SearchPage from '@/components/SearchPage.vue'
import LoginPage from '@/components/LoginPage.vue'
import Destination from '@/components/lda.html'
import { createApp } from 'vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomePage
  },
  {
    path: '/open',
    name: 'SomeDoor',
    component: SomeDoor
  },
  {
    path: '/trending',
    name: 'Trending',
    component: Trending
  },
  {
    path: '/detail',
    name: 'DetailPage',
    component: DetailPage
  },
  {
    path: '/search',
    name: 'SearchPage',
    component: SearchPage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
