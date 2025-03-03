<!-- src/components/EventosList.vue -->
<template>
    <div class="eventos-list">
      <h1>Eventos</h1>
      <div v-if="loading">Cargando...</div>
      <div v-else>
        <div v-for="evento in eventos" :key="evento.id" class="evento-card">
          <h2>{{ evento.nombre }}</h2>
          <p><strong>Fecha:</strong> {{ formatFecha(evento.fecha) }}</p>
          <p><strong>Ubicación:</strong> {{ evento.ubicacion.direccion }}, {{ evento.ubicacion.municipio.nombre }}, {{ evento.ubicacion.municipio.departamento.nombre }}</p>
          <p><strong>Causa:</strong> {{ evento.causa }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { getEventos } from '../services/eventos';
  
  export default {
    data() {
      return {
        eventos: [],
        loading: true,
      };
    },
    async created() {
      try {
        this.eventos = await getEventos();
      } catch (error) {
        console.error('Error al cargar los eventos:', error);
      } finally {
        this.loading = false;
      }
    },
    methods: {
      formatFecha(fecha) {
        return new Date(fecha).toLocaleDateString();
      },
    },
  };
  </script>
  
  <style scoped>
  .eventos-list {
    padding: 20px;
  }
  
  .evento-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    background-color: #f9f9f9;
  }
  
  .evento-card h2 {
    margin-top: 0;
  }
  
  .evento-card p {
    margin: 8px 0;
  }
  </style>