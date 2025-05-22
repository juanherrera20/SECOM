<script setup>
import { ref } from 'vue'

const visible = ref(true)

defineProps({
  title: String,
  message: String
})

</script>


<template>
  <div class="alert" v-if="visible">
    <font-awesome-icon icon="circle-check" class="alert-icon" />
    <div class="alert-content">
      <strong class="alert-title">{{ title }}</strong>
      <p class="alert-message">{{ message }}</p>
    </div>
    <button class="alert-close" @click="visible = false" aria-label="Cerrar">
      <font-awesome-icon icon="xmark" />
    </button>
  </div>
</template>


<style scoped>
.alert {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  border: 1px solid #808080;
  background-color: #fff;
  padding: 16px;
  border-radius: 3px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
  max-width: 400px;
  width: calc(100% - 40px);
}

.alert-icon {
  font-size: 24px;
  color: #16a34a;
  flex-shrink: 0;
}

.alert-content {
  flex: 1;
}

.alert-title {
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.alert-message {
  font-size: 14px;
  color: #374151;
  margin-top: 4px;
}

.alert-close {
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  border-radius: 50%;
  color: #6b7280;
  transition: background-color 0.2s ease;
}

.alert-close:hover {
  background-color: #f3f4f6;
  color: #111827;
}
</style>
