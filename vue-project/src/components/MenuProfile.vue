<script setup>
import { logout as logoutService } from '../services/Authentication';
import { useRouter } from 'vue-router';

const router = useRouter();

const handleLogout = async () => {
  try {
    await logoutService();
    alert('Sesión cerrada exitosamente');
    router.push('/'); // Redirigir a la página de inicio
  } catch (error) {
    console.error('Error al cerrar sesión:', error);
  }
};
</script>

<template>
  <div class="container">
    <ul class="menu_categ">
      <li class="li">
        <a href="#" class="link">Seguimiento 
          <span class="material-symbols-outlined">sticky_note_2</span>
        </a>
      </li>
      <li class="li">
        <router-link to="/EditPerfil" class="link">Configuración 
          <span class="material-symbols-outlined">manufacturing</span>
        </router-link>
      </li>
      <li class="li">
        <router-link to="/VerPerfil" class="link">Perfil 
          <span class="material-symbols-outlined">account_circle</span>
        </router-link>
      </li>
      <li class="li">
        <a href="#" class="link" @click.prevent="handleLogout">Salir 
          <span class="material-symbols-outlined">logout</span>
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>
a { font-size: 14px; }
span { font-size: 21px; }

.menu_despl {
  position: relative; /* Permite que el menú se posicione con respecto a este */
}

.menu_categ {
  list-style: none;
  position: absolute;
  right: 0; /* Asegura que el menú aparezca justo debajo del perfil */
  top: 50px; /* Ajusta la distancia desde la imagen de perfil */
  background-color: #15323f;
  padding: 10px;
  min-width: 150px; /* Evita que el menú sea demasiado estrecho */
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Agrega una sombra para visibilidad */
  border-radius: 5px; /* Bordes redondeados */
  z-index: 1000; /* Asegura que esté por encima de otros elementos */
}

.menu_categ a {
  color: white;
  text-decoration: none;
  display: block; /* Asegura que cada enlace ocupe todo el ancho */
  padding: 8px 15px;
}

.li {
  list-style: none;
  margin: 0;
}

.li:hover a {
  color: green;
  background-color: rgba(255, 255, 255, 0.1); /* Pequeño cambio de color al pasar el mouse */
  border-radius: 3px;
}
</style>
