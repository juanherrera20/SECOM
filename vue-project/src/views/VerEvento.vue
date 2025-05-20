<template>
    <div class="container">
      <div class="event-card">
        <div class="header">
          <img :src="event.images[0]" alt="Imagen del evento" class="event-image" />
          <h2>{{ event.nombre }}</h2>
          <p class="info">📅 Fecha: <strong>{{ event.fecha }}</strong></p>
          <p class="info">📍 Ubicación: <strong>{{ event.ubicacion.municipio }}, {{ event.ubicacion.departamento }}</strong></p>
          <p class="info">🏠 Dirección: <strong>{{ event.ubicacion.direccion }}</strong></p>
          <p class="info">👤 Organizador: <strong>{{ user.first_name }} {{ user.last_name }}</strong></p>
          <p class="info">✉️ Contacto: <strong>{{ user.email }}</strong></p>
          <span class="badge">{{ event.causa }}</span>
        </div>
  
        <div class="gallery">
          <img
            v-for="(image, index) in event.images"
            :key="index"
            :src="image"
            :alt="'Imagen ' + (index + 1)"
            class="gallery-image"
          />
        </div>
  
        <div class="description">
          <h3>📝 Descripción del evento</h3>
          <p>{{ event.descripcion }}</p>
        </div>
  
        <div class="donations">
          <h3>🎁 Categoría de donaciones aceptadas</h3>
          <p class="typeDonac">{{ event.donacion }}</p>
        </div>
  
        <div class="button-container">
          <ButtonDefault
            v-if="isOrganizer"
            size="default"
            color="verde"
            text="Editar Evento"
            class="editar-btn"
            @click="EditarEvento"
          />
          <ButtonDefault
            v-else
            size="default"
            color="azul"
            text="Ayudar"
            class="ayudar-btn"
          />
        </div>
      </div>
      
    </div>
    <FooterComponent />
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';

  import { getCurrentUser, getUserDetail } from '../services/users';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  
  const route = useRoute();
  const router = useRouter();
  const eventoId = route.params.id;
  
  const event = ref({
    nombre: '',
    fecha: '',
    organizador: '',
    causa: '',
    descripcion: '',
    ubicacion: {
      municipio: '',
      departamento: '',
      direccion: '',
    },
    donacion: '',
    images: [],
  });
  
  const user = ref({ first_name: '', last_name: '', email: '' });
  const currentUser = ref(null);
  const isOrganizer = ref(false);
  
  onMounted(async () => {
    try {
      // Obtener evento
      const eventoResponse = await getEventoById(eventoId);
      const imagenesResponse = await getImagenesByEventoId(eventoId);
  
      event.value = {
        ...eventoResponse,
        images: imagenesResponse.map((imagen) => imagen.url_imagen),
      };
  
      // Obtener detalles del organizador
      const userResponse = await getUserDetail(eventoResponse.organizador);
      user.value = userResponse;
  
      // Obtener usuario autenticado
      const currentUserResponse = await getCurrentUser();
      currentUser.value = currentUserResponse;
  
      // Verificar si el usuario autenticado es el organizador
      isOrganizer.value = currentUserResponse?.id === eventoResponse.organizador;
    } catch (error) {
      console.error('Error al cargar datos:', error);
    }
  });
  
  const EditarEvento = () => {
    router.push({ name: 'EditarEvento', params: { id: eventoId } });
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .event-card {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
  }
  
  .header {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .event-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .info {
    margin: 8px 0;
    font-size: 16px;
    color: #555;
  }
  
  .badge {
    display: inline-block;
    padding: 6px 12px;
    background-color: #4caf50;
    color: white;
    border-radius: 20px;
    font-size: 14px;
    margin-top: 10px;
  }
  
  .gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 10px;
    margin: 20px 0;
  }
  
  .gallery-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .description {
    margin: 20px 0;
  }
  
  .description h3 {
    font-size: 20px;
    color: #2c3e50;
  }
  
  .description p {
    font-size: 16px;
    color: #555;
  }
  
  .donations {
    margin: 20px 0;
  }
  
  .donations h3 {
    font-size: 20px;
    color: #2c3e50;
  }
  
  .typeDonac {
    font-size: 16px;
    color: #555;
  }
  
  .button-container {
    text-align: center;
    margin: 20px 0;
  }
  
  .editar-btn {
    background-color: #4caf50;
  }
  
  .ayudar-btn {
    background-color: #2196f3;
  }
  </style>