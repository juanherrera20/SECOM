<script setup>
import { ref } from 'vue';
import ButtonDefault from '@/components/ButtonDefault.vue';
import FooterComponent from '@/components/FooterComponent.vue';


// Datos del evento obtenidos desde la base de datos o API
const event = ref({
    nombre: 'Ayuda para José',
    fecha: '04/08/2024',
    organizador: 'jr938519E@gmail.com',
    causa: 'Inundación de vivienda',
    descripcion: '¡Ayudemos a Don José! Su casa se inundó debido a las fuertes lluvias recientes, y ha perdido muchos de sus muebles y pertenencias. Estamos organizando una colecta para apoyarlo con donaciones de ropa, alimentos, muebles y todo lo que pueda necesitar para reconstruir su vida. ¡Cualquier aporte será de gran ayuda! Juntos, podemos marcar la diferencia en su recuperación. Gracias por tu solidaridad.',
    ubicacion: {
        municipio: 'Becerril',
        departamento: 'Cesar',
        direccion: 'Barrio Manguitos, Calle 10 #5-22'
    },
    donacion: 'Ropa, Hogar y muebles, Dinero',
    images: [
        '../assets/Images/cuida-planeta.jpg',
        '../assets/Images/intercambios-locos.jpg',
        '../assets/Images/eventos.jpg'
    ]
});
</script>

<template>
<div>
    <div class="container">
        <div class="header">
            <img :src="event.images[0]" alt="Imagen del evento">
            <h2>{{ event.nombre }}</h2>
            <p class="info">Fecha de lo ocurrido: <strong>{{ event.fecha }}</strong></p>
            <p class="info">Ubicación: <strong>{{ event.ubicacion.municipio }}, {{ event.ubicacion.departamento }}</strong></p>
            <p class="info">Dirección: <strong>{{ event.ubicacion.direccion }}</strong></p>
            <p class="info">Organizador: <strong>{{ event.organizador }}</strong></p>
            <span class="badge">{{ event.causa }}</span>
        </div>
        
        <div class="gallery">
            <img v-for="(image, index) in event.images" :key="index" :src="image" :alt="'Imagen ' + (index + 1)">
        </div>
        
        <div class="description">
            <h3>Descripción del evento</h3>
            <p>{{ event.descripcion }}</p>
        </div>
        
        <div class="donations">
            <h3>Categoría de donaciones aceptadas</h3>
            <p class="typeDonac">{{ event.donacion }}</p>
        </div>
    </div>

    <div class="button-container">
        <ButtonDefault size="default" color="azul" text="Ayudar" class="publicarP" />
    </div>

    <FooterComponent />
</div>
</template>

<style scoped>
.container {
    background-color: rgb(245, 245, 245);
    border: solid 1px rgb(197, 197, 197);
    padding: 20px;
    max-width: 800px;
    margin: auto;
    margin-top: 10px;
}
.header {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.header img {
    width: 100%;
    max-width: 340px;
    border-radius: 10px;
}
.header h2 {
    color: #0F4F42;
    font-size: 24px;
    font-weight: bold;
}
.info {
    font-size: 14px;
    color: #555;
}
.badge {
    background: #0F4F42;
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    display: inline-block;
    margin-top: 10px;
}
.gallery {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 20px;
}
.gallery img {
    width: 100%;
    border-radius: 5px;
}
.description, .donations {
    margin-top: 20px;
}
.description h3, .donations h3 {
    font-size: 18px;
    font-weight: bold;
}
.description p, .donations p {
    color: #444;
}
.button-container {
    display: flex;
    justify-content: center;
    margin: 20px 0px;
}
</style>
