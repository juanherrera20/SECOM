<script setup>
import { ref } from 'vue';

const props = defineProps(['size','color','text'])
</script>


<template>
<button class="default">Guardar</button>
</template>


<style scoped>
.default {
    font-family: 'Aldrich', sans-serif;
    width: 130px;
    height: 40px;
    font-size: 14px;
    color: white;
    background-color: #2B6682;
    border-radius: 10px;
    border: 0;
}
</style>