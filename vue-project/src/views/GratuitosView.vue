<template>
  <ProductsList :defaultFree="true" />
</template>

<script setup>
import { useRoute } from 'vue-router';
import ProductsList from '../components/ProductsList.vue';

const route = useRoute();
// const categoria = route.params.id;
</script>
