<template>
    <div class="seleccionar-municipio">
      <label for="municipio">Selecciona un municipio:</label>
      <select id="municipio" v-model="municipioSeleccionado" required>
        <option v-for="municipio in municipios" :key="municipio.id" :value="municipio.id">
          {{ municipio.nombre }} ({{ municipio.departamento.nombre }})
        </option>
      </select>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue';
  import { getMunicipios } from '../services/ubicacion.js';
  
  const props = defineProps({
    modelValue: {
      type: Number,
      default: null,
    },
  });
  
  const emit = defineEmits(['update:modelValue']);
  
  const municipios = ref([]);
  const municipioSeleccionado = ref(props.modelValue);
  
  // Cargar municipios al montar el componente
  onMounted(async () => {
    try {
      municipios.value = await getMunicipios();
    } catch (error) {
      console.error('Error al cargar los municipios:', error);
    }
  });
  
  // Actualizar el valor seleccionado cuando cambie
  watch(municipioSeleccionado, (newValue) => {
    emit('update:modelValue', newValue);
  });
  </script>
  
  <style scoped>
  .seleccionar-municipio {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #2c3e50;
  }
  
  select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    background-color: #fff;
    transition: border-color 0.3s ease;
  }
  
  select:focus {
    border-color: #4CAF50;
    outline: none;
  }
  </style>