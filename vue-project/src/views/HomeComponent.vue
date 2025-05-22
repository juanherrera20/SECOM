<script setup>
import { ref, onMounted } from 'vue';
import ProductTarget from '@/components/ProductTarget.vue';
import FooterComponent from '@/components/FooterComponent.vue';
import { RouterLink } from 'vue-router';
import AlertComponent from '../components/AlertComponent.vue'


let products = ref ([
    {id:1, img: "src/assets/Images/televisor.webp", descuento: false, precio: 730000, descrip: 'Televisor Smart 75 Neo Qled 4k Qn85d', tags: 'TVs'},
    {id:2, img:"src/assets/Images/applePC.webp", descuento: true, precio: 250000, descrip: 'iMac Retina 4k , Pantalla 21.5 Año 2019 Excelente Estado', tags: 'Computadora'},
    {id:3, img:"src/assets/Images/playstation.webp", descuento: false, precio: 690000, descrip: 'Sony Playstation 4 - 500gb +7 Juegos Digitales+precio:630000', tags: 'Juegos'},
    {id:4, img:"src/assets/Images/pantalon.webp", descuento: false, precio: 30000, descrip: 'PANTALON STYLE TALLA 8', tags: 'Pantalones'}
])  

const showAlertLogin = ref(false)
const showAlertLogout = ref(false)

onMounted(() => {
  if (localStorage.getItem('loginSuccess') === 'true') {
    showAlertLogin.value = true
    localStorage.removeItem('loginSuccess')
    setTimeout(() => showAlertLogin.value = false, 3000)
  }
  else if (localStorage.getItem('loginSuccess') === 'false') {
    showAlertLogout.value = true
    localStorage.removeItem('loginSuccess')
    setTimeout(() => showAlertLogout.value = false, 3000)
  }
})

</script>


<template>
    <div id="contenedorMayor">
        <AlertComponent v-if="showAlertLogin" title="Inicio de sesión exitoso" message="¡Bienvenido/a a SECOM!" />
        <AlertComponent v-if="showAlertLogout" title="Sesión cerrada exitosamente" message="¡Adios!" />
<div class="pagina">
    <div class="eventos">
        <button class="boton eventos-right"><span class="material-symbols-outlined">arrow_left</span></button>
        <p>Participa en eventos de donación en tu zona y apoya a los que lo necesitan</p>
        <button class="boton eventos-left"><span class="material-symbols-outlined">arrow_right</span></button>
        
        <RouterLink to="/CrearEvento" class="destructive"><button class="destructive">Ver mas...</button></RouterLink>
        
    </div>
    <div class="tendencias">
        <h2>TENDENCIAS</h2>
        <div class="anuncio1"></div>
        <div class="anuncio2"></div>
        <div class="anuncio3"></div>
    </div>
    <div class="novedades">
        <h2>NOVEDADES</h2>
        <button class="boton novedades-left"><span class="material-symbols-outlined">arrow_left</span></button>

        <!--Así se insertan los valores para repetir el componente-->
        <ProductTarget v-for = "product in products" :key="product.id" :product="product"></ProductTarget>

        <button class="boton novedades-right"><span class="material-symbols-outlined">arrow_right</span></button>
    </div>
    <div class="vender">
        <router-link to="/VenderComponent">
            <button class="destructive" id="btnVender">Empezar a Vender..</button>
        </router-link>
    </div>
    <div class="unete">
        <router-link to="/Login" id="linkBotonRegister"><button class="destructive">Registrate</button></router-link>
    </div>
</div>
<div class="contenedorFooter">
    <FooterComponent />
</div>
</div>
</template>


<style scoped lang="scss">
.pagina {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 80% 1fr;
    grid-template-rows: repeat(5,400px);
    row-gap: 4rem;
}

.eventos {
    display: grid;
    grid-template-columns: 10% 80% 10%;
    grid-template-rows: 60% 40%;
    background-image: linear-gradient(to left, #15323F 37%, rgba(255, 126, 95, 0) 72%), url(@/assets/Images/eventos.jpg);
    background-size: 100% 500px;
    grid-column: 2 / 3;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.eventos p {
    width: 380px;
    color: whitesmoke;
    font-size: 28px;
    grid-area: 2 / 2 / 3 / 3;
    justify-self: end;
    margin: 0;
}

/*Botones para cambiar de información*/
.boton {
    background-color: transparent;
    border: 1px solid black;
    border-radius: 100%;
    width: 30px;
    height: 30px;
    justify-self: center;
}

.eventos-right{
    grid-area: 1 / 1 / 2/ 2;
    align-self: end;
}

.eventos-left{
    grid-area: 1 / 3 / 2/ 4;
    align-self: end;
}

.destructive{
    grid-area: 2 / 3 / 3 / 4;
    align-self: center;
    width: 99px;
    height: 25px;
    background-color: $primary_color100;
    font-family: 'Aldrich', sans-serif;
    color: whitesmoke;
    border-radius: 10px;
    padding: 0;
    border: 0;
}

#btnVender {
    margin-top: 200%;
}

.destructive:hover {
    background-color: #1C957C;
}

.boton:hover{
    background-color: rgba(255, 255, 255, 0.35);
}

/*Aquí empieza la parte de tendecias*/
.tendencias {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 10% 90%;
    gap: 10px;
    grid-column: 2 / 3;
}

.tendencias h2 {
    border-bottom: 2px solid gray;
    padding: 5px;
    grid-area: 1 / 1 / 2 / 4;
}

.anuncio1{
    background-image: url(@/assets/Images/ofertas.png);
    background-size: cover;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.anuncio2{
    background-image: url(../assets/Images/cuida-planeta.jpg);
    background-size: cover;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.anuncio3{
    background-image: url(../assets/Images/intercambios-locos.jpg);
    background-size: cover;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

/*Aquí empieza la parte de novedades*/
.novedades {
    display: grid;
    grid-template-columns: 4% repeat(4, 1fr) 4%;
    grid-template-rows: 10% 90%;
    gap: 10px;
    grid-column: 2 / 3;
}

.novedades h2 {
    border-bottom: 2px solid gray;
    padding: 5px;
    grid-area: 1 / 1 / 2 / 7;
}

.novedades-left {
    order: -1;
    align-self: center;
}

.novedades-right {
    order: 1;
    align-self: center;
}

/*Aquí empieza la parte de Vender*/
.vender {
    display: flex;
    justify-content: end;
    background-image: url(../assets/Images/Vender-nosotros.png);
    background-size: 100% 100%; /* Ajusta la imagen para que encaje completamente dentro del contenedor */
    background-repeat: no-repeat;
    padding: 30px;
    grid-column: 2 / 3;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.vender button{
    width: 150px;
    align-self: flex-end;
}

/*Aquí empieza la parte de Unete*/
.unete {
    background-image: url(../assets/Images/Unete-nosotros.png);
    display: flex;
    justify-content: end;
    background-size: 100% 100%; /* Ajusta la imagen para que encaje completamente dentro del contenedor */
    background-repeat: no-repeat;
    padding: 30px;
    grid-column: 2 / 3;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.unete button {
    align-self: flex-end;
}

#linkBotonRegister {
    display: flex;
}

</style>