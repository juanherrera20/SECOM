<template>
    <div class="cargar-imagenes">
      <label for="imagenes">📷 Imágenes del evento:</label>
      <input
        type="file"
        id="imagenes"
        multiple
        accept="image/*"
        @change="manejarCambioImagenes"
      />
      <div class="vista-previa">
        <!-- Mostrar imágenes existentes -->
        <div v-for="(imagen, index) in imagenesExistente" :key="index" class="imagen-container">
          <img :src="imagen.url_imagen" :alt="'Imagen ' + (index + 1)" class="imagen" />
          <button @click="eliminarImagenExistente(index)" class="eliminar-btn">🗑️</button>
        </div>
        <!-- Mostrar nuevas imágenes -->
        <div v-for="(imagen, index) in imagenes" :key="'nueva-' + index" class="imagen-container">
          <img :src="imagen.url" :alt="'Imagen ' + (index + 1)" class="imagen" />
          <button @click="eliminarImagen(index)" class="eliminar-btn">🗑️</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const props = defineProps({
    imagenesExistente: {
      type: Array,
      default: () => [],
    },
  });
  
  const imagenes = ref([]);
  const imagenesEliminadas = ref([]);
  
  const manejarCambioImagenes = (event) => {
    const archivos = event.target.files;
    for (let i = 0; i < archivos.length; i++) {
      const archivo = archivos[i];
      const url = URL.createObjectURL(archivo);
      imagenes.value.push({ archivo, url });
    }
  };
  
  const eliminarImagen = (index) => {
    imagenes.value.splice(index, 1);
  };
  
  const eliminarImagenExistente = (index) => {
    imagenesEliminadas.value.push(props.imagenesExistente[index].id);
    props.imagenesExistente.splice(index, 1);
  };
  
  defineExpose({
    imagenes,
    imagenesEliminadas,
  });
  </script>
  
  <style scoped>
  /* Estilos (iguales a los anteriores) */
  </style>