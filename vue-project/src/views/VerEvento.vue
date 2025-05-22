<template>
  <div>
    <div class="container">
      <div class="event-card">

        <div class="header">
          <div class="evento-image">
            <img
              v-if="imgEvento.length > 0"
              :src="imgEvento[0].url"
              alt="Imagen principal del evento"
            />
          </div>
          <!--<img :src="event.images[0]" alt="Imagen del evento" class="event-image" />-->
          <h2>{{ event.name }}</h2>
          <p class="info">📅 Fecha: <strong>{{ event.meet_date }}</strong></p>
          <p class="info">📍 Ubicación: <strong>{{ ubicacion.city?.name || 'Ciudad no definida' }}, 
            {{ ubicacion.city?.departamento || 'Departamento no definido' }}</strong>
          </p>
          <p class="info">🏠 Dirección: <strong>{{ ubicacion.address }}</strong></p>
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
          <p>{{ event.description }}</p>
        </div>
  
        <div class="donations">
          <h3>🎁 Categoría de donaciones aceptadas</h3>
          <p class="typeDonac">{{ event.type_donation }}</p>
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
  </div>
  </template>
  
  <script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { getCurrentUser, getUserDetail } from '../services/users';
import ButtonDefault from '@/components/ButtonDefault.vue';
import FooterComponent from '@/components/FooterComponent.vue';

import EventosService from '../services/eventos';

const route = useRoute();
const eventoId = route.params.id;

const router = useRouter();

const donations = ref([]);

const imgEvento = ref([]);

const event = ref({
  name: "",
  meet_date: '',
  description: '',
  type_donation: '',
  donation_id: null,
});

const user = ref({
  first_name: '',
  last_name: '',
  email: ''
});

const currentUser = ref(null);
const isOrganizer = ref(false);

const ubicacion = ref({
  address: '',
  city: {
    name: '',
    departamento: ''
  }
});

onMounted(async () => {
  try {
    // Obtener evento
    const [donationsResponse, eventoResponse, getDonationsByEventoId] = await Promise.all([
      EventosService.getDonations(),
      EventosService.getEventoById(eventoId),
      EventosService.getImagesByEventoId(eventoId)
    ]);

    donations.value = donationsResponse;
    event.value = eventoResponse;
    imgEvento.value = getDonationsByEventoId;

    const donation = donations.value.find(obj => obj.name === event.value.type_donation)
    event.value.donation_id = donation.id

    // Obtener detalles del organizador
    const userResponse = await getUserDetail(eventoResponse.organizador);
    user.value = userResponse;

    // Obtener usuario autenticado
    const currentUserResponse = await getCurrentUser();
    currentUser.value = currentUserResponse;

    // Verificar si el usuario autenticado es el organizador
    isOrganizer.value = currentUserResponse?.id === eventoResponse.organizador;

    // Asignar directamente la ubicación
    ubicacion.value = eventoResponse.ubicacion;

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
  
  .evento-image {
  width: 100%;
  height: 300px;
  overflow: hidden;
  border-radius: 8px;
  }

  .evento-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  h2 {
    margin-top: 15px;
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