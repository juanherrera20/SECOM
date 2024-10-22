<script setup>
</script>

<template>
<div class="footer-container">
    <img src="../assets/Images/Logo.png" alt="SECOM Logo" class="footer-logo">
    <!-- Sección contacto -->
    <div class="footer-section">
        <p><strong>Contacto</strong><br>
            (606) 555-0129<br>
            (+57) 321 419 4663<br>
            Bogotá DC Calle 23 #57-22<br>
            (Cundinamarca/Colombia)<br>
            <a href="#">OficialSECOM@gmail.com</a></p>
    </div>
    <!-- Sección de enlaces SECOM -->
    <div class="footer-subsection">
        <h3>SECOM</h3>
        <ul>
            <li><router-link to="/QuienesSomosView"><a>¿Quiénes Somos?</a></router-link></li>
            <li><router-link to="/TerminosYCondiciones"><a>Términos y Condiciones</a></router-link></li>
            <li><router-link to="/AvisoDeActividadView"><a>Aviso de Privacidad</a></router-link></li>
        </ul>
    </div>
    <!-- Sección de soporte -->
    <div class="footer-subsection">
        <h3>SOPORTE</h3>
        <ul>
            <li><a href="#">Preguntas Frecuentes</a></li>
            <li><a href="#">¿Cómo vender?</a></li>
            <li><a href="#">¿Cómo comprar?</a></li>
        </ul>
    </div>
    <!-- Sección de redes sociales -->
    <div class="footer-logos">
        <h3>REDES SOCIALES</h3>
        <p>Síguenos</p>
        <div class="social-icons">
            <a href="#"><img class="iconos" src="../assets/Images/instagram.png" alt="Instagram"></a>
            <a href="#"><img class="iconos" src="../assets/Images/facebook.png" alt="facebook"></a>
            <a href="#"><img class="iconos" src="../assets/Images/youtube.png" alt="Youtube"></a>
            <a href="#"><img class="iconos" src="../assets/Images/logox.png" alt="X"></a>
        </div>
    </div>
</div>
<!-- Sección de copyright -->
<div class="footer-bottom">
    <p>SECOM © 2024. Design por NexoDigital</p>
</div>
</template>

<style scoped>
.footer-container {
    height: 270px;
    background-color: #15323F;
    display: grid;
    grid-template-columns: repeat(5 , 1fr);
    padding: 40px;
}

.footer-logo {
    width: 225px;
    height: auto;
    align-self: center;
}

.footer-section {
    font-size: 18px;
    color: #77878F;
    display: flex;
    align-items: center;
    justify-content: center;
    line-height: 2;
}

.footer-section  a{
    color: whitesmoke;
    text-decoration: none;
}

.footer-section strong {
    color: whitesmoke;
}

.footer-subsection {
    font-size: 14px;
    color: #77878F;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}

.footer-subsection a {
    color: #77878F;
    text-decoration: none;
}

.footer-subsection ul {
    height: 70%;
    display: flex;
    flex-direction: column;
    align-content: space-between;
    list-style-type: none;
    padding: 0;
    margin: 0;
    justify-content: space-around;
}

.footer-subsection  h3{
    color: whitesmoke;
}

.footer-logos {
    font-size: 14px;
    color: whitesmoke;
    display: grid;
    grid-template-rows: 20% 80%;
    grid-template-columns: 50% 50%;
    padding: 15px;
}

.iconos {
    width: 20px;
    height: auto;
}

.footer-logos h3 {
    grid-area: 1 / 1 / 1 /3;
    justify-self: center;
}

.footer-logos p {
    color: #77878F;
    justify-self: center;
}

.footer-bottom {
    display: flex;
    justify-content: center;
    height: 20px;
}

.footer-bottom p {
    text-align: center ;
    font-size: 14px;
    color: #77878F;
    background-color: #1C4356;
    width: 1000px;
}
</style>