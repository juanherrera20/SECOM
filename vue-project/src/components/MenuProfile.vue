<script>
</script>

<template>
  <ul class="menu_categ">
    <li class="li"><a href="#" class="link">Seguimiento <span class="material-symbols-outlined">
        sticky_note_2
        </span></a></li>
        <li class="li"><router-link to="/EditPerfil" class="link">Configuración <span class="material-symbols-outlined">
        manufacturing
        </span></router-link></li>
        <li class="li"><a href="#" class="link">Perfil <span class="material-symbols-outlined">
        account_circle
        </span></a></li>
        <li class="li"><a href="#" class="link">Salir <span class="material-symbols-outlined">
        logout
        </span></a></li>
                </ul>


  <!--
    <div class="menuProfile">
      <ul class="opciones">
        <li class="li"><a href="#" class="link">Seguimiento <span class="material-symbols-outlined">
        sticky_note_2
        </span></a></li>
        <li class="li"><a href="#" class="link">Configuración <span class="material-symbols-outlined">
        manufacturing
        </span></a></li>
        <li class="li"><a href="#" class="link">Perfil <span class="material-symbols-outlined">
        account_circle
        </span></a></li>
        <li class="li"><a href="#" class="link">Salir <span class="material-symbols-outlined">
        logout
        </span></a></li>
      </ul>
    </div>
    -->
</template>




<style scoped>



.menu_categ {
    list-style: none;
    display: none;
    position: absolute;
    background-color: #15323f;
    padding: 0px 10px;
  }
  
  .menu_categ li {
    padding: 2px 0;
  }

  .menu_categ a {
    color: white;
    text-decoration: none;
  }

  .li {
    list-style: none;
    margin: 15px 0px;
  }

  .li:hover a {
    color: green;
  }
  

/*
.menuProfile {
    background: #15323f;
    padding: 10px 20px;
    margin: 20px 660px;
    margin-top: 120px;
    border-radius: 20px 0px 20px 20px;
    display: none;
}

.li {
    list-style: none;
    margin: 15px 0px;
    display: flex;
    justify-content: center;
}

.link {
    color: white;
    text-decoration: none;
    display: flex;
    justify-content: center;
}

.link:hover {
    color: green;
  }

  .material-symbols-outlined {
    margin-left: 5px;
  }
*/
</style>