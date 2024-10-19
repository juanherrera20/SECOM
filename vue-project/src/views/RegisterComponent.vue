<script setup>
import NavbarComponent from '../components/NavbarComponent.vue'
</script>


<template>
<NavbarComponent />

<div class="pagina">
    <div class="container left">
        <img class="logo"  alt="Logo Alternativo Secom Png">
        <p>Aquí, tus objetos usados encuentran un nuevo propósito. 
        Compra, vende y dona sin complicaciones en un espacio diseñado para conectar a personas que 
        buscan darle una segunda vida a sus cosas. ¡Únete a nuestra comunidad y haz la diferencia hoy!
        </p>
    </div>

    <div class="container right">
        <H1>REGISTRATE</H1>
        <input type="text" placeholder="Nombres" class="campos">
        <input type="text" placeholder="Apellidos" class="campos">
        <input type="email" placeholder="Email" class="campos">
        <input type="password" placeholder="Contraseña" class="campos">
        <button class="registro">Continuar</button>

        <div>
            <p>Ó Registrate con:</p>
            <button class="google"><img class="google" >Google</button>
        </div>

    </div>

</div>
</template>


<style scoped>


.pagina {
    width: 100%;
    height: 85%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background-color: white;
}

.logo {
    width: 250px;
    height: auto;
}

.container {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    width: 535px;
    height: 570px;
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2);
}

.container.left{
    text-align: center;
    padding: 20px;
    color: white;
    font-size: 22px;
    background-color: #a59a57;
}

.container.right{
    color: white;
    background-color: #0B3C32;
}

.container.right div {
    display: flex;
    flex-direction: row;
    gap: 10px;
}

/*elementos*/

.registro {
    background-color: #0F4F42;
    border: 0;
    padding: 0 ;
    font-family: 'Aldrich', sans-serif;
    color: white;
    width: 270px;
    height: 40px;
}

.registro:hover {
    background-color: #145649;
    border: 1px solid white;
}

.google {
    display: flex;
    align-items: center;
    background-color: transparent;
    border: 1px solid white;
    border-radius: 4px;
    width: 100px;
    color: white;
    font-family: 'Aldrich', sans-serif;
}

.google:hover {
    border: 1px solid green;
}

.google img {
    width: 40px;
    border:  none;
}

.campos {
    background-color: #f2f2f2;
    border: none;
    padding: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    width: 310px;
    height: 35px;
}

.campos:hover, .campos:focus{
    border: 2px solid #a59a57;
    outline: none;
    
}

</style>