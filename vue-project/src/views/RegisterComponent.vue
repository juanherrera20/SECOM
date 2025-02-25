<script setup>
import axios from 'axios';
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const usuario = reactive({
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    password: ''
});

const mensajeExito = ref("");
const mensajeError = ref("");

async function crearUsuario() {
    mensajeExito.value = "";
    mensajeError.value = "";

    try {
        const response = await axios.post("http://127.0.0.1:8000/api/usuarios/", usuario);
        if (response.status === 201) {
            mensajeExito.value = "Usuario creado exitosamente.";
            console.log("Usuario creado con éxito.");

            Object.assign(usuario, {
                username: "",
                first_name: "",
                last_name: "",
                email: "",
                password: "",
            });

            router.push({ name: "home" });
            alert("Usuario creado exitosamente.")
        }
    } catch (error) {
        if (error.response) {
            mensajeError.value = error.response.data.detail || "Error al crear usuario.";
        } else {
            mensajeError.value = "No se pudo conectar al servidor.";
        }

        Object.assign(usuario, {
                username: "",
                first_name: "",
                last_name: "",
                email: "",
                password: "",
            });
        
        console.error("Error al crear usuario:", error);
        alert("Error al crear usuario.")
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
        <form @submit.prevent="crearUsuario" class="container">
        <h1>REGISTRATE</h1>
        <input v-model="usuario.username" type="text" required placeholder="Elije un nombre único" class="campos">
        <input v-model="usuario.first_name" type="text" placeholder="Nombres" class="campos">
        <input v-model="usuario.last_name" type="text" placeholder="Apellidos" class="campos">
        <input v-model="usuario.email" type="email" placeholder="Email" class="campos">
        <input v-model="usuario.password" type="password" required placeholder="Contraseña" class="campos">
        <button class="registro">Continuar</button>

        <div>
            <p>Ó Registrate con:</p>
            <button class="google"><img class="google" src="../assets/Images/google.png">Google</button>
        </div>
    </form>
    </div>
</div>
</template>


<style scoped>

.pagina {
    margin: 50px 0px;
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