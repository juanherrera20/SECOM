<script setup>
import { ref } from 'vue'
import ButtonDefault from '../components/ButtonDefault.vue';
import ProductTarget from '@/components/ProductTarget.vue';

let products = ref ([
    {id:100, img:"src/assets/Images/pantalon.webp", descuento: false, precio: 0, descrip: 'PANTALON STYLE TALLA 8', tags: 'Pantalones'},
    {id:1, img:"src/assets/Imgs-para-categorias/Image.png", descuento: false, precio: 0, descrip: 'Vesido largo', tags: 'Vestidos'},
    {id:2, img:"src/assets/Imgs-para-categorias/Image2.png", descuento: false, precio: 0, descrip: 'Vestido corto', tags: 'Vestidos'},
    {id:3, img:"src/assets/Imgs-para-categorias/Image3.png", descuento: false, precio: 0, descrip: 'Jean cargo para mujer', tags: 'Pantalones'},
    {id:4, img:"src/assets/Imgs-para-categorias/Image4.png", descuento: false, precio: 0, descrip: 'Blusa crop top encaje moño coquette', tags: 'Blusas'},
    {id:5, img:"src/assets/Imgs-para-categorias/Image5.png", descuento: false, precio: 0, descrip: 'Camiseta koaj roja estampado centrico', tags: 'Camisetas'},
    {id:6, img:"src/assets/Imgs-para-categorias/Image6.png", descuento: false, precio: 0, descrip: 'Pijama de dama', tags: 'Pijamas'},
    {id:7, img:"src/assets/Imgs-para-categorias/Image7.png", descuento: false, precio: 0, descrip: 'Sudadera con bolsillos laterales', tags: 'Sudaderas'},
    {id:8, img:"src/assets/Imgs-para-categorias/Image8.png", descuento: false, precio: 0, descrip: 'Camiseta corta beige cuello largo', tags: 'Camisetas'},
    {id:9, img:"src/assets/Imgs-para-categorias/Image9.png", descuento: false, precio: 0, descrip: 'Disfraz de Cenicienta', tags: 'Disfraces'},
    {id:10, img:"src/assets/Imgs-para-categorias/Image10.png", descuento: false, precio: 0, descrip: 'Media pantalón diseño negro', tags: 'Lenceria'},
    {id:11, img:"src/assets/Imgs-para-categorias/Image11.png", descuento: false, precio: 0, descrip: 'Disfraz de Luigi', tags: 'Disfraces'},
    {id:12, img:"src/assets/Imgs-para-categorias/Image12.png", descuento: false, precio: 0, descrip: 'Blusita de bolerito', tags: 'Blusas'},
    {id:13, img:"src/assets/Imgs-para-categorias/Image13.png", descuento: false, precio: 0, descrip: 'Disfraz gladiadora romana', tags: 'Disfraces'},
    {id:14, img:"src/assets/Imgs-para-categorias/Image14.png", descuento: false, precio: 0, descrip: 'Chaqueta para dama en Pana, color rojo XL', tags: 'Chaquetas'},
    {id:15, img:"src/assets/Imgs-para-categorias/Image15.png", descuento: false, precio: 0, descrip: 'Crop top Zara Color gris claro', tags: 'Camisetas'},
    {id:16, img:"src/assets/Imgs-para-categorias/Image16.png", descuento: false, precio: 0, descrip: 'Vestido de baño dos partes casual', tags: 'V. baño'},
    {id:17, img:"src/assets/Imgs-para-categorias/Image18.png", descuento: false, precio: 0, descrip: 'Vestido de baño talla S agua bendita', tags: 'V. baño'},
    {id:18, img:"src/assets/Imgs-para-categorias/Image19.png", descuento: false, precio: 0, descrip: 'Blusa corta café claro', tags: 'Blusas'},
    {id:29, img:"src/assets/Imgs-para-categorias/Image20.png", descuento: false, precio: 0, descrip: 'Cosplay Disfraz Gojo Satoru peluca gafas', tags: 'Disfraces'},
])
</script>


<template>
<!-- <ButtonDefault size="sm" color="azul" text="Analizar" icono="favorite"></ButtonDefault> -->
<section class="main">
    <section class="compras">
    </section>

    <div class="navigation">
        <span class="material-symbols-outlined">home</span>
        <p>Inicio</p>
        <span class="material-symbols-outlined">chevron_left</span>
        <p>Categorías</p>
        <span class="material-symbols-outlined">chevron_left</span>
        <p>Ropa</p>
        <span class="material-symbols-outlined">chevron_left</span>
        <strong>Todos</strong>
    </div>

    <section class="main-container">
        <article class="filters">
            <div class="inputs-container">
                <h4>CATEGORÍAS</h4>
                <div class="elements">
                    <input type="radio" name="category" id="radio1"><label for="radio1">Todos</label>
                    <input type="radio" name="category" id="radio2"><label for="radio2">Vestidos</label>
                    <input type="radio" name="category" id="radio3"><label for="radio3">Pantalones</label>
                    <input type="radio" name="category" id="radio4"><label for="radio4">Camisetas</label>
                    <input type="radio" name="category" id="radio5"><label for="radio5">Suéteres</label>
                    <input type="radio" name="category" id="radio6"><label for="radio6">Blusas</label>
                    <input type="radio" name="category" id="radio7"><label for="radio7">Faldas</label>
                    <input type="radio" name="category" id="radio8"><label for="radio8">Sudaderas</label>
                    <input type="radio" name="category" id="radio9"><label for="radio9">Pijamas</label>
                    <input type="radio" name="category" id="radio10"><label for="radio10">Disfraces</label>
                    <input type="radio" name="category" id="radio11"><label for="radio11">Vestidos de baño</label>
                    <input type="radio" name="category" id="radio12"><label for="radio12">Chaquetas</label>
                    <input type="radio" name="category" id="radio13"><label for="radio13">Abrigos</label>
                    <input type="radio" name="category" id="radio14"><label for="radio14">Camisas</label>
                    <input type="radio" name="category" id="radio15"><label for="radio15">Lenceria</label>
                    <input type="radio" name="category" id="radio16"><label for="radio16">Otros</label>
                </div>
            </div>
            <div class="inputs-container">
                <h4>TALLAS</h4>
                <div class="elements2">
                    <input type="checkbox"  id="marcas1"><label for="marcas1">XXXS</label>
                    <input type="checkbox"  id="marcas2"><label for="marcas2">XXS</label>
                    <input type="checkbox"  id="marcas3"><label for="marcas3">XS</label>
                    <input type="checkbox"  id="marcas4"><label for="marcas4">S</label>
                    <input type="checkbox"  id="marcas5"><label for="marcas5">M</label>
                    <input type="checkbox"  id="marcas6"><label for="marcas6">L</label>
                    <input type="checkbox"  id="marcas7"><label for="marcas7">XL</label>
                    <input type="checkbox"  id="marcas8"><label for="marcas8">2XL</label>
                    <input type="checkbox"  id="marcas9"><label for="marcas9">Otro</label>
                </div>
            </div>
            <div class="inputs-container">
                <h4>ESTADO</h4>
                <div class="elements">
                    <input type="radio" name="estado" id="estado1"><label for="estado1">Todos</label>
                    <input type="radio" name="estado" id="estado2"><label for="estado2">Sin Usar</label>
                    <input type="radio" name="estado" id="estado3"><label for="estado3">Pocos Usos</label>
                    <input type="radio" name="estado" id="estado4"><label for="estado4">Muchos Usos</label>
                    <input type="radio" name="estado" id="estado5"><label for="estado5">Tercera Mano</label>
                    <input type="radio" name="estado" id="estado6"><label for="estado6">Otros</label>
                </div>
            </div>
        </article>

        <article class="products-container">
            <div class="barra">
                <div class="barraBuscar">
                    <input class="inputBuscar" type="text" placeholder="Buscar">
                    <span class="material-symbols-outlined icon">search</span>
                </div>
                <div class="ordenar">
                    <label for="ordenarPor">Ordenar Por:</label>
                    <div class="barraOrdenar">
                        <input id="ordenarPor" class="inputBuscar" type="text" placeholder="Por Precios">
                        <span class="material-symbols-outlined icon">stat_minus_1</span>
                    </div>
                </div>
            </div>
            <div class="resultados">
                <div class="sub-filters">
                    <p>Filtros: </p>
                    <div v-for="filtro in ['XS']" :key="filtro">
                        <strong>{{ filtro }}</strong>
                        <span class="material-symbols-outlined icon">close</span>
                    </div>
                </div>
                <div><strong>65,857</strong> <p>resultados</p></div>
            </div>

            <div class="products">
                <ProductTarget v-for="product in products" :key="product.id" :product="product" />
            </div>
            <ButtonDefault size="default" color="azul" text="Cargar mas" icono="autorenew" :style="{ width: '100%' }"></ButtonDefault>
           
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
input[type="radio"]:checked + label, input[type="checkbox"]:checked + label{
    color: #23B89A;
}
input[type="radio"]:checked + label:before {
    border: 4px solid #23B89A;
}


input[type="checkbox"] + label:before {
    content: "";
	width: 15px;
	height: 15px;
	float: left;
	margin: 0.5em 0.5em 0 0;
	border: 2px solid #CCCBCB;
	background: #FAFAFA;
}
input[type="checkbox"]:checked + label:before {
    border: 4px solid #23B89A;
    box-sizing: border-box;
}




/*Sectión de compras*/
.compras{
    background-image: url('@/assets/Images/CN_Producto-Gratis 1.png');
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
    padding: 20px 15px;
}

.inputs-precio {
    display: flex;
    gap: 20px;
}
.inputPrecio {
    background-color: white;
    width: 45%;
    height: 35px;
    padding: 10px 20px 10px 18px; /* Aumenta el padding a la derecha para dejar espacio para el icono */
    border-radius: 2px;
    border: 1px solid #CCCBCB;
    font-size: 10px;
}

.elements {
    display: flex;
    flex-direction: column;
    font-size: 14px;
    color: #433E3F;
    padding-bottom: 20px;
    padding-top: 10px;
    gap: 5px;
    border-bottom: 2px solid #CCCBCB;
}

.elements2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    font-size: 14px;
    color: #433E3F;
    padding-bottom: 20px;
    padding-top: 10px;
    gap: 5px;
    border-bottom: 2px solid #CCCBCB;
}

.products-container {
    display: flex;
    flex-direction: column;
    padding: 10px;
    gap:20px;
}

/* Barra de buscar */
.barraBuscar {
    position: relative; /* Necesario para que el icono se posicione respecto al contenedor */
    flex-grow: 1;
    max-width: 400px;
}

.inputBuscar {
    background-color: white;
    width: 100%;
    height: 35px;
    padding: 12px 40px 12px 20px; /* Aumenta el padding a la derecha para dejar espacio para el icono */
    border-radius: 2px;
    border: 1px solid #CCCBCB;
    font-size: 14px;
}

/* Ajuste del icono de búsqueda */
.barraBuscar .material-symbols-outlined {
    position: absolute;
    right: 10px; /* Ajusta la distancia del borde derecho */
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color: gray;
}

#i {
    position: absolute;
    right: 10px; /* Ajusta la distancia del borde derecho */
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color: gray;
}

.barra {
    display: flex;
    justify-content: space-between;
    align-items: center; /* Para alinear verticalmente todos los elementos */
    gap: 20px; /* Espacio entre los elementos de la barra */
}

.ordenar {
    display: flex;
    align-items: center;
    gap: 10px; /* Espacio entre el label y la barra de ordenar */
}

.barraOrdenar {
    position: relative;
    flex-grow: 1;
    max-width: 150px;
}

.barraOrdenar .material-symbols-outlined {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color: gray;
}

/* Filtros aplicados */
.resultados {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 40px;
    padding: 10px;
    background-color: #F3F2F2;
    font-size: 14px;
    color: gray;
} .resultados strong {
    color: black;
} .resultados div {
    display: flex;
    align-items: center;
}

.sub-filters {
    gap: 10px;
}


/*Targetas de productos*/
.products {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(6, 380px); /* Filas con altura fija de 330px */
    gap: 10px;
}

</style>