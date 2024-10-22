<script>
</script>

<template>
    <div class="fondo">
        <div class="fotoPerfil">
        <span class="material-symbols-outlined" id="fotoPerfil">
        account_circle
        </span>
        <div class="starsPrincipales">
        <span class="material-symbols-outlined" id="starsDebajoDeFoto">
        star
        </span>
        <span class="material-symbols-outlined" id="starsDebajoDeFoto">
        star
        </span>
        <span class="material-symbols-outlined" id="starsDebajoDeFoto">
        star
        </span>
        <span class="material-symbols-outlined" id="starsDebajoDeFoto">
        star
        </span>
        <span class="material-symbols-outlined" id="starsDebajoDeFoto5">
        star
        </span>
    </div>
    </div>
    <div id="namePerfil">
        <p id="nameUsuario">Juan Felipe
        <br> Ramos Rojas</p>
    </div>
    <div class="resumenActividadYUbicacion">
        <p><strong>3</strong> compras y <strong>5 </strong> ventas/donaciones</p>
    </div>
    </div>
</template>

<style>

.fondo {
    background-color: rgb(245, 245, 245);
    margin: 0px 200px;
    border: solid 1px rgb(197, 197, 197);
    padding-left: 10px;
    padding-top: 10px;
    display: flex;
    flex-direction: column;
    justify-items: center;
}

#fotoPerfil {
    font-size: 140px;
    background-color: #0F4F42;
    border-radius: 20px;
    border: solid 2px;
    color: white;
    padding: 10px;
}

#starsDebajoDeFoto, #starsDebajoDeFoto5 {
    display: flex;
    flex-direction: column;
    font-size: 34px;
    margin-top: 5px;
}

#starsDebajoDeFoto {
    color: green;
}

#starsDebajoDeFoto5 {
    color: rgb(143, 143, 143);
}

.starsPrincipales {
    display: flex;
}

#namePerfil {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-left: 10px;
}

#nameUsuario {
    font-size: 50px;
}

.resumenActividadYUbicacion {
    display: flex;
    flex-direction: column;
}

</style>