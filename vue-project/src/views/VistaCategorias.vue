<script setup>
import { ref } from 'vue'
import ButtonDefault from '../components/ButtonDefault.vue';
import ProductTarget from '@/components/ProductTarget.vue';

let products = ref ([
    {id:1, img: "src/assets/Images/televisor.webp", descuento: false, precio: 730000, descrip: 'Televisor Smart 75 Neo Qled 4k Qn85d', tags: 'TVs'},
    {id:2, img:"src/assets/Images/applePC.webp", descuento: true, precio: 250000, descrip: 'iMac Retina 4k , Pantalla 21.5 Año 2019 Excelente Estado', tags: 'Computadora'},
    {id:3, img:"src/assets/Images/playstation.webp", descuento: false, precio: 690000, descrip: 'Sony Playstation 4 - 500gb +7 Juegos Digitales+precio:630000', tags: 'Juegos'},
    {id:4, img:"src/assets/Images/pantalon.webp", descuento: false, precio: 30000, descrip: 'PANTALON STYLE TALLA 8', tags: 'Pantalones'}
])  
</script>


<template>
<!-- <ButtonDefault size="sm" color="azul" text="Analizar" icono="favorite"></ButtonDefault> -->
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
        <article class="filters">
            <div class="inputs-container">
                <h4>CATEGORÍAS</h4>
                <div class="elements">
                    <label><input type="radio" name="category">Todos</label>
                    <label><input type="radio" name="category">Computadores</label>
                    <label><input type="radio" name="category">Accesorios de Computador</label>
                    <label><input type="radio" name="category">Celulares</label>
                    <label><input type="radio" name="category">Auriculares</label>
                    <label><input type="radio" name="category">Juegos</label>
                    <label><input type="radio" name="category">TV y Pantallas</label>
                    <label><input type="radio" name="category">Relojes y Accesorios Electronicos</label>
                    <label><input type="radio" name="category">Otros</label>
                </div>
            </div>
        </article>

        <article class="products">
            <!--Así se insertan los valores para repetir el componente-->
            <ProductTarget v-for = "product in products" :key="product.id" :product="product"></ProductTarget>
        </article>
    </section>

</section>

</template>


<style scoped>
.main {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    padding: 20px;
}

/*Configuraciones generales de los inputs*/
input {
    accent-color: #23B89A;
}

/*Sectión de compras*/
.compras{
    background-image: url(@/assets/Images/compras.jpg);
    background-size: 1400px 325px;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
    width: 1400px;
    height: 325px;
}
.compras p{
    font-size: 144px;
    color: whitesmoke;
}

/*Section de el encabezado de ubicación*/
.navigation {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
    width: 1400px;
    background-color: #FAFAFA;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
    padding-left: 20px;
    padding-right: 20px;

    color: gray;
    font-size: 14px;
}
.navigation strong{
    color: #4197C0;
}

/*Section de productos y filtros, la seccion principal*/
.main-container{
    display: grid;
    background-color: #FAFAFA;
    grid-template-columns: 20% 80%;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
    width: 1400px;
    height: auto;
}

/*Section de filtros general*/
.filters {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.inputs-container{
    display: flex;
    flex-direction: column;
    width: 100%;
    padding: 30px 10px;
    gap: 10px

}

.elements {
    display: flex;
    font-size: 16px;
    flex-direction: column;
    color: #433E3F;
    gap: 5px
}




</style>