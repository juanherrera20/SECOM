<script>
import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue'

export default {
  components: {
    BotonPaginaAnterior
  }
};

</script>

<template>

    <BotonPaginaAnterior />

    <div class="contenedorTitulo"><p class="nombreContenedor">INFORMACIÓN BÁSICA</p></div>
    <div class="fondo">
        <div class="containerInfoBasica">
<div class="container">
    <div class="fotoYLinkEditar">
    <div class="fotoPerfil">
        <span class="material-symbols-outlined" id="fotoPerfil">
        account_circle
        </span>
    </div>
    <div class="editarFoto">
        <a href="#">Editar foto</a> <span class="material-symbols-outlined" id="lapiz">
        edit
        </span>
    </div>
    </div>
    <div class="inputsInfo">
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Nombres/s</strong></p>
        <input type="text" placeholder="Escriba su nombre aquí">
        <div class="mensajeRequerido">
        <span class="material-symbols-outlined puntoRojo">
        radio_button_unchecked
        </span> <p class="requerido"><strong>Campo requerido</strong></p>
        </div>
        </div>
        <div class="inputInterior">
        <p><strong>Apellidos/s</strong></p>
        <input type="text" placeholder="Sus apellidos aquí">
        </div>
        </div>
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Correo electrónico</strong></p>
        <input type="text" placeholder="Su correo electrónico aquí">
        <div class="mensajeRequerido">
        <span class="material-symbols-outlined puntoRojo">
        radio_button_unchecked
        </span> <p class="requerido"><strong>Campo requerido</strong></p>
        </div>
        </div>
        <div class="inputInterior">
        <p><strong>Cédula</strong></p>
        <input type="text" placeholder="Su número de cédula aquí">
        <div class="mensajeRequerido">
        <span class="material-symbols-outlined puntoRojo">
        radio_button_unchecked
        </span> <p class="requerido"><strong>Campo requerido</strong></p>
        </div>
        </div>
        </div>
        <div class="Inputs" id="ultimoInput">
        <div>
        <p><strong>Teléfono</strong></p>
        <input type="text" placeholder="Su teléfono aquí">
        </div>
        </div>
    </div>
</div>
</div>
    </div>
    <div class="contenedorTitulo" id="separarContenedores"><p class="nombreContenedor">DIRECCIÓN DEL PRODUCTO</p></div>
    <div class="fondoUbicacion">
        <div class="mensajeDeAyuda">
        <span class="material-symbols-outlined" id="help">
        help
        </span> 
        <p>Dirección del perfil, de esta manera se filtrarán los productos en relación a tu ubicación, facilitando el comercio e intercambio. De igual manera tu ubicación es usada al momento de publicar productos.</p>
        </div>
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>País</strong></p>
        <input type="text" placeholder="País de ubicación">
        </div>
        <div class="inputInterior">
        <p><strong>Ciudad</strong></p>
        <input type="text" placeholder="Ciudad de ubicación">
        </div>
        </div>
        <div class="confirmarUbicacion">
            <button id="botonconfirmarUbicacion">Confirmar ubicación</button>
        </div>
    </div>
    <div class="contenedorTitulo" id="separarContenedores"><p class="nombreContenedor">INFORMACIÓN EXTRA</p></div>
    <div class="fondoInfoExtra">
        <div class="mensajeDeAyuda">
        <span class="material-symbols-outlined" id="help">
        help
        </span> 
        <p>Regístrate como una empresa para tener algunas funcionalidades especiales como publicar eventos. Llena tus datos y envía tu solicitud, nuestro equipo la revisará y te dará una respuesta.</p>
        </div>
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Nombre de la empresa</strong></p>
        <input type="text">
        </div>
        <div class="inputInterior">
        <p><strong>NIT</strong></p>
        <input type="text">
        </div>
        </div>
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Razón social</strong></p>
        <input type="text">
        </div>
        <div class="inputInterior">
        <p><strong>Correo electrónico</strong></p>
        <input type="text">
        </div>
        </div>
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Sobre ustedes</strong></p>
        <input type="text">
        </div>
        </div>
    </div>
    <div class="contenedorTitulo" id="separarContenedores"><p class="nombreContenedor">CAMBIAR CONTRASEÑA</p></div>
    <div class="fondoCambiarContra">
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Contraseña actual</strong></p>
        <input type="text">
        </div>
        <div class="inputInterior">
        <p><strong>Nueva contraseña</strong></p>
        <input type="text">
        </div>
        </div>
        <div class="Inputs">
        <div class="inputInterior">
        <p><strong>Confirmar contraseña</strong></p>
        <input type="text">
        </div>
        </div>
    </div>
</template>

<style scoped>

.container {
    display: inline-flex;
    justify-content: center;
}

.inputsInfo {
    display: inline-block;
}

#fotoPerfil {
    font-size: 140px;
    background-color: #0F4F42;
    border-radius: 20px;
    border: solid 2px;
    color: white;
    padding: 10px;
}

.editarFoto {
    display: flex;
}

a {
    text-decoration: none;
    margin-top: 5px;
    color: black;
}

a:hover, .editarFoto:hover {
    color: green;
}

.fotoYLinkEditar {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 32px 25px;
}

.puntoRojo {
    background-color: rgb(177, 0, 0);
    color: rgb(177, 0, 0);
    border-radius: 20px;
    font-size: 15px;
    margin-right: 3px;
}

.requerido {
    font-size: 13px;
}

.mensajeRequerido {
    display: flex;
    justify-items: left;
    margin-top: 3px;
}

/*-------------------*/

.Inputs {
    display: flex;
    justify-content: center;
    margin: 35px 0px;
}

#ultimoInput {
    display: flex;
    justify-content: center;
}

.inputInterior {
    margin: 0px 15px;
}

input {
    padding: 5px 80px;
    padding-left: 2px;
}

.contenedorTitulo {
    background-color: #0F4F42;
    padding: 10px 0px;
    display: flex;
    justify-content: center;
    margin: 0px 200px;
}

.nombreContenedor {
    color: white;
    font-size: 35px;
}

.fondo, .fondoUbicacion, .fondoInfoExtra, .fondoCambiarContra {
    background-color: rgb(245, 245, 245);
    margin: 0px 200px;
    padding: 10px 0px;
    border: solid 1px rgb(197, 197, 197);
}

.fondo {
    display: flex;
    justify-content: center;
}

#separarContenedores {
    margin-top: 40px;
}

.mensajeDeAyuda {
    display: flex;
    justify-content: left;
    margin-bottom: 40px;
}

#help {
    margin: 0px 8px;
    margin-top: 5px;
}

.confirmarUbicacion {
    display: flex;
    justify-content: center;
    margin: 35px 0px 15px 0px;
}

#botonconfirmarUbicacion {
    background-color: rgb(0, 197, 197);
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 8px;
    font-size: 15px;
}

#botonconfirmarUbicacion:hover {
    background-color: rgb(0, 146, 146);
}

</style>