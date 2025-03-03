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
        <div v-for="(imagen, index) in imagenes" :key="index" class="imagen-container">
          <img :src="imagen.url" :alt="'Imagen ' + (index + 1)" class="imagen" />
          <button @click="eliminarImagen(index)" class="eliminar-btn">🗑️</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const imagenes = ref([]);
  
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
  
  defineExpose({
    imagenes,
  });
  </script>
  
  <style scoped>
  .cargar-imagenes {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #2c3e50;
  }
  
  input[type="file"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    background-color: #fff;
    transition: border-color 0.3s ease;
  }
  
  input[type="file"]:focus {
    border-color: #4CAF50;
    outline: none;
  }
  
  .vista-previa {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 10px;
  }
  
  .imagen-container {
    position: relative;
    width: 100px;
    height: 100px;
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
  }
  
  .imagen {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .eliminar-btn {
    position: absolute;
    top: 5px;
    right: 5px;
    background-color: rgba(255, 0, 0, 0.7);
    border: none;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    padding: 5px;
  }
  
  .eliminar-btn:hover {
    background-color: rgba(255, 0, 0, 1);
  }
  </style>