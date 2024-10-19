import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../views/LoginComponent.vue'
import RegisterComponent from '@/views/RegisterComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginComponent,
    },

    {
      path: '/register',
      name: 'register',
      component: RegisterComponent,
    },
    
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue'),
    // },
  ],
})

export default router
