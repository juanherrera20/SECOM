<script setup>
import { ref } from 'vue'
import ChatCard from './ChatCard.vue'

defineProps(['visible'])

const ventas = [
  {
    id: 1,
    nombre: 'Stiven Andres Zapata',
    mensaje: 'Camiseta Manga larga negra',
    tiempo: 'Enviado hace 3 horas',
    nuevo: false,
    img: '../assets/Imgs-para-categorias/Image4.png',
    foto: 'stiven.jpg'
  },
  {
    id: 2,
    nombre: 'Arturo sims Gomez',
    mensaje: 'Portátil HP 240 G8',
    tiempo: 'Nuevo Mensaje',
    nuevo: true,
    img: '../assets/Imgs-para-categorias/Image4.png',
    foto: 'arturo.jpg'
  },
]

const compras = [
  {
    id: 3,
    nombre: 'karen Bermudez G.',
    mensaje: 'Celular Nokia 7j negro',
    tiempo: 'Enviado hace 2 minutos',
    nuevo: false,
    img: '../assets/Imgs-para-categorias/Image4.png',
    foto: 'karen.jpg'
  },
  {
    id: 4,
    nombre: 'Cristina Balanta',
    mensaje: 'Short jeans',
    tiempo: 'Enviado hace 1 minuto',
    nuevo: false,
    img: '../assets/Imgs-para-categorias/Image4.png',
    foto: 'cristina.jpg'
  },
]

const emit = defineEmits(['close', 'abrirChatPrivado'])

</script>

<template>
  <div v-if="visible" class="modal-container">
    <div class="modal-content">
        <font-awesome-icon
          icon="xmark"
          class="close-icon"
          @click="emit('close')"
        />

      <h2 class="modal-title">
        CHATS <font-awesome-icon icon="envelope" />
      </h2>

      <section>
        <h3 class="section-title">Ventas <font-awesome-icon icon="arrow-right" /></h3>
        <ChatCard
          v-for="chat in ventas"
          :key="chat.id"
          :chat="chat"
          @abrirChatPrivado="$emit('abrirChatPrivado', chat)"
        />
      </section>

      <section>
        <h3 class="section-title">Compras <font-awesome-icon icon="shopping-cart" /></h3>
        <ChatCard
          v-for="chat in compras"
          :key="chat.id"
          :chat="chat"
          @abrirChatPrivado="$emit('abrirChatPrivado', chat)"
        />
      </section>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-container {
  position: absolute;
  top: 70px; /* ajustar según tu header */
  right: 100px; /* ajustar según posición del ícono */
  z-index: 9999;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0,0,0,0.2);
  width: 400px;
  max-height: 90vh;
  overflow-y: auto;
  padding: 10px 20px;
}

.modal-title {
  font-weight: bold;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  color: $primary_color100;
}

.section-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 6px;
  color: $secondary_color100;
}

.close-icon {
  position: absolute;
  top: 12px;
  right: 16px;
  font-size: 1.2rem;
  cursor: pointer;
  color: #555;
  transition: color 0.2s;
}

.close-icon:hover {
  color: #d00;
}

</style>
