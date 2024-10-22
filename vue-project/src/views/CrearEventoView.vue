<script>
import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue'
import FooterComponent from '@/components/FooterComponent.vue';

export default {
  components: {
    BotonPaginaAnterior,
    FooterComponent
  }
};

</script>

<template>

<div class="botonYTitulo">

    <BotonPaginaAnterior />

    <h1>Crea tu evento</h1>
    </div>
    <div class="infoEvento">
    <div class="infoEventoEInputs">
    <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
    </div>
<div class="contenedorInputs">
    <div class="inputsInfo">
        <div class="campo">
        <p class="tituloDeInput"><strong>Nombre del evento</strong></p>
        <input class="inputInfoEvento" type="text" placeholder="Ejemplo: Ayuda para María">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
        <div class="campo">
        <p class="tituloDeInput"><strong>Descripción del evento</strong></p>
        <input class="inputInfoEvento" type="text" placeholder="Ejemplo: Hola, buenos días...">
        </div>
    </div>
    <div class="inputsInfo">
        <div class="campo">
        <p class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></p>
        <input class="inputInfoEvento" type="text" placeholder="Ejemplo: Incendio de vivienda">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
        <div class="campo">
        <p class="tituloDeInput"><strong>Ubicación del evento (País, Ciudad, Barrio)</strong></p>
        <input class="inputInfoEvento" type="text" placeholder="Ejemplo: Colombia, Cali...">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
    </div>
    <div class="inputsInfo">
        <div class="campo">
        <form action="">
            <p class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></p>
        <select name="categoriasAceptadas" id="categoriasAceptadas" >
            <option value="opciion1">Dinero</option>
            <option value="opciion2">Ropa y calzado</option>
            <option value="opciion3">Alimentos</option>
            <option value="opciion4">Artículos de higiene personal</option>
            <option value="opciion5">Agua y bebidas</option>
            <option value="opciion6">Todas</option>
        </select>
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </form>
        </div>
        <div class="campo">
        <p class="tituloDeInput"><strong>Fecha de lo ocurrido</strong></p>
        <input class="inputInfoEvento" type="text" placeholder="Día/Mes/Año">
        </div>
    </div>
    <div class="inputsInfo">
        <div class="campo">
        <p class="tituloDeInput"><strong>Contacto del organizador</strong></p>
        <input class="inputInfoEvento" type="text" placeholder="Número de teléfono o correo electrónico">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
    </div>
    <div class="inputsInfo">
        <div class="campo">
        <p class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></p>
        <div class="contenedorDeSubirFotos">
        <div class="subirFotos">
            <a href="#">
            <span id="iconoSubirFotos" class="material-symbols-outlined">
            photo_library
            </span>
            </a>
        </div>
        <div class="contenedorDeSubirFotos2">
        <div class="subirFotos2">
            <a href="#">
            <span id="iconoSubirFotos2" class="material-symbols-outlined">
            photo_library
            </span>
            </a>
        </div>
        <div class="subirFotos2">
            <a href="#">
            <span id="iconoSubirFotos2" class="material-symbols-outlined">
            photo_library
            </span>
            </a>
        </div>
        <div class="subirFotos2">
            <a href="#">
            <span id="iconoSubirFotos2" class="material-symbols-outlined">
            photo_library
            </span>
            </a>
        </div>
        <div class="subirFotos2">
            <a href="#">
            <span id="iconoSubirFotos2" class="material-symbols-outlined">
            photo_library
            </span>
            </a>
        </div>
        </div>
        </div>
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
    </div>
</div>
</div>
<div class="boton">
<button class="publicarProducto"><strong>Publicar</strong></button>
</div>
<FooterComponent />

</template>

<style scoped>

  .botonYTitulo {
    display: flex;
    justify-content: space-between;
    padding-bottom: 10px;
  }

   h1 {
    display: flex;
    font-size: 70px;
    margin: 0 auto;
    margin-top: 30px;
  }

  #subtitulo, .inputsInfo {
    margin: 0;
    padding: 0;
    display: block;
  }

  .infoEventoEInputs {
    display: flex;
    justify-content: center;
    font-size: 25px;
    background-color: #0F4F42;
    color: white;
    padding: 7px 0px;
  }

  .infoEvento {
    margin: 0px 150px;
    display: block;
  }

  .contenedorInputs {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-bottom: 0px;
    border-style: solid;
    border-color: #dadada;
    border-width: 1px;
    background-color: #FAFAFA;
  }

  .inputsInfo {
    display: flex;
    justify-content: space-between;
    padding: 0px 100px;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .spanYCampoRequer, .campoRequerido {
    font-size: 12px;
    margin-top: 2px;
  }

  .campoRequerido {
    color: #B81C2C;
  }

  #iconoSubirFotos {
    color: #898384;
    font-size: 60px;
  }

  #iconoSubirFotos:hover {
    color: #5a5a5a;
  }

  .subirFotos {
    border-style: solid;
    border-width: 1px;
    border-color: gray;
    display: flex;
    justify-content: center;
    padding: 30px 120px;
  }

  .subirFotos2 {
    border-style: solid;
    border-width: 1px;
    border-color: gray;
    justify-content: center;
    padding: 0px 10px;
  }
  #iconoSubirFotos2 {
    color: #898384;
    font-size: 50px;
  }

  #iconoSubirFotos2:hover {
    color: #5a5a5a;
  }

  .contenedorDeSubirFotos2 {
    display: flex;
    justify-content: space-between;
    margin: 0;
    padding-top: 5px;
  }

  .contenedorDeSubirFotos {
    display: block;
    justify-content: center;
  }

  .publicarProducto {
    background-color: #2B6682;
    width: 129px;
    height: 30px;
    border-radius: 5px;
    border: none;
    font-family: 'Aldrich', sans-serif;
  }

  .boton {
    display: flex;
    justify-content: center;
    margin: 20px 0px;
  }

  .publicarProducto:hover {
    background-color: #3c92b9;
  }

  .tituloDeInput {
    margin-bottom: 2px;
  }

  .inputInfoEvento {
    padding-right: 180px;
    padding-top: 3px;
    display: flex;
    justify-content: left;
  }

  .inputInfoEvento:hover {
    border: 2px solid black;
    outline: none;
  }

  #categoriasAceptadas {
    padding: 2px 0px;
    padding-right: 160px;
  }

  .campo {
    margin: 0px 20px;
  }

</style>