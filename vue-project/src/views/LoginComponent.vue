<script setup>
  import { RouterLink, useRouter} from 'vue-router';
  import { ref } from 'vue';
  import { login } from '../services/Authentication';

  //Definimos las variables que se van a utilizar en el formulario
  const email = ref('');
  const password = ref('');
  const router = useRouter();
  const errorMessage = ref('')

  const handleSubmit = async () => {
    try {
      console.log("Intentando iniciar sesión");

      const response = await login(email.value, password.value);
      alert('Inicio de sesión exitoso');
      router.push('/');

    } catch (error) {
      console.error(error);
      errorMessage.value = 'Error al iniciar sesión. Verifica tus credenciales.'
    }
  };

</script>


<template>

<form class="pagina" @submit.prevent="handleSubmit">
  <div class="container left">
    <img class="logo" src="../assets/Images/logo secom.png" alt="Logo Alternativo Secom Png">
    <p>Aquí, tus objetos usados encuentran un nuevo propósito. 
    Compra, vende y dona sin complicaciones en un espacio diseñado para conectar a personas que 
    buscan darle una segunda vida a sus cosas. ¡Únete a nuestra comunidad y haz la diferencia hoy!
    </p>
  </div>

  <div class="container right">
    <H1>INICIA SESIÓN</H1>
    <input class="campos" type="text" v-model="email"  placeholder="Usuario o correo electrónico">
    <input class="campos" type="password" v-model="password" placeholder="Contraseña">
    <button class="iniciarsesion">Continuar</button>
    <a class="linkRecuperarContra" href="recuperarContra">¿Has olvidado la contraseña?</a>
    <p>¿No tienes una cuenta? <RouterLink to="/Register">Registrarse</RouterLink></p>
    <p v-if="errorMessage" class="error" style="color: red">{{ errorMessage }}</p>
  </div>
</form>
  

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
  background-color: #0B3C32;
}

.container.right{
  color: white;
  background-color: #a59a57;
}

/*elementos*/

.iniciarsesion {
  background-color: #0F4F42;
  border: 0;
  padding: 0 ;
  font-family: 'Aldrich', sans-serif;
  color: white;
  width: 270px;
  height: 40px;
}

.iniciarsesion:hover {
  background-color: #145649;
  border: 1px solid white;
}

.linkRegister {
  text-decoration: none;
  color: #0F4F42;
}

.linkRegister:hover {
  color: #0D7643;
}

.linkRecuperarContra {
  text-decoration: none;
  color: white;
}

.campos {
  width: 310px;
  height: 35px;
  padding : 5px;
}

.campos:hover, .campos:focus{
  border: 2px solid #0F4F42;
  outline: none;
}

</style>