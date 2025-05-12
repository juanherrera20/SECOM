<script setup>
import ButtonDefault from '@/components/ButtonDefault.vue';
import { defineProps, defineEmits, ref } from 'vue';
import axios from 'axios';

//Ajustes para el modal
const props = defineProps({
    mostrar: Boolean
});

const emit = defineEmits(['cerrar']);

const cerrarModal = () => {
    emit('cerrar');
};


//Obtener y guardar ubicación
const address = ref({
    pais: "",
    ciudad: "",
});



const msgFalla = ref(false); //Para mostrar el mensaje de intentar obtener la ubicación otra vez si la obtenida es errónea

const loading = ref(false);
const errorMsg = ref("");

async function obtenerUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "este navegador no soporta geolocalización";
        return;
    }
    
    loading.value = true;
    errorMsg.value = "";
    
    navigator.geolocation.getCurrentPosition(async (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        try {

            const response = await axios.get(`https://nominatim.openstreetmap.org/reverse`, {
                params: { lat, lon, format: "json" }
            });
            
            const data = response.data;
            
            address.value.ciudad = data.address.city || data.address.town || data.address.village;
            address.value.pais = data.address.country;
            
            //console.log("Ubicación obtenida: ", address.value);
            console.log("latitud: ", lat, " longitud: ", lon);

            msgFalla.value = true;
            
            //await guardarUbicacion(address.value.pais, address.value.ciudad);
        } catch (error) {
            errorMsg.value = "Error al obtener la ubicación";
            console.log(errorMsg);
        } finally {
            loading.value = false;
        }
    }, (error) => {
        errorMsg.value = "Error de geolocalización: " + error.message;
        loading.value = false;
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 } //Con esto el navegador usa el GPS y no la dirección IP
);
}
/*
const guardarUbicacion = async () => {
  try {
    const token = localStorage.getItem('token');
    const response = await axios.post('http://127.0.0.1:8000/api/v1/ubicacion/', address.value, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert('Ubicación guardada correctamente');
    ubicacion.value = { pais: '', ciudad: '' };
  } catch (error) {
    errorMsg.value = "Error al guardar la ubicación.";
    console.error('Error al guardar la ubicación', error);
  }
};*/

const guardarUbicacion = async () => {
  try {
    const token = localStorage.getItem('token');
    
    if (!token) {
      console.error("No hay token disponible.");
      return;
    }

    const response = await axios.post(
      'http://127.0.0.1:8000/api/v1/ubicacion/',
      address.value,
      {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true,
      }
    );

    alert('Ubicación guardada correctamente');
    ubicacion.value = { pais: '', ciudad: '' };
  } catch (error) {
    errorMsg.value = "Error al guardar la ubicación.";
    console.error('Error al guardar la ubicación:', error.response?.data || error.message);
  }
};

</script>


<template>
    <Teleport to="body">
    <div class="divMayor" v-if="mostrar" @click="cerrarModal">
  <div class="container" @click.stop>
    <div class="iconYTitle">
        <span class="material-symbols-outlined">
            home_pin
        </span>
        <h2>Agregue su ubicación</h2>
    </div>
    <div class="Btn">
        <div class="containerBntDefault">
            <ButtonDefault @click="obtenerUbicacion" :disabled="loading" size="default" color="azul" icono="" class="agg" :text="loading ? 'Obteniendo ubicación...' : 'Obtener Ubicación'" />
        </div>
        <p v-if="address.pais"><strong>País:</strong> {{ address.pais }}</p>
        <p v-if="address.ciudad"><strong>Ciudad:</strong> {{ address.ciudad }}</p>
        <p class="txt" v-if="msgFalla">Si esta no es tu ubicación actual, intentalo más tarde, pero si lo es, guardala.</p>
        <ButtonDefault v-if="msgFalla" @click="guardarUbicacion" :disabled="loading" size="default" color="azul" icono="" class="agg save" :text="loading ? 'Ubicación guardada' : 'Guardar Ubicación'" />
        <p id="error" v-if="errorMsg">{{ errorMsg }}</p>
    </div>
  </div>
</div>
</Teleport>
</template>


<style scoped>

.divMayor {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.container {
    display: flex;
    flex-direction: column;
    width: 350px;
}

.iconYTitle {
    background-color: #0F4F42;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 25px 0px;
}

span {
    font-size: 90px;
}

h2 {
    font-size: 27px;
}

input {
    padding: 4px 0px;
    padding-right: 160px;
    margin-top: 5px;
}

.Btn {
    padding-top: 12px;
    background-color: rgb(245, 245, 245);
    border: solid 1px rgb(197, 197, 197);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.containerBntDefault {
    display: flex;
    justify-content: center;
    margin: 20px 0px;
}

.agg {
    border-radius: 2px;
    width: 220px;
}

.save {
    margin-bottom: 15px;
}

#error {
    color: red;
    margin-bottom: 10px;
}

.txt {
    margin: 15px 0px;
    text-align: center;
}

</style>