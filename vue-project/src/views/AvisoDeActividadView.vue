<script setup>
    import FooterComponent from '@/components/FooterComponent.vue';
</script>

<template>
<div class="imgDeFondo">
    <div class="logoYTitulo">
        <div class="contenedorLogo">
    <img src="../assets/Images/logo secom.png" alt="Logo secom" class="logoSECOM">
        </div>
    <h1>Aviso de actividad</h1>
    </div>
</div>
<div class="parrafos">
    <p><strong>Privacidad y Protección de Datos</strong></p>
    <p>La recopilación y el uso de tus datos personales se rigen por nuestra Política de Privacidad (enlace a la política de privacidad). Nos comprometemos a proteger tu información y a no compartirla con terceros sin tu consentimiento, excepto en los casos permitidos por la ley.</p>
    <br>
        <p><strong>Propiedad Intelectual</strong></p>
        <p>Todo el contenido y software de SECOM, incluidos textos, gráficos, logotipos e imágenes, son propiedad de SECOM o de sus licenciantes y están protegidos por las leyes de propiedad intelectual. No se permite copiar, modificar o distribuir contenido sin nuestra autorización previa.</p>
</div>
<FooterComponent></FooterComponent>
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