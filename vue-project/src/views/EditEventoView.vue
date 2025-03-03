<template>
    <FormularioEvento :eventoId="eventoId" />
</template>
  
<script setup>
    import { useRoute } from 'vue-router';
    import FormularioEvento from '@/components/FormularioEvento.vue';

    const route = useRoute();
    const eventoId = route.params.id; // Obtener el ID del evento desde la ruta
</script>