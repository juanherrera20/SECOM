import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'; //Librería para íconos (por ahora solo para AlertComponent.vue)

// Importar los íconos que se van a usar
import { faCircleCheck, faXmark, faEnvelope, faShoppingCart, faArrowRight, faClock } from '@fortawesome/free-solid-svg-icons';

// Agregar los íconos a la librería
library.add(faCircleCheck, faXmark, faEnvelope, faShoppingCart, faArrowRight, faClock);

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon);
app.use(router)

app.mount('#app')
