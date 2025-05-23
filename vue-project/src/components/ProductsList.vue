<script setup>
import { ref, onMounted, watch, defineProps } from "vue";
import { useRoute, useRouter } from "vue-router";
import FooterComponent from "@/components/FooterComponent.vue";
import ProductTarget from "@/components/ProductTarget.vue";
import ProductsService from "../services/products";

// Router
const route = useRoute();
const router = useRouter();

// Props
const props = defineProps({
  defaultCategoryId: Number,
  defaultOffers: {
    type: Boolean,
    default: false
  },
  defaultFree: {
    type: Boolean,
    default: false
  }
});

// Reactive states
const products = ref([]);
const conditions = ref([]);
const categories = ref([]);
const tags = ref([]);

// Filtros reactivos
const filtros = ref({
  category: null,
  tags: null,  // ahora es valor único, no array
  min_price: null,
  max_price: null,
  condition: '',
  free: props.defaultFree,
  offers: props.defaultOffers,
  ordering: '',
  search: '',
});

// Obtener productos del backend
async function cargarProductos() {
  try {
    const response = await ProductsService.getProducts(filtros.value);
    products.value = response;
  } catch (error) {
    console.error("Error al cargar productos:", error);
  }
}

// onMounted: carga condiciones, categorías, tags iniciales y productos
onMounted(async () => {
  try {
    const [conditionsResponse, categoriesResponse] = await Promise.all([
      ProductsService.getConditions(),
      ProductsService.getCategories()
    ]);

    conditions.value = conditionsResponse;
    categories.value = categoriesResponse;

    if (props.defaultCategoryId) {
      filtros.value.category = props.defaultCategoryId;
      tags.value = await ProductsService.getTags(props.defaultCategoryId);
    } else {
      tags.value = await ProductsService.getTags();
    }

    await cargarProductos();
  } catch (error) {
    console.error("Error al cargar datos iniciales:", error);
  }
});

// Watch para recargar TAGS cuando cambia la categoría
watch(() => filtros.value.category, async (newCategory) => {
    // 🔧 Asegurarse de que filtros.tags es un número
  if (typeof filtros.value.tags === 'object' && filtros.value.tags !== null) {
    filtros.value.tags = filtros.value.tags.id;
  }
  console.log('Filtros antes de cargar productos:', filtros.value);
  try {
    if (newCategory) {
      tags.value = await ProductsService.getTags(newCategory);
    } else {
      tags.value = await ProductsService.getTags();
    }
    filtros.value.tags = null;  // Limpia selección de tags
  } catch (error) {
    console.error("Error al cargar tags:", error);
  }
});

// Watch para recargar productos al cambiar filtros (profundamente)
watch(filtros, async () => {
  await cargarProductos();
}, { deep: true });
</script>

<template>
  <section class="main">
    <section class="compras">
      <p>Compras</p>
    </section>

    <div class="navigation">
      <span class="material-symbols-outlined">home</span>
      <p>Inicio</p>
      <span class="material-symbols-outlined">chevron_left</span>
      <p>Categorías</p>
      <span class="material-symbols-outlined">chevron_left</span>
      <p>Tecnología</p>
      <span class="material-symbols-outlined">chevron_left</span>
      <strong>Todos</strong>
    </div>

    <section class="main-container">
      <!-- Filtros -->
      <article class="filters">
        <!-- Categorías -->
        <div class="inputs-container">
          <h4>CATEGORÍAS</h4>
          <div class="elements">
            <div>
              <input
                type="radio"
                id="category-todos"
                value=""
                v-model="filtros.category"
              />
              <label for="category-todos">Todos</label>
            </div>
            <div v-for="category in categories" :key="category.id">
              <input
                type="radio"
                :id="'category-' + category.id"
                :value="category.id"
                v-model="filtros.category"
              />
              <label :for="'category-' + category.id">{{ category.name }}</label>
            </div>
          </div>
        </div>

        <!-- Etiquetas -->
        <div class="inputs-container">
          <h4>ETIQUETAS</h4>
          <div class="elements">
            <div>
              <input
                type="radio"
                id="tag-todos"
                value=""
                v-model="filtros.tags"
              />
              <label for="tag-todos">Todos</label>
            </div>
            <div v-for="tag in tags" :key="tag.id">
              <input
                type="radio"
                :id="'tag-' + tag.id"
                :value="tag.id"        
                v-model="filtros.tags"
                />
              <label :for="'tag-' + tag.id">{{ tag.name }}</label>
            </div>
          </div>
        </div>

        <!-- Precio -->
        <div class="inputs-container">
          <h4>PRECIO</h4>
          <div class="elements">
            <div class="inputs-precio">
              <input
                type="number"
                class="inputPrecio"
                placeholder="Min. Precio"
                v-model.number="filtros.min_price"
              />
              <input
                type="number"
                class="inputPrecio"
                placeholder="Max. Precio"
                v-model.number="filtros.max_price"
              />
            </div>
          </div>
        </div>

        <!-- Estado -->
        <div class="inputs-container">
          <h4>CONDICIÓN</h4>
          <div class="elements">
            <div v-for="condition in conditions" :key="condition.value">
              <input
                type="radio"
                name="condicion"
                :id="'condicion' + condition.value"
                :value="condition.value"
                v-model="filtros.condition"
              />
              <label :for="'condicion' + condition.value">{{ condition.label }}</label>
            </div>
          </div>
        </div>
      </article>

      <!-- Productos -->
      <article class="products-container">
        <div class="barra">
          <!-- Búsqueda -->
          <div class="barraBuscar">
            <input
              class="inputBuscar"
              type="text"
              placeholder="Buscar"
              v-model="filtros.search"
            />
            <span class="material-symbols-outlined icon">search</span>
          </div>

          <!-- Ordenamiento -->
          <div class="ordenar">
            <label for="ordenarPor">Ordenar Por:</label>
            <div class="barraOrdenar">
              <select
                id="ordenarPor"
                v-model="filtros.ordering"
                class="inputBuscar"
              >
                <option value="">Predeterminado</option>
                <option value="-price">Precio: Mayor a menor</option>
                <option value="price">Precio: Menor a mayor</option>
                <option value="-user__reputacion">Reputación: Mayor a menor</option>
                <option value="user__reputacion">Reputación: Menor a mayor</option>
                <option value="-create_date">Más recientes</option>
                <option value="create_date">Más antiguos</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Resultados -->
        <div class="resultados">
          <div><strong>{{ products.length }}</strong> <p>resultados</p></div>
        </div>

        <!-- Productos -->
        <div class="products">
          <ProductTarget v-for="product in products" :key="product.id" :product="product" />
        </div>

        <ButtonDefault size="default" color="azul" text="Cargar más" icono="autorenew" :style="{ width: '100%' }" />
      </article>
    </section>
  </section>

  <FooterComponent />
</template>

<style scoped>
/* --- Contenedor principal --- */
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 20px;
  max-width: 1400px;
  margin: 0 auto;
  box-sizing: border-box;
}

/* --- Imagen de fondo compras --- */
.compras {
  background-image: url('@/assets/Images/compras.jpg');
  background-size: cover;       /* Ajusta la imagen para cubrir todo el área */
  background-position: center;  /* Centra la imagen */
  box-shadow: 4px 4px 10px rgba(0,0,0,0.5);
  width: 100%;
  max-width: 1400px;
  height: 325px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.compras p {
  font-size: clamp(72px, 10vw, 144px); /* Escala con la pantalla */
  color: whitesmoke;
  text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
  margin: 0;
  font-weight: 700;
}

/* --- Navegación --- */
.navigation {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  max-width: 1400px;
  padding: 10px 20px;
  background-color: #FAFAFA;
  box-shadow: 4px 4px 10px rgba(0,0,0,0.2);
  color: gray;
  font-size: 14px;
  box-sizing: border-box;
  flex-wrap: wrap;
  border-radius: 6px;
}
.navigation p,
.navigation strong {
  margin: 0;
  white-space: nowrap;
}
.navigation strong {
  color: #4197C0;
  font-weight: 600;
}

/* Iconos dentro de navegación */
.navigation .material-symbols-outlined {
  font-size: 20px;
  color: gray;
  user-select: none;
}

/* --- Inputs personalizados --- */
input[type="radio"], input[type="checkbox"] {
  display: none;
}
input[type="radio"] + label,
input[type="checkbox"] + label {
  line-height: 1.8em;
  display: flex;
  align-items: center;
  cursor: pointer;
  font-size: 14px;
  color: #433E3F;
  user-select: none;
}
input[type="radio"] + label:before,
input[type="checkbox"] + label:before {
  content: "";
  display: inline-block;
  margin-right: 10px;
  background: #FAFAFA;
  border: 2px solid #CCCBCB;
  box-sizing: border-box;
  flex-shrink: 0;
  transition: border-color 0.3s ease;
}
input[type="radio"] + label:before {
  width: 20px;
  height: 20px;
  border-radius: 50%;
}
input[type="checkbox"] + label:before {
  width: 18px;
  height: 18px;
  border-radius: 4px;
}
input[type="radio"]:checked + label,
input[type="checkbox"]:checked + label {
  color: #23B89A;
}
input[type="radio"]:checked + label:before {
  border: 4px solid #23B89A;
}
input[type="checkbox"]:checked + label:before {
  border: 4px solid #23B89A;
}

/* --- Filtros y layout --- */
.inputs-container {
  display: flex;
  flex-direction: column;
  padding: 20px 15px;
  border-bottom: 2px solid #CCCBCB;
  gap: 10px;
  width: 100%;
}

.inputs-precio {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}
.inputPrecio {
  background-color: white;
  width: 100%;
  max-width: 140px;
  height: 38px;
  padding: 8px 12px;
  border-radius: 4px;
  border: 1px solid #CCCBCB;
  font-size: 14px;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}
.inputPrecio:focus {
  outline: none;
  border-color: #23B89A;
}

.elements {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 14px;
  color: #433E3F;
}

.main-container {
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 20px;
  background-color: #FAFAFA;
  box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
  padding: 20px;
  width: 100%;
  max-width: 1400px;
  box-sizing: border-box;
}

.filters {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.products {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

/* Barra de búsqueda */
.barraBuscar {
  position: relative;
  max-width: 400px;
  width: 100%;
}
.inputBuscar {
  width: 100%;
  height: 38px;
  padding: 10px 40px 10px 15px;
  border-radius: 4px;
  border: 1px solid #CCCBCB;
  font-size: 14px;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}
.inputBuscar:focus {
  outline: none;
  border-color: #23B89A;
}
.barraBuscar .material-symbols-outlined {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: gray;
  font-size: 20px;
}

/* Barra de ordenamiento */
.barraOrdenar {
  position: relative;
  max-width: 150px;
  width: 100%;
}
.barraOrdenar select {
  width: 100%;
  height: 38px;
  padding: 6px 30px 6px 10px;
  border-radius: 4px;
  border: 1px solid #CCCBCB;
  font-size: 14px;
  appearance: none;
  background: white url('data:image/svg+xml;utf8,<svg fill="gray" height="16" viewBox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>') no-repeat right 10px center;
  background-size: 16px;
  box-sizing: border-box;
  cursor: pointer;
}
.barraOrdenar select:focus {
  outline: none;
  border-color: #23B89A;
}

/* Resultados - filtros aplicados */
.resultados {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 40px;
  padding: 0 10px;
  background-color: #F3F2F2;
  font-size: 14px;
  color: gray;
  border-radius: 4px;
  box-sizing: border-box;
  margin-bottom: 10px;
}
.resultados strong {
  color: black;
}

/* Responsive */
@media (max-width: 1024px) {
  .main-container {
    grid-template-columns: 1fr 2fr;
    padding: 15px;
  }
  .inputs-precio {
    justify-content: space-between;
  }
  .inputPrecio {
    max-width: 120px;
  }
  .products {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 768px) {
  .main-container {
    grid-template-columns: 1fr;
    padding: 15px;
  }
  .filters {
    flex-direction: row;
    overflow-x: auto;
    gap: 10px;
    padding-bottom: 10px;
  }
  .inputs-container {
    padding: 10px 5px;
    min-width: 150px;
    border-bottom: none;
    border-right: 2px solid #CCCBCB;
  }
  .products {
    grid-template-columns: 1fr;
  }
  .inputPrecio {
    max-width: 100%;
  }
  .inputBuscar {
    max-width: 100%;
  }
}

/* Mejor foco accesible */
input[type="radio"]:focus + label,
input[type="checkbox"]:focus + label {
  outline: 2px solid #23B89A;
  outline-offset: 2px;
}
</style>
