<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { ref, onMounted } from 'vue';
import { getCurrentUser, getUserDetail } from '../services/users';

const user = ref({
    img_profile: '',
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    telefono: '',
});

onMounted(async () => {
  try {
    // Obtener usuario autenticado
    const currentUser = await getCurrentUser();

    // Obtener detalles del usuario con su ID
    const userResponse = await getUserDetail(currentUser.id);
    user.value = userResponse;
  } catch (error) {
    console.error('Error al cargar datos:', error);
  }
});
</script>


<template>
  <div class="perfil-container">
    <div class="perfil-card">
      <div class="perfil-header">
        <button class="editar-btn" title="Editar perfil">
          <font-awesome-icon icon="pen" />
        </button>
        <div class="perfil-img-placeholder">
          <img v-if="user.img_profile" :src="user.img_profile" alt="Foto de perfil" class="foto-perfil" />
          <font-awesome-icon v-else :icon="['fas', 'user']" class="icon" />
        </div>
        <div class="perfil-info">
          <h2 class="perfil-nombre">{{ user.first_name }} {{ user.last_name }}</h2>
          <p class="perfil-username">@{{ user.username }}</p>
          <p class="perfil-contacto">{{ user.email }} - {{ user.telefono || 'Sin número' }}</p>
        </div>
        <button class="editar-btn">
          <font-awesome-icon icon="pen" />
        </button>
      </div>

      <div class="perfil-favoritos">
        <button class="favoritos-btn">
          Favoritos <font-awesome-icon icon="heart" />
        </button>
      </div>

      <div class="perfil-productos">
        <h3 class="productos-title">PRODUCTOS</h3>
        <p class="no-productos">No tienes productos disponibles</p>
      </div>
    </div>
  </div>
</template>


<style scoped>
.perfil-container {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.perfil-card {
  background-color: #f5f5f5;
  width: 100%;
  max-width: 700px;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}

.perfil-header {
  display: flex;
  align-items: center;
  position: relative;
}

.perfil-img-placeholder {
  background-color: #0d4e49;
  color: white;
  font-size: 2.5rem;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
}

.perfil-info {
  flex-grow: 1;
}

.perfil-nombre {
  margin: 0;
  font-size: 30px;
  font-weight: bold;
  color: #111;
}

.perfil-username,
.perfil-contacto {
  margin: 2px 0;
  font-size: 0.95rem;
  color: #333;
}

.editar-btn {
  position: absolute;
  top: 0;
  right: 0;
  background-color: transparent;
  border: none;
  cursor: pointer;
  color: #0d4e49;
  font-size: 1.1rem;
}

.perfil-favoritos {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

.favoritos-btn {
  background-color: #357a73;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 6px;
}

.perfil-productos {
  margin-top: 20px;
  background-color: #0d4e49;
  color: white;
  padding: 10px;
  border-radius: 4px;
}

.productos-title {
  margin: 0;
  font-weight: bold;
  font-size: 1.1rem;
}

.no-productos {
  background-color: #f5f5f5;
  color: #333;
  padding: 15px;
  border-radius: 4px;
  margin-top: 10px;
  text-align: center;
}

@media (max-width: 600px) {
  .perfil-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .editar-btn {
    top: 10px;
    right: 10px;
  }

  .perfil-favoritos {
    justify-content: center;
  }
}

.foto-perfil {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #ccc;
}

.editar-btn {
  background-color: transparent;
  border: none;
  color: #444;
  font-size: 16px;
  cursor: pointer;
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 8px;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

.editar-btn:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

</style>
