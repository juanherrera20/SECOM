<template>
  <div class="card" :class="{ 'highlight': chat.nuevo }">
    <img class="profile-pic" :src="Image4" alt="foto" />
    <div class="info">
      <span class="name cursor" @click="$emit('abrirChatPrivado', chat)">{{ chat.nombre }}</span>
      <p class="message">{{ chat.mensaje }}</p>
      <span class="timestamp" :class="{ 'new': chat.nuevo }">{{ chat.tiempo }}</span>
    </div>
    <img class="product" :src="Image4" alt="producto" />
  </div>
</template>

<script setup>
import Image4 from '../assets/Imgs-para-categorias/Image4.png'

defineProps(['chat'])
defineEmits(['abrirChatPrivado'])

</script>

<style scoped>
.card {
  border: 2px solid #ccc;
  border-radius: 6px;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  align-items: center;
}

.profile-pic {
  width: 40px;
  height: 40px;
  border-radius: 100%;
}

.info {
  flex-grow: 1;
  padding: 0 10px;
}

.name {
  font-weight: bold;
  display: block;
}

.message {
  margin: 4px 0;
  font-size: 13px;
}

.timestamp {
  font-size: 0.8rem;
  color: gray;
}

.timestamp.new {
  color: goldenrod;
  font-weight: bold;
}

.product {
  width: 60px;
  height: auto;
}
</style>
