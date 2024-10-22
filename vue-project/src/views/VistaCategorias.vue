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
                    <input type="radio" name="category" id="radio1"><label for="radio1">Todos</label>
                    <input type="radio" name="category" id="radio2"><label for="radio2">Computadores</label>
                    <input type="radio" name="category" id="radio3"><label for="radio3">Accesorios de Computador</label>
                    <input type="radio" name="category" id="radio4"><label for="radio4">Celulares</label>
                    <input type="radio" name="category" id="radio5"><label for="radio5">Auriculares</label>
                    <input type="radio" name="category" id="radio6"><label for="radio6">Juegos</label>
                    <input type="radio" name="category" id="radio7"><label for="radio7">TV y Pantallas</label>
                    <input type="radio" name="category" id="radio8"><label for="radio8">Relojes y Accesorios Electronicos</label>
                    <input type="radio" name="category" id="radio9"><label for="radio9">Otros</label>
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
input[type="radio"] + label,
input[type="checkbox"] + label {
	line-height: 2em;
    align-items: end;
}

input[type="radio"] , input[type="checkbox"] {
	display: none;
}

input[type="radio"] + label:before {
    content: "";
	width: 20px;
	height: 20px;
	float: left;
	margin: 0.5em 0.5em 0 0;
	border: 2px solid #CCCBCB;
	background: #FAFAFA;
    border-radius: 100%;
}
input[type="radio"]:checked + label{
    color: #23B89A;
}
input[type="radio"]:checked + label:before {
    border: 4px solid #23B89A;
}


input[type="checkbox"] + label:before {
    content: "";
	width: 20px;
	height: 20px;
	float: left;
	margin: 0.5em 0.5em 0 0;
	border: 2px solid #CCCBCB;
	background: #FAFAFA;
}
input[type="checkbox"]:checked + label:before {
    border-color: #0fbf12;
}
input[type="checkbox"]:checked + label:after {
    content: "";
    width: 12px;
    height: 6px;
    border: 4px solid #0fbf12;
    float: left;
    margin-left: -1.95em;
    border-right: 0;
    border-top: 0;
    margin-top: 1em;
    transform: rotate(-55deg);
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
    padding: 30px 15px;
}

.elements {
    display: flex;
    flex-direction: column;
    font-size: 14px;
    color: #433E3F;
    padding-bottom: 10px;
    padding-top: 10px;
    gap: 5px;
    border-bottom: 2px solid #CCCBCB;
}

.products {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(auto-fill, 400px); /* Filas con altura fija de 330px */
    gap: 10px;
    padding: 10px;
}

</style>