<script setup>
import { ref } from 'vue'

defineProps(['visible', 'chat'])
const emit = defineEmits(['cerrar'])

const mensaje = ref('')

const enviarMensaje = () => {
  if (mensaje.value.trim()) {
    console.log(`Mensaje a ${chat.nombre}:`, mensaje.value)
    mensaje.value = ''
  }
}
</script>

<template>
  <div v-if="visible" class="modal-container">
    <div class="modal-content">
      <button class="close-button" @click="$emit('cerrar')">✖</button>
      <h2 class="modal-title">Chat con {{ chat.nombre }}</h2>

      <div class="chat-messages">
        <div class="message received">Hola, ¿sigues interesado?</div>
        <div class="message sent">Sí, aún estoy interesado</div>
      </div>

      <div class="chat-input">
        <input v-model="mensaje" placeholder="Escribe un mensaje..." />
        <button @click="enviarMensaje">Enviar</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-container {
  position: fixed;
  top: 80px;
  right: 80px;
  z-index: 10000;
  width: 400px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
  padding: 20px;
}

.close-button {
  position: absolute;
  right: 12px;
  top: 10px;
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
}

.modal-title {
  font-weight: bold;
  margin-bottom: 10px;
}

.chat-messages {
  height: 200px;
  overflow-y: auto;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.message {
  max-width: 75%;
  padding: 8px 12px;
  border-radius: 10px;
}

.received {
  background: #eee;
  align-self: flex-start;
}

.sent {
  background: #cef;
  align-self: flex-end;
}

.chat-input {
  display: flex;
  gap: 10px;
}

.chat-input input {
  flex-grow: 1;
  padding: 6px;
}
</style>
