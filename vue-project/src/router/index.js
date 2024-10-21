import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../views/LoginComponent.vue'
import RegisterComponent from '@/views/RegisterComponent.vue'
import HomeComponent from '@/views/HomeComponent.vue'
import VistaCategorias from '@/views/VistaCategorias.vue'
import EditPerfil from '@/views/EditPerfil.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/Login',
      name: 'login',
      component: LoginComponent,
    },

    {
      path: '/',
      name: 'home',
      component: HomeComponent,
    },

    {
      path: '/Register',
      name: 'register',
      component: RegisterComponent,
    },
    
    {
      path: '/Categorias',
      name: 'categorias',
      component: VistaCategorias,
    },

    {
      path: '/EditPerfil',
      name: 'editperfil',
      component: EditPerfil,
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

import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../views/LoginComponent.vue'
import RegisterComponent from '@/views/RegisterComponent.vue'
import HomeComponent from '@/views/HomeComponent.vue'
import EditPerfil from '@/views/EditPerfil.vue'

