<script setup>
import { ref } from 'vue'
import ButtonDefault from '../components/ButtonDefault.vue';
import ProductTarget from '@/components/ProductTarget.vue';
import FooterComponent from '@/components/FooterComponent.vue';

// Ejemplo de como mandar filtros
// const filtros = {
//   category: 3,
//   tags: 7,
//   price_min: 10000,
//   price_max: 80000,
//   condition: '1',
//   free: true,
//   offers: true,
//   ordering: '-price',
//   search: 'chanel',
// };

// const productos = await ProductsService.getProductos(filtros);


let products = ref ([
    // {id:100, img:"src/assets/Images/pantalon.webp", descuento: false, precio: 30000, descrip: 'PANTALON STYLE TALLA 8', tags: 'Pantalones'},
    {id:1, img:"src/assets/Tecnologia/ImageC.png", descuento: false, precio: 450000, descrip: 'TOZO T6 True Wireless Earbuds Bluetooth Headphon...', tags: 'Celulares'},
    {id:2, img:"src/assets/Images/applePC.webp", descuento: true, precio: 250000, descrip: 'iMac Retina 4k , Pantalla 21.5 Año 2019 Excelente Estado', tags: 'Computadora'},
    {id:3, img:"src/assets/Tecnologia/Image.png", descuento: false, precio: 50000, descrip: 'Portable Wshing Machine, 11lbs capacity Model 18NMF...', tags: 'Celulares'},
    {id:4, img:"src/assets/Tecnologia/Image-1.png", descuento: false, precio: 200500, descrip: 'Para Repuestos Tv Kalley 43 Smart Para Repuestos', tags: 'TVs'},
    {id:5, img:"src/assets/Tecnologia/Image-2.png", descuento: false, precio: 50000, descrip: '4K UHD LED Smart TV with Chromecast Built-in', tags: 'Celulares'},
    {id:6, img:"src/assets/Tecnologia/Image-3.png", descuento: true, precio: 72000, descrip: 'Ratón inalámbrico M170 - Compacto y portátil | Logitech', tags: 'Mouse'},
    {id:7, img:"src/assets/Tecnologia/Image-4.png", descuento: false, precio: 100000, descrip: 'Colección juegos Arcade en buen estado', tags: 'Juegos'},
    {id:8, img:"src/assets/Tecnologia/Image-5.png", descuento: false, precio: 123000, descrip: 'Celular Motorola Moto G Pure 32gb 3gb Ram Unlock Deep Indigo | MercadoLibre', tags: 'Celulares'},
    {id:9, img:"src/assets/Tecnologia/Image-6.png", descuento: false, precio: 26000, descrip: 'Teclado Flexible Portatil Siliconado', tags: 'Accesorios'},
    {id:10, img:"src/assets/Tecnologia/Image-7.png", descuento: false, precio: 35600, descrip: 'JBL Tune 520BT | Auriculares inalámbricos supraaurales', tags: 'Auriculares'},
    {id:11, img:"src/assets/Tecnologia/Image-8.png", descuento: false, precio: 56000, descrip: 'Delux K9600, Teclado Gamer Rgb Programable Macros Multimedia', tags: 'Accesorios'},
    {id:12, img:"src/assets/Tecnologia/Image-9.png", descuento: false, precio: 250000, descrip: 'Tv Samsung Series 4 Un32j4000efxza Led Hd 32 110v - 120v', tags: 'TVs'},
    {id:13, img:"src/assets/Tecnologia/Image-10.png", descuento: false, precio: 56000, descrip: 'Camara Web Webcam Cam 1080p Full Hd Microfono X Mayor Color Gris oscuro', tags: 'Accesorios'},
    {id:14, img:"src/assets/Tecnologia/Image-11.png", descuento: false, precio: 263000, descrip: 'Lenovo V510 Intel i5 6200u RAM 8GB SSD 256GB Layar Full HD', tags: 'Portatiles'},
    {id:15, img:"src/assets/Tecnologia/Image-12.png", descuento: false, precio: 152000, descrip: 'Celular Motorola G04 128gb 4gb Verde', tags: 'Celulares'},
    {id:16, img:"src/assets/Tecnologia/Image-13.png", descuento: false, precio: 32300, descrip: 'Smart Watch T900 Promax L, Serie 8 2.0 Big Color De La Caja Negro', tags: 'Relojes'},
    {id:17, img:"src/assets/Tecnologia/Image-14.png", descuento: true, precio: 618000, descrip: 'Cpu Torre Intel Core I5 2 Generacion 6gb Ram Pc Corporativo', tags: 'Computadores'},
    {id:18, img:"src/assets/Tecnologia/Image-15.png", descuento: false, precio: 74400, descrip: 'Reloj inteligente marca Samsumg UltraPlus 2k', tags: 'Relojes'},
    {id:19, img:"src/assets/Tecnologia/Image-16.png", descuento: false, precio: 730500, descrip: 'Amazon Basics High-Speed HDMI Cable (18 Gbps, 4K/6...', tags: 'TVs'},
    {id:20, img:"src/assets/Tecnologia/Image-17.png", descuento: false, precio: 176000, descrip: 'Impresora Fotográfica Inalámbrica EcoTank L8050', tags: 'Accesorios'},
    {id:21, img:"src/assets/Images/playstation.webp", descuento: false, precio: 690000, descrip: 'Sony Playstation 4 - 500gb +7 Juegos Digitales+precio:630000', tags: 'Juegos'},
    {id:22, img:"src/assets/Tecnologia/Image-18.png", descuento: false, precio: 200000, descrip: 'Samsung Electronics Samsung Galexy S21 5G', tags: 'Celulares'},
    {id:23, img:"src/assets/Tecnologia/Image-19.png", descuento: true, precio: 600000, descrip: 'iphone XS Dorado con Acabados redondeados pantalla 16pl', tags: 'Celulares'},
    {id:24, img: "src/assets/Images/televisor.webp", descuento: true, precio: 730000, descrip: 'Televisor Smart 75 Neo Qled 4k Qn85d', tags: 'TVs'}
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
            <div class="inputs-container">
                <h4>PRECIO</h4>
                <div class="elements">
                    <div class="inputs-precio">
                        <input class="inputPrecio" type="text" placeholder="Min. Precio">
                        <input class="inputPrecio" type="text" placeholder="Max. Precio">
                    </div>
                </div>
            </div>
            <div class="inputs-container">
                <h4>MARCAS POPULARES</h4>
                <div class="elements2">
                    <input type="checkbox"  id="marcas1"><label for="marcas1">Apple</label>
                    <input type="checkbox"  id="marcas2"><label for="marcas2">Dell</label>
                    <input type="checkbox"  id="marcas3"><label for="marcas3">Microsoft</label>
                    <input type="checkbox"  id="marcas4"><label for="marcas4">HP</label>
                    <input type="checkbox"  id="marcas5"><label for="marcas5">Samsung</label>
                    <input type="checkbox"  id="marcas6"><label for="marcas6">Google</label>
                    <input type="checkbox"  id="marcas7"><label for="marcas7">Intel</label>
                    <input type="checkbox"  id="marcas8"><label for="marcas8">Xiaomi</label>
                    <input type="checkbox"  id="marcas9"><label for="marcas9">Sony</label>
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
                    <div v-for="filtro in ['Apple', 'Todos los Precios', '5 Estrellas']" :key="filtro">
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

<FooterComponent></FooterComponent>
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