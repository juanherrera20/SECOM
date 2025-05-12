<template>
  <div class="seleccionar-municipio">
    <label for="municipio">Selecciona un municipio:</label>
    <select id="municipio" v-model="municipioSeleccionado" required>
      <option v-for="municipio in municipios" :key="municipio.id" :value="municipio.id">
        {{ municipio.name }} ({{ municipio.departamento.name }})
      </option>
    </select>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { getMunicipios } from '../services/ubicacion.js';

// Propiedad que recibe el valor seleccionado para el v-model
const props = defineProps({
  modelValue: {
    type: Number,
    default: null,
  },
});

// Emitir cambios al padre
const emit = defineEmits(['update:modelValue']);

const municipios = ref([]);  // Almacena los municipios cargados
const municipioSeleccionado = ref(props.modelValue);  // Valor de la selección, por defecto es el valor recibido

// Cargar municipios al montar el componente
onMounted(async () => {
  try {
    municipios.value = await getMunicipios();
  } catch (error) {
    console.error('Error al cargar los municipios:', error);
  }
});

// Vigilar cambios en la selección y emitir al componente padre
watch(municipioSeleccionado, (newValue) => {
  emit('update:modelValue', newValue);  // Emitir el valor al componente padre
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