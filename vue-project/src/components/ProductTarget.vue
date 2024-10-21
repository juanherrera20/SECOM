<script setup>
import { ref } from 'vue';

const props = defineProps(['product'])

</script>


<template>
<div class="producto">
    <div class="imagen" :style="{'background-image':'url(' + product.img + ')'}"><p v-show="product.descuento">Oferta 50%</p></div>
    <div class="precios">
        <span class="material-symbols-outlined">favorite</span>
        <span class="descuento" v-show="product.descuento">${{ product.precio }}</span>
        <!--Si hay descuento que lo aplique o no, dependiendo de eso muestra uno o el otro-->
        <span v-show="product.descuento">${{ product.precio * 0.5}}</span>
        <span v-show="!product.descuento">${{ product.precio }}</span>
    </div>
    <p class="descripcion">{{ product.descrip }}</p>
    <div class="etiquetas">
        <p>{{ product.tags }}</p>
    </div>
    <div class="stars">
        <span class="material-symbols-outlined">star</span>
        <span class="material-symbols-outlined">star</span>
        <span class="material-symbols-outlined">star</span>
        <span class="material-symbols-outlined">star</span>
        <span class="material-symbols-outlined">star</span>
    </div>
</div>
</template>


<style scoped>
.producto {
    display: grid;
    background-color: #F3F2F2;
    grid-template-rows: 55% 1fr 2fr 1fr 1fr;
    border-radius: 3px;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);
}

.imagen {
    background-size: cover; /* Hace que la imagen cubra todo el contenedor */
    background-position: center; /* Centra la imagen en el contenedor */
    background-repeat: no-repeat; /* Evita que la imagen se repita */
    border-radius: 3px;
}

.imagen p {
    background-color: yellow;
    display: inline-block; 
}

.precios {
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #0B3C32;
    padding: 5px;
}

.descripcion {
    padding: 5px;
}

.descuento {
    color: gray;
    text-decoration: line-through;
}

.etiquetas {
    display: flex;
    align-items: center;
    justify-content: start;
    padding: 5px;
}
.etiquetas p {
    background-color: rgb(170, 53, 156);
    display: inline-block; 
    border-radius: 6px;
}

.pc {
    background-color: #8E7C3C;
}

.stars {
    padding: 5px;
}

.stars span{
    color: #779553;
}
</style>