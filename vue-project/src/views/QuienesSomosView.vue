<script setup> 
import FooterComponent from '@/components/FooterComponent.vue';
import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';

</script>

<template>
    <div>
        <BotonPaginaAnterior />
    
<div class="imgDeFondo">
    <div class="logoYTitulo">
        <div class="contenedorLogo">
    <img src="../assets/Images/logo secom.png" alt="Logo secom" class="logoSECOM">
        </div>
    <h1>¿Quiénes somos?</h1>
    </div>
</div>
<div class="parrafos">
    <p>SECOM es una plataforma web creada para facilitar la compra, venta y donación de artículos usados. Nuestra misión es conectar a personas que desean dar una segunda vida a sus objetos, promoviendo la sostenibilidad, el reciclaje y el apoyo a causas comunitarias a través de donaciones.</p>
    <br>
    <p>En SECOM, creemos en el poder de la reutilización para reducir el impacto ambiental y en la importancia de ayudar a quienes lo necesitan. A través de nuestra plataforma, no solo puedes intercambiar productos de manera simple y segura, sino también contribuir a eventos de caridad organizados por miembros de la comunidad.</p>
    <br>
    <p><strong>¿Qué ofrecemos?</strong></p>
        <li>Un espacio seguro y confiable para vender y comprar productos usados.</li>
        <li>La posibilidad de donar artículos a personas u organizaciones que los necesiten.</li>
        <li>Oportunidades para organizar y participar en eventos de caridad, en los que las donaciones pueden hacer una diferencia en la vida de otros.</li>
        <br>
        <p><strong>Nuestra visión</strong></p>
        <p>Nuestro objetivo es construir una comunidad inclusiva y consciente que valore la reutilización y el apoyo mutuo. Aspiramos a convertirnos en una herramienta esencial para aquellas personas que desean hacer un impacto positivo tanto en el medio ambiente como en la sociedad.</p>
        <br>
        <p><strong>Desarrolladores</strong></p>
        <p>SECOM ha sido creada por Juan Felipe Ramos y Juan Andrés Herrera, estudiantes de tecnología en análisis y desarrollo de software. Nuestra motivación principal es utilizar nuestras habilidades para crear una plataforma que no solo facilite el intercambio de productos usados, sino que también fomente el sentido de comunidad y la ayuda mutua.</p>
</div>

<FooterComponent />
</div>
</template>

<style scoped>

.imgDeFondo {
    background-image: url('../assets/Images/Reciclaje-031.png');
    background-size: cover;
    background-position: center;
    height: 310px;
    display: flex;
    justify-content: center;
}

.logoSECOM {
    height: 200px;
    width: 200px;
    display: flex;
    justify-content: center;
}

.logoYTitulo {
    display: flex;
    flex-direction: column;
    margin-top: 40px;
    margin-bottom: 50px;
}

h1 {
    font-size: 50px;
}

.contenedorLogo {
    display: flex;
    justify-content: center;
}

.parrafos {
    display: flex;
    flex-direction: column;
    margin: 40px 130px;
}

p, li {
    font-size: 20px;
}

</style>