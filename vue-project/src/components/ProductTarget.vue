<script setup>
const props = defineProps(['product'])

const getPrecioFinal = () => {
  const offer = props.product.offer?.[0];
  return offer && offer.active ? offer.offer_price : props.product.price;
};

const tieneDescuento = () => {
  const offer = props.product.offer?.[0];
  return offer && offer.active;
};

const porcentajeDescuento = () => {
  const offer = props.product.offer?.[0];
  return offer && offer.active ? `${offer.discount_percentage}% OFF` : null;
};
</script>

<template>
  <div class="producto">
    <div
      class="imagen"
      :style="{ backgroundImage: 'url(' + product.image + ')' }"
    >
      <p v-if="tieneDescuento()">{{ porcentajeDescuento() }}</p>
    </div>

    <div class="precios">
      <span class="material-symbols-outlined">favorite</span>
      <span class="descuento" v-if="tieneDescuento()">${{ product.price }}</span>
      <span>${{ getPrecioFinal() }}</span>
    </div>

    <p class="descripcion">{{ product.name }}</p>

    <div class="etiquetas">
      <p v-for="(tag, i) in product.tags" :key="i">{{ tag }}</p>
    </div>

    <div class="stars">
      <span
        class="material-symbols-outlined"
        v-for="i in 5"
        :key="i"
        :style="{ color: i <= Math.round(product.rating) ? '#779553' : '#ccc' }"
      >
        star
      </span>
    </div>
  </div>
</template>

<style scoped>
.producto {
  display: grid;
  background-color: #f3f2f2;
  grid-template-rows: 55% 1fr 2fr 1fr 1fr;
  border-radius: 3px;
  box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);
}

.imagen {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 3px;
  height: 200px;
  position: relative;
}

.imagen p {
  background-color: yellow;
  padding: 2px 8px;
  position: absolute;
  top: 5px;
  left: 5px;
  border-radius: 4px;
  font-weight: bold;
}

.precios {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #0b3c32;
  padding: 5px;
  gap: 8px;
}

.descuento {
  color: gray;
  text-decoration: line-through;
}

.descripcion {
  padding: 5px;
  font-weight: 500;
}

.etiquetas {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  padding: 5px;
}

.etiquetas p {
  background-color: rgb(170, 53, 156);
  color: white;
  padding: 2px 6px;
  border-radius: 6px;
  font-size: 12px;
}

.stars {
  padding: 5px;
}

.stars span {
  font-size: 20px;
}
</style>
