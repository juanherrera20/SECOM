<!--Dejo esto como esta para que vea como es la estructura por defecto del App.Vue cuando se instala router-->
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<!--Limpie todo lo que venia por defecto, si mira el video aparecia la información basica de Vue--> 
<!--Aquí se van poniento las rutas para ir manejando el direccionamiento-->
<!-- <nav> 
  <RouterLink to="/register">Register</RouterLink>
</nav> -->

<RouterView />
</template>

<style>
/* Configuraciones generales para todas las vistas*/
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: white;
  font-family: 'Aldrich', sans-serif;
  height: 100vh;
  margin: 0;
  padding: 0;
}
</style>
