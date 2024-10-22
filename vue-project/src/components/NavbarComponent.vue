<script>

import MenuDespl from '../components/MenuDespl.vue'
import MenuProfile from '../components/MenuProfile.vue'

export default {
  components: {
    MenuDespl,
    MenuProfile
  }
};

</script>


<template>
  
<nav class="barraSuperior">
        <img class="logoSuperior" src="../assets/Images/Logo.png" alt="Logo SECOM">
        <ul class="opciSuperiores">
            <li class="lista_opci ubicacion1"><a href="#">Ubicación <span class="material-symbols-outlined">add_location_alt</span></a></li>
        </ul>
        <div class="barraBuscar">
            <input class="inputBuscar" type="text" placeholder="Buscar artículo">
            <span id="i" class="material-symbols-outlined">search</span>
        </div>
        <ul class="opciSuperiores">
            <div id="mensajYNotif">
            <li class="lista_opci mensaje1"><a href="#"><span class="material-symbols-outlined">forum</span></a></li>
            <li class="lista_opci notificacion1"><a href="#"><span class="material-symbols-outlined" id="iconNotif">notifications</span></a></li>
        </div>
        </ul>
        <li class="menu_despl">
                <a class="lista_opci" href="#"><span class="material-symbols-outlined" id="idPerfil">
                  account_circle </span></a>
                <MenuProfile />
            </li>
    </nav>
    <nav class="barraCategorias">
        <ul class="nav_menu">
            <li><a class="lista_opci" href="sostenibles">SOSTENIBLES</a></li>
            <li><a class="lista_opci" href="vender">VENDER</a></li>
            <li class="menu_despl">
                <a class="lista_opci" href="categorias">CATEGORÍAS <span class="material-symbols-outlined">arrow_drop_down</span></a>
                <MenuDespl />
            </li>
            <li><router-link to="/Gratuitos"><a class="lista_opci">GRATUITOS</a></router-link></li>
            <li><a class="lista_opci" href="eventos">EVENTOS</a></li>
            <li><a class="lista_opci" href="ofertas">OFERTAS <span class="material-symbols-outlined">sell</span></a></li>
        </ul>
    </nav>
    

</template>


<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: whitesmoke;
    font-family: 'Aldrich', sans-serif;
}

  /*Estilos y estetica para la barra de navegación*/
  .barraSuperior {
    background-color: #0F4F42;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 50px;
    padding-left: 20px;
    padding-right: 20px;
  }
  
  .logoSuperior {
    height: 55px;
    width: auto;
  }
  
  .ubicacion1 {
    display: flex;
    padding: 0px 70px;
    justify-content: center;
  }
  
  .barraBuscar {
    position: relative;
    flex-grow: 1;
    max-width: 400px;
  }
  
  .inputBuscar {
    background-color: rgb(236, 236, 236);
    width: 100%;
    height: 35px;
    padding: 12px 35px 12px 20px;
    border-radius: 18px;
    border: none;
    font-size: 14px;
  }
  
  #i {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    font-size: 22px;
    color: rgb(75, 75, 75);
  }
  
  .opciSuperiores {
    list-style: none;
    display: flex;
    justify-content: space-between;
    width: 300px;
  }
  
  .opciSuperiores li {
    margin: 0;
  }
  
  .opciSuperiores a {
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
  }
  
  #mensajYNotif, .mensaje1, .notificacion1 {
    display: flex;
    justify-content: space-between;
    padding: 0px 40px;
  }
  
  #idPerfil {
    color: white;
    font-size: 40px;
    margin-right: 50px;
  }
  
  #idPerfil:hover, .opciSuperiores a:hover {
    color: green;
  }
  
  .material-symbols-outlined {
    font-size: 22px;
  }
  
  .nav_menu {
    list-style: none;
    display: flex;
    justify-content: space-around;
    width: 100%;
    color: white;
  }
  
  .nav_menu a {
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
  }
  
  .barraCategorias {
    background-color: #a59a57;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
  }
  
  .lista_opci {
    margin: 0 20px;
  }
  
  .lista_opci:hover, .lista_categ:hover {
    color: green;
  }
  
  .menu_despl:hover .menu_categ {
    display: block;
  }


  .desplegar:hover .menuProfile {
    display: block;
  }

  .menu_despl {
    list-style-type: none;
  }

  #mensajYNotif {
    margin-left: 15px;
  }

  #iconNotif {
    margin-left: 35px;
  }

</style>
