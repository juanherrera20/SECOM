<!-- src/components/EventosList.vue -->
<template>
  <div class="eventos-list">
    <h1>Eventos</h1>
    <button class="add-event-button" @click="navigateToAddEvent">Agregar Evento +</button>
    <div v-if="loading">Cargando...</div>
    <div v-else class="eventos-container">
      <div 
        v-for="evento in eventos" 
        :key="evento.id" 
        class="evento-card"
        @click="navigateToEvento(evento.id)" 
      >
        <div class="evento-image" v-if="evento.image">
          <img :src="evento.image" alt="Imagen del evento" />
        </div>
        <div class="evento-info">
          <h2>{{ evento.name }}</h2>
          <p><strong>Fecha:</strong> {{ formatFecha(evento.meet_date) }}</p>
          <p v-if="evento.ubicacion">
            <strong>Ubicación:</strong> 
            {{ evento.ubicacion.address || 'Dirección no disponible' }}, 
            {{ evento.ubicacion.city?.name || 'Ciudad no Definida' }}, 
            {{ evento.ubicacion.city?.departamento || 'Departamento no Definido' }}
          </p>
          <p v-else>
            <strong>Ubicación:</strong> No disponible
          </p>
          <p><strong>Donaciones:</strong> {{ evento.type_donation }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import EventosService  from '../services/eventos';

// // Definimos la estructura de un evento
// const eventoStructure = {
//   id: null,
//   nombre: '',
//   fecha: '',
//   causa: '',
//   ubicacion: {
//     id: null,
//     municipio: '',
//     departamento: '',
//     nombre: '',
//     direccion: '',
//     latitud: '',
//     longitud: '',
//   },
//   image: null,
// };

// Estado reactivo
const eventos = ref([]);
const loading = ref(true);
const router = useRouter();

// Función para formatear la fecha
const formatFecha = (fecha) => {
  return new Date(fecha).toLocaleDateString();
};

// Función para navegar a la vista de agregar evento
const navigateToAddEvent = () => {
  router.push({ name: 'crearevento' });
};

// Función para navegar a la vista individual del evento
const navigateToEvento = (eventoId) => {
  router.push({ name: 'verevento', params: { id: eventoId } });
};

// Cargar eventos al montar el componente
onMounted(async () => {
  try {
    const [ eventosResponse, ] = await Promise.all([
      EventosService.getEventos(),
    ]);
    eventos.value = eventosResponse

    console.log('Eventos cargados:', eventos.value);
    loading.value = false;

  } catch (error) {
    console.error('Error al cargar los eventos:', error);
  } 
});
</script>

<style scoped>
.eventos-list {
  padding: 20px;
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
}

.add-event-button {
  position: absolute;
  top: 20px;
  right: 20px;
  background-color: #2c3e50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.add-event-button:hover {
  background-color: #34495e;
}

.eventos-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 60px;
}

.evento-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-top: 4px solid #4CAF50; /* Borde verde en la parte superior */
  cursor: pointer; /* Cambia el cursor al pasar sobre la tarjeta */
}

.evento-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.evento-image {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.evento-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.evento-info {
  padding: 16px;
  flex: 1;
}

.evento-info h2 {
  margin-top: 0;
  font-size: 20px;
  color: #2c3e50;
}

.evento-info p {
  margin: 8px 0;
  font-size: 14px;
  color: #555;
}

.evento-info p strong {
  color: #333;
}
</style>