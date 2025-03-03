import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../views/LoginComponent.vue'
import RegisterComponent from '@/views/RegisterComponent.vue'
import HomeComponent from '@/views/HomeComponent.vue'
import VistaCategorias from '@/views/VistaCategorias.vue'
import GratuitosView from '@/views/GratuitosView.vue'
import EditPerfil from '@/views/EditPerfil.vue'
import CrearEventoView from '@/views/CrearEventoView.vue'
import VerPerfilView from '@/views/VerPerfilView.vue'
import TerminosYCondicionesView from '@/views/TerminosYCondicionesView.vue'
import QuienesSomosView from '@/views/QuienesSomosView.vue'
import AvisoDeActividadView from '@/views/AvisoDeActividadView.vue'
import VenderComponent from '@/views/VenderComponent.vue'
import AddImgsComponent from '@/components/AddImgsComponent.vue'
import EventosList from '@/views/EventosList.vue'
import VerEvento from '@/views/VerEvento.vue'


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
      path: '/CategoriasTecnologia',
      name: 'categoriasTecnologia',
      component: VistaCategorias,
    },

    {
      path: '/Gratuitos',
      name: 'categorias',
      component: GratuitosView,
    },

    {
      path: '/Gratuitos',
      name: 'gratuitos',
      component: GratuitosView,
    },

    {
      path: '/EditPerfil',
      name: 'editperfil',
      component: EditPerfil,
    },

    {
      path: '/CrearEvento',
      name: 'crearevento',
      component: CrearEventoView,
    },

    {
      path: '/VerPerfil',
      name: 'verperfil',
      component: VerPerfilView,
    },

    {
      path: '/TerminosYCondiciones',
      name: 'terminosycondiciones',
      component: TerminosYCondicionesView,
    },

    {
      path: '/QuienesSomosView',
      name: 'quienessomosview',
      component: QuienesSomosView,
    },

    {
      path: '/AvisoDeActividadView',
      name: 'avisodeactividadview',
      component: AvisoDeActividadView,
    },

    {
      path: '/VenderComponent',
      name: 'vendercomponent',
      component: VenderComponent,
    },

    {
      path: '/AddImgsComponent',
      name: 'addimgscomponent',
      component: AddImgsComponent,
    },
    {
      path: '/Eventos',
      name: 'EventosList',
      component: EventosList,
    },
    {
      path: '/VerEvento',
      name: 'verevento',
      component: VerEvento,
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


