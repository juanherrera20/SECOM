<template>
    <div>
      <div class="botonYTitulo">
        <BotonPaginaAnterior />
        <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
      </div>
      <div class="infoEvento">
        <div class="infoEventoEInputs">
          <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
        </div>
        <div class="contenedorInputs">
          <div class="inputsInfo">
            <div class="campo">
              <p class="tituloDeInput"><strong>Nombre del evento</strong></p>
              <input
                class="inputInfoEvento"
                type="text"
                v-model="evento.nombre"
                required
                placeholder="Ejemplo: Ayuda para María"
              />
              <p class="spanYCampoRequer">
                <span
                  class="material-symbols-outlined campoRequerido"
                  style="font-variation-settings: 'FILL' 1;"
                  >circle</span
                ><strong>Campo requerido</strong>
              </p>
            </div>
            <div class="campo">
              <p class="tituloDeInput"><strong>Descripción del evento</strong></p>
              <textarea
                class="inputInfoEvento"
                v-model="evento.descripcion"
                placeholder="Ejemplo: Hola, buenos días..."
              ></textarea>
            </div>
          </div>
          <div class="inputsInfo">
            <div class="campo">
              <p class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></p>
              <input
                class="inputInfoEvento"
                type="text"
                v-model="evento.causa"
                required
                placeholder="Ejemplo: Incendio de vivienda"
              />
              <p class="spanYCampoRequer">
                <span
                  class="material-symbols-outlined campoRequerido"
                  style="font-variation-settings: 'FILL' 1;"
                  >circle</span
                ><strong>Campo requerido</strong>
              </p>
            </div>
            <div class="campo">
              <p class="tituloDeInput"><strong>Ubicación del evento</strong></p>
              <SelectMunicipios v-model="evento.ubicacion.municipio_id" />
              <input
                class="inputInfoEvento"
                type="text"
                v-model="evento.ubicacion.direccion"
                required
                placeholder="Dirección"
              />
              <input
                class="inputInfoEvento"
                type="text"
                v-model="evento.ubicacion.nombre"
                placeholder="Nombre de la ubicación (opcional)"
              />
              <input
                class="inputInfoEvento"
                type="text"
                v-model="evento.ubicacion.latitud"
                placeholder="Latitud (opcional)"
              />
              <input
                class="inputInfoEvento"
                type="text"
                v-model="evento.ubicacion.longitud"
                placeholder="Longitud (opcional)"
              />
            </div>
          </div>
          <div class="inputsInfo">
            <div class="campo">
              <p class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></p>
              <select v-model="evento.donacion_id" required>
                <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                  {{ donacion.nombre }}
                </option>
              </select>
            </div>
            <div class="campo">
              <p class="tituloDeInput"><strong>Fecha Evento</strong></p>
              <input class="inputInfoEvento" id="date" type="date" v-model="evento.fecha" />
            </div>
          </div>
          <div class="inputsInfo">
            <div class="addIMGS">
              <p class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></p>
              <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
            </div>
          </div>
        </div>
      </div>
      <div class="boton">
        <ButtonDefault
          size="default"
          color="azul"
          :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
          icono="archive"
          class="Publicar"
          @click="guardarEvento"
        />
      </div>
      <ButtonDefault v-if="modoEdicion" size="default"  color="rojo" text="Eliminar Evento" @click="eliminarEvento" />
      <FooterComponent />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { createEvento, updateEvento, getEventoById, getDonaciones, deleteEvento } from '../services/eventos';
  import { getCurrentUser } from '../services/users';
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';
  
  const route = useRoute();
  const router = useRouter();
  const eventoId = route.params.id;
  const modoEdicion = !!eventoId;
  
  const evento = ref({
    nombre: '',
    descripcion: '',
    causa: '',
    ubicacion: {
      municipio_id: null,
      nombre: '',
      direccion: '',
      latitud: '',
      longitud: '',
    },
    donacion_id: null,
    fecha: '',
    imagenes: [],
    pais: 'Colombia',
    ciudad: 'Cali',
  });
  
  const cargarImagenes = ref(null);
  const currentUser = ref(null);
  const donaciones = ref([]);
  
  onMounted(async () => {
    // Obtener usuario autenticado
    const userResponse = await getCurrentUser();
    currentUser.value = userResponse;
  
    // Obtener donaciones
    try {
      donaciones.value = await getDonaciones();
    } catch (error) {
      console.error('Error al cargar las donaciones:', error);
    }
  
    // Cargar datos del evento si estamos en modo edición
    if (modoEdicion) {
      try {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
  
        // Asignar valores a los desplegables
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      } catch (error) {
        console.error('Error al cargar el evento:', error);
      }
    }
  });
  
  const guardarEvento = async () => {
    try {
      // Validar campos requeridos
      if (
        !evento.value.nombre ||
        !evento.value.descripcion ||
        !evento.value.causa ||
        !evento.value.fecha ||
        !evento.value.ubicacion.municipio_id ||
        !evento.value.ubicacion.direccion ||
        !evento.value.donacion_id
      ) {
        alert('Todos los campos requeridos deben estar completos');
        return;
      }
  
      const eventoData = {
        ...evento.value,
        organizador: currentUser.value.id, // Usar el ID del usuario autenticado
        imagenes: cargarImagenes.value?.imagenes || [],
      };
  
      if (modoEdicion) {
        await updateEvento(eventoId, eventoData);
        alert('Evento actualizado correctamente');
      } else {
        await createEvento(eventoData);
        alert('Evento creado correctamente');
      }
      router.push({ name: 'EventosList' });
    } catch (error) {
      console.error('Error al guardar el evento:', error);
      alert('Hubo un error al guardar el evento');
    }
  };

  //Eliminar Evento
    const eliminarEvento = async () => {
        if (confirm('¿Seguro que deseas eliminar este evento?')) {
            try {
            await deleteEvento(eventoId);
            alert('Evento eliminado correctamente');
            router.push({ name: 'EventosList' });
            } catch (error) {
            console.error('Error al eliminar el evento:', error);
            alert('Hubo un error al eliminar el evento');
            }
        }
    };

  </script>


  <style scoped>
    
  .botonYTitulo {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin: 0;
  }
  
  .infoEvento {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .infoEventoEInputs {
    background-color: #0F4F42;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
  }
  
  .contenedorInputs {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .inputsInfo {
    display: flex;
    gap: 20px;
  }
  
  .campo {
    flex: 1;
  }
  
  .tituloDeInput {
    font-size: 1rem;
    color: #2c3e50;
    margin-bottom: 8px;
  }
  
  .inputInfoEvento {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
  }
  
  .inputInfoEvento:focus {
    border-color: #4CAF50;
    outline: none;
  }
  
  .spanYCampoRequer {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 0.9rem;
    color: #B81C2C;
    margin-top: 5px;
  }
  
  .campoRequerido {
    color: #B81C2C;
  }
  
  .boton {
    text-align: center;
    margin-top: 20px;
  }
  
  .Publicar {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .Publicar:hover {
    background-color: #45a049;
  }
  </style>