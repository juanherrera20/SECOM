<template>
  <ul class="menu_categ">
    <li v-for="category in categories" :key="category.id">
      <RouterLink :to="{ name: 'categorias', params: { id: category.id } }" class="lista_categ">
        {{ category.name }}
      </RouterLink>
    </li>
  </ul>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import ProductsService from "../services/products";

const router = useRouter();
const categories = ref([]);

onMounted(async () => {
  try {
    const [categoriesResponse] = await Promise.all([
      ProductsService.getCategories(),
    ]);

    categories.value = categoriesResponse;
    console.log("Categories menu desplegable ", categories.value);
  } catch (error) {
    console.error("Error cargando datos iniciales:", error);
  }
});
</script>

<style>

.menu_categ {
    list-style: none;
    display: none;
    position: absolute;
    background-color: #15323f;
    padding: 3px;
  }
  
  .menu_categ li {
    padding: 2px 0;
  }

  .menu_categ a {
    color: white;
    text-decoration: none;
  }

  .lista_categ:hover {
    color: green;
  }
  
</style>