<script setup>
import { computed , ref } from 'vue';

// Definir props para el tamaño, color y texto del botón
const props = defineProps({
  size: {
    type: String,
    default: 'default', // Valores permitidos: 'default', 'lg', 'sm'
  },
  color: {
    type: String,
    default: '#2B6682', // Color predeterminado del botón
  },
  text: {
    type: String,
    default: 'Guardar', // Texto predeterminado del botón
  },
  icono: {
    type:  String,
    default: '',
  }
});

// Computar la clase para el tamaño del botón
const buttonSizeClass = computed(() => {
  switch (props.size) {
    case 'lg':
      return 'large';
    case 'sm':
      return 'small';
    default:
      return 'default';
  }
});


</script>

<template>
  <button :class="['button', buttonSizeClass, props.color]"> {{ text }} <span class="material-symbols-outlined">{{ props.icono }}</span></button>
</template>

<style scoped>
/* Estilos base para el botón */
.button {
  font-family: 'Aldrich', sans-serif;
  color: white;
  border-radius: 10px;
  border: 0;
  cursor: pointer;
}

/* Color azul */
.azul {
    background-color: #2B6682;
} 
.azul:hover {
    background-color: #4197C0;
    color: whitesmoke;
}

/* Color verde */
.verde {
    background-color: #0D7643;
} 
.verde:hover {
    background-color: #1C957C;
    color: whitesmoke;
}

/* Tamaño por defecto */
.default {
  width: 140px;
  height: 40px;
  font-size: 14px;
}

/* Tamaño grande */
.large {
  width: 170px;
  height: 50px;
  font-size: 16px;
}

/* Tamaño pequeño */
.small {
  width: 110px;
  height: 30px;
  font-size: 12px;
}
</style>
