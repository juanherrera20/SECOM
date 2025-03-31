<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";
import { register } from "../services/Authentication";

const router = useRouter();
const data = ref({
    email: "",
    password: "",
    first_name: "",
    last_name: "",
    telefono: ""
});

const mensajeExito = ref("");
const mensajeError = ref("");


const loginWithGoogle = async () => {
    try {
        const response = await fetch("http://localhost:8000/auth/google/");
        const data = await response.json();

        localStorage.setItem("oauth_state", data.state); // Guardamos el state

        window.location.href = data.auth_url; // Redirigir a Google con el state correcto
    } catch (error) {
        console.error("Error al obtener la URL de autenticación:", error);
    }
};

const handleSubmit = async () => {
    try {
        console.log("Intentando registrar usuario");
        const response = await register(data.value);
        mensajeExito.value = "Usuario registrado exitosamente";
        router.push("/login");
    } catch (error) {
        console.error(error);
        mensajeError.value = "Error al registrar usuario. Verifica tus credenciales.";
    }
}
</script>


<template>
<div class="pagina">
    <div class="container left">
        <img class="logo"  src="../assets/Images/logo secom.png"  alt="Logo Alternativo Secom Png">
        <p>Aquí, tus objetos usados encuentran un nuevo propósito. 
        Compra, vende y dona sin complicaciones en un espacio diseñado para conectar a personas que 
        buscan darle una segunda vida a sus cosas. ¡Únete a nuestra comunidad y haz la diferencia hoy!
        </p>
    </div>

    <div class="container right">
        <form @submit.prevent="handleSubmit" class="container">
        <h1>REGISTRATE</h1>
        <input v-model="data.first_name" type="text" placeholder="Nombres" class="campos">
        <input v-model="data.last_name" type="text" placeholder="Apellidos" class="campos">
        <input v-model="data.email" type="email" placeholder="Correo Electronico" class="campos">
        <input v-model="data.telefono" type="text" placeholder="Telefono" class="campos">
        <input v-model="data.password" type="password"  placeholder="Contraseña" class="campos">
        <button class="registro">Continuar</button>

        <div>
            <p>Ó Registrate con:</p>
            <button class="google"  @click="loginWithGoogle" href=""><img class="google" src="../assets/Images/google.png">Google</button>
        </div>
    </form>
    </div>
</div>
</template>


<style scoped>

.pagina {
    margin: 20px 0px;
    width: 100%;
    height: 80%;
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
    align-items: center;
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