<script setup>
    import FooterComponent from '@/components/FooterComponent.vue';
</script>

<template>
<div class="imgDeFondo">
    <div class="logoYTitulo">
        <div class="contenedorLogo">
    <img src="../assets/Images/logo secom.png" alt="Logo secom" class="logoSECOM">
        </div>
    <h1>Términos y condiciones de SECOM</h1>
    </div>
</div>
<div class="parrafos">
    <p>Bienvenido a SECOM. Al acceder y utilizar nuestra plataforma, aceptas cumplir con los siguientes Términos y Condiciones. Te recomendamos leerlos atentamente antes de utilizar nuestros servicios.</p>
    <br>
    <p><strong>Uso de la plataforma</strong></p>
    <p>SECOM proporciona una plataforma en línea para el intercambio de artículos sostenibles y de segunda mano entre usuarios de la comunidad. Al utilizar SECOM, te comprometes a:</p>
    <br>
    <p>Usar la plataforma de manera responsable y conforme a la ley.
    No publicar contenido ofensivo, ilegal o que viole los derechos de otros.
    Respetar las reglas de intercambio y comportamiento establecidas por SECOM.</p>
    <p><strong>Registro de cuenta y seguridad</strong></p>
    <p>Para utilizar ciertos servicios de SECOM, es necesario registrarse y crear una cuenta. Como usuario, eres responsable de la seguridad de tus credenciales y de cualquier actividad que ocurra bajo tu cuenta.</p>
    <br>
        <li>Debes proporcionar información precisa y mantenerla actualizada.</li>
        <li>No compartas tu contraseña con terceros.</li>
        <li>Notifícanos de inmediato si detectas un uso no autorizado de tu cuenta.</li>
        <br>
        <p><strong>Publicación y gestión de articulos</strong></p>
        <p>Al publicar artículos en SECOM, aceptas que:</p>
        <li>Los artículos deben estar en buen estado y ser útiles para otros.</li>
        <li>La información proporcionada sobre los artículos debe ser precisa y no engañosa.</li>
        <li>SECOM se reserva el derecho de eliminar cualquier publicación que no cumpla con nuestras políticas.</li>
        <br>
        <p><strong>Colaboración con Organizaciones y Eventos Locales</strong></p>
        <p>Nuestra plataforma permite a los usuarios colaborar con organizaciones benéficas locales y participar en eventos comunitarios. Al hacerlo, aceptas seguir las normativas de cada evento y organización.</p>
        <br>
        <p><strong>Limitación de Responsabilidad</strong></p>
        <p>SECOM no se hace responsable por:</p>
        <br>
        <li>Pérdida de artículos durante el proceso de intercambio.</li>
        <li>Daños derivados del uso de la plataforma.</li>
        <li>La calidad o estado de los artículos intercambiados.</li>
        <li>El uso de la plataforma es bajo tu propio riesgo.</li>
        <br>
        <p><strong>Modificaciones a los Términos y Condiciones</strong></p>
        <p>Nos reservamos el derecho a modificar estos términos en cualquier momento. Te notificaremos sobre cualquier cambio significativo a través de la plataforma o por correo electrónico. Es tu responsabilidad revisar periódicamente los Términos y Condiciones actualizados.</p>
        <br>
        <p><strong>Ley Aplicable y Jurisdicción</strong></p>
        <p>Estos Términos y Condiciones se rigen por las leyes de Colombia y cualquier disputa relacionada con ellos será resuelta en los tribunales de [Ciudad o Región].</p>
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