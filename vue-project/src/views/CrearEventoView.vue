<script setup>
import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue'
import ButtonDefault from '@/components/ButtonDefault.vue';
import FooterComponent from '@/components/FooterComponent.vue';
import AddImgsComponent from '@/components/AddImgsComponent.vue'

</script>

<template>
<div>
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
        <input class="inputInfoEvento" type="text" required placeholder="Ejemplo: Ayuda para María">
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
        <input class="inputInfoEvento" type="text" required placeholder="Ejemplo: Incendio de vivienda">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
        <div class="campo">
        <p class="tituloDeInput"><strong>Ubicación del evento (País, Ciudad, Barrio)</strong></p>
        <input class="inputInfoEvento" type="text" required placeholder="Ejemplo: Colombia, Cali...">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
    </div>
    <div class="inputsInfo">
        <div class="campo">
        <form action="">
            <p class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></p>
        <select name="categoriasAceptadas" id="categoriasAceptadas">
            <option value="opciion1">Todas</option>
            <option value="opciion2">Dinero</option>
            <option value="opciion3">Ropa y calzado</option>
            <option value="opciion4">Alimentos</option>
            <option value="opciion5">Artículos de higiene personal</option>
            <option value="opciion6">Agua y bebidas</option>
        </select>
        </form>
        </div>
        <div class="campo">
        <p class="tituloDeInput"><strong>Fecha de lo ocurrido</strong></p>
        <input class="inputInfoEvento" id="date" type="date">
        </div>
    </div>
    <div class="inputsInfo">
        <div class="campo">
        <p class="tituloDeInput"><strong>Contacto del organizador</strong></p>
        <input class="inputInfoEvento" type="email" required placeholder="Correo electrónico">
        <p class="spanYCampoRequer"><span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">circle</span><strong>Campo requerido</strong></p>
        </div>
    </div>
    <div class="inputsInfo">
      <div class="addIMGS">
        <div>
        <p class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></p>
      </div>
      <AddImgsComponent />
      </div>
    </div>
</div>
</div>
<div class="boton">
  <ButtonDefault size="default" color="azul" text="Publicar" icono="archive" class="Publicar" />
</div>
<FooterComponent />
</div>
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
    display: flex;
    flex-direction: column;
    margin: 0px 200px;
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

  #date{
    text-transform: uppercase;
    padding-right: 235px;
    padding-block: 1px;
  }

  .spanYCampoRequer, .campoRequerido {
    font-size: 12px;
    margin-top: 2px;
  }

  .campoRequerido {
    color: #B81C2C;
  }

  .boton {
    display: flex;
    justify-content: center;
    margin: 20px 0px;
  }

  .inputInfoEvento {
    padding-right: 180px;
    padding-top: 3px;
    padding-block: 3px;
    display: flex;
    justify-content: left;
  }

  .inputInfoEvento:hover {
    border: 2px solid black;
    outline: none;
  }

  #categoriasAceptadas:hover {
    border: 1.9px solid black;
    outline: none; 
  }

  #categoriasAceptadas {
    padding: 2px 0px;
    padding-right: 160px;
  }

  .campo {
    margin: 0px 20px;
  }

  .addIMGS {
    flex-direction: column;
  }

</style>