<template>
  <div>
    <!-- Encabezado con título y botón -->
    <header class="botonYTitulo">
      <BotonPaginaAnterior />
      <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
    </header>

    <!-- Sección de información del evento -->
    <section class="infoEvento">
      <div class="infoEventoEInputs">
        <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
      </div>

      <div class="contenedorInputs">
        <div class="inputsInfo">
          <!-- Nombre del Evento -->
          <div class="campo">
            <label for="eventoNombre" class="tituloDeInput"><strong>Nombre del evento</strong></label>
            <input
              id="eventoNombre"
              class="inputInfoEvento"
              type="text"
              v-model="evento.nombre"
              required
              placeholder="Ejemplo: Ayuda para María"
            />
            <p v-if="!evento.nombre" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Descripción del Evento -->
          <div class="campo">
            <label for="eventoDescripcion" class="tituloDeInput"><strong>Descripción del evento</strong></label>
            <textarea
              id="eventoDescripcion"
              class="inputInfoEvento"
              v-model="evento.descripcion"
              placeholder="Ejemplo: Hola, buenos días..."
            ></textarea>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Causa del Evento -->
          <div class="campo">
            <label for="eventoCausa" class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></label>
            <input
              id="eventoCausa"
              class="inputInfoEvento"
              type="text"
              v-model="evento.causa"
              required
              placeholder="Ejemplo: Incendio de vivienda"
            />
            <p v-if="!evento.causa" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Ubicación del Evento -->
          <div class="campo">
            <label for="eventoUbicacion" class="tituloDeInput"><strong>Ubicación del evento</strong></label>
            <SelectMunicipios v-model="evento.ubicacion.municipio_id" :municipios="municipios" />
            <label for="asignarUbicacion" class="tituloDeInput"><strong>O también asigna una ubicación en tiempo real</strong></label>
            <button
              id="asignarUbicacion"
              class="btn-asignar-ubicacion"
              type="button"
              @click="asignarUbicacion"
              :disabled="loading"
            >
              {{ loading ? 'Asignando ubicación...' : 'Asignar Ubicación' }}
            </button>

            <!-- Mensajes de error y éxito -->
            <p v-if="msgFalla" class="texto-emergencia">
              <strong>Hubo un error al asignar la ubicación.</strong>
            </p>
            <p v-if="msgExito" class="texto-emergencia">
              <strong>Se asignó correctamente la ubicación a este evento.</strong>
            </p>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Categoría de donaciones -->
          <div class="campo">
            <label for="eventoDonacion" class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></label>
            <select id="eventoDonacion" v-model="evento.donacion_id" required>
              <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                {{ donacion.nombre }}
              </option>
            </select>
          </div>

          <!-- Fecha del Evento -->
          <div class="campo">
            <label for="eventoFecha" class="tituloDeInput"><strong>Fecha Evento</strong></label>
            <input id="eventoFecha" class="inputInfoEvento" type="date" v-model="evento.fecha" />
          </div>
        </div>

        <!-- Imágenes -->
        <div class="inputsInfo">
          <div class="addIMGS">
            <label class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></label>
            <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
          </div>
        </div>
      </div>
    </section>

    <!-- Botón de acción para guardar -->
    <footer class="boton">
      <ButtonDefault
        size="default"
        color="azul"
        :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
        icono="archive"
        class="Publicar"
        @click="guardarEvento"
      />
    </footer>

    <!-- Botón de eliminar evento si estamos en modo edición -->
    <ButtonDefault
      v-if="modoEdicion"
      size="default"
      color="rojo"
      text="Eliminar Evento"
      @click="eliminarEvento"
    />

    <FooterComponent />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';

  // Import services to consume API
  import EventosService from '../services/eventos';
  import { getCurrentUser } from '../services/users';

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
  const municipios = ref([]);
  
  const msgFalla = ref(false); 
  const msgExito = ref(false); 
  const errorMsg = ref("");
  const loading = ref(false);

  onMounted(async () => {
    try {
      // Obtener usuario autenticado
      const userResponse = await getCurrentUser();
      currentUser.value = userResponse;

      // Obtener donaciones
      donaciones.value = await getDonaciones();

      // Obtener municipios
      const response = await api.get('/ubicacion/lista_city/');
      municipios.value = response.data;

      // Cargar datos del evento si estamos en modo edición
      if (modoEdicion) {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
        
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      }
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      alert("Hubo un error al cargar los datos.");
    }
  });

  // Asignar ubicación con geolocalización
  async function asignarUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "Este navegador no soporta geolocalización.";
        return;
    }

    loading.value = true;
    errorMsg.value = "";
    msgFalla.value = false;
    msgExito.value = false;

    try {
      navigator.geolocation.getCurrentPosition(async (position) => {
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        evento.value.ubicacion.latitud = latitud;
        evento.value.ubicacion.longitud = longitud;

        msgExito.value = true;
        console.log("Ubicación asignada correctamente:", latitud, longitud);
      }, (err) => {
        msgFalla.value = true;
        errorMsg.value = "Error al obtener la ubicación: " + err.message;
        console.log(errorMsg.value);
      });
    } catch (error) {
      msgFalla.value = true;
      errorMsg.value = "Error al obtener la ubicación";
      console.error(errorMsg.value);
    } finally {
      loading.value = false;
    }
  }
  
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
        organizador: currentUser.value.id,
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

  // Eliminar Evento
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


<style scoped lang="scss">
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
    background-color: #0f4f42;
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
    flex-wrap: wrap;
    gap: 20px;
  }

  .campo {
    flex: 1 1 300px;
    display: flex;
    flex-direction: column;
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

  #exito {
    color: #339636;
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

  .btn-asignar-ubicacion {
    padding: 10px;
    background-color: #0F4F42;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-asignar-ubicacion:hover {
    background-color: #0c3b32;
  }

  .texto-emergencia {
    font-size: 0.9rem;
    color: #555;
    margin-top: 8px;
  }
</style><template>
  <div>
    <!-- Encabezado con título y botón -->
    <header class="botonYTitulo">
      <BotonPaginaAnterior />
      <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
    </header>

    <!-- Sección de información del evento -->
    <section class="infoEvento">
      <div class="infoEventoEInputs">
        <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
      </div>

      <div class="contenedorInputs">
        <div class="inputsInfo">
          <!-- Nombre del Evento -->
          <div class="campo">
            <label for="eventoNombre" class="tituloDeInput"><strong>Nombre del evento</strong></label>
            <input
              id="eventoNombre"
              class="inputInfoEvento"
              type="text"
              v-model="evento.nombre"
              required
              placeholder="Ejemplo: Ayuda para María"
            />
            <p v-if="!evento.nombre" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Descripción del Evento -->
          <div class="campo">
            <label for="eventoDescripcion" class="tituloDeInput"><strong>Descripción del evento</strong></label>
            <textarea
              id="eventoDescripcion"
              class="inputInfoEvento"
              v-model="evento.descripcion"
              placeholder="Ejemplo: Hola, buenos días..."
            ></textarea>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Causa del Evento -->
          <div class="campo">
            <label for="eventoCausa" class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></label>
            <input
              id="eventoCausa"
              class="inputInfoEvento"
              type="text"
              v-model="evento.causa"
              required
              placeholder="Ejemplo: Incendio de vivienda"
            />
            <p v-if="!evento.causa" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Ubicación del Evento -->
          <div class="campo">
            <label for="eventoUbicacion" class="tituloDeInput"><strong>Ubicación del evento</strong></label>
            <SelectMunicipios v-model="evento.ubicacion.municipio_id" :municipios="municipios" />
            <label for="asignarUbicacion" class="tituloDeInput"><strong>O también asigna una ubicación en tiempo real</strong></label>
            <button
              id="asignarUbicacion"
              class="btn-asignar-ubicacion"
              type="button"
              @click="asignarUbicacion"
              :disabled="loading"
            >
              {{ loading ? 'Asignando ubicación...' : 'Asignar Ubicación' }}
            </button>

            <!-- Mensajes de error y éxito -->
            <p v-if="msgFalla" class="texto-emergencia">
              <strong>Hubo un error al asignar la ubicación.</strong>
            </p>
            <p v-if="msgExito" class="texto-emergencia">
              <strong>Se asignó correctamente la ubicación a este evento.</strong>
            </p>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Categoría de donaciones -->
          <div class="campo">
            <label for="eventoDonacion" class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></label>
            <select id="eventoDonacion" v-model="evento.donacion_id" required>
              <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                {{ donacion.nombre }}
              </option>
            </select>
          </div>

          <!-- Fecha del Evento -->
          <div class="campo">
            <label for="eventoFecha" class="tituloDeInput"><strong>Fecha Evento</strong></label>
            <input id="eventoFecha" class="inputInfoEvento" type="date" v-model="evento.fecha" />
          </div>
        </div>

        <!-- Imágenes -->
        <div class="inputsInfo">
          <div class="addIMGS">
            <label class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></label>
            <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
          </div>
        </div>
      </div>
    </section>

    <!-- Botón de acción para guardar -->
    <footer class="boton">
      <ButtonDefault
        size="default"
        color="azul"
        :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
        icono="archive"
        class="Publicar"
        @click="guardarEvento"
      />
    </footer>

    <!-- Botón de eliminar evento si estamos en modo edición -->
    <ButtonDefault
      v-if="modoEdicion"
      size="default"
      color="rojo"
      text="Eliminar Evento"
      @click="eliminarEvento"
    />

    <FooterComponent />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';

  // Import services to consume API
  import EventosService from '../services/eventos';
  import { getCurrentUser } from '../services/users';

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
  const municipios = ref([]);
  
  const msgFalla = ref(false); 
  const msgExito = ref(false); 
  const errorMsg = ref("");
  const loading = ref(false);

  onMounted(async () => {
    try {
      // Obtener usuario autenticado
      const userResponse = await getCurrentUser();
      currentUser.value = userResponse;

      // Obtener donaciones
      donaciones.value = await getDonaciones();

      // Obtener municipios
      const response = await api.get('/ubicacion/lista_city/');
      municipios.value = response.data;

      // Cargar datos del evento si estamos en modo edición
      if (modoEdicion) {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
        
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      }
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      alert("Hubo un error al cargar los datos.");
    }
  });

  // Asignar ubicación con geolocalización
  async function asignarUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "Este navegador no soporta geolocalización.";
        return;
    }

    loading.value = true;
    errorMsg.value = "";
    msgFalla.value = false;
    msgExito.value = false;

    try {
      navigator.geolocation.getCurrentPosition(async (position) => {
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        evento.value.ubicacion.latitud = latitud;
        evento.value.ubicacion.longitud = longitud;

        msgExito.value = true;
        console.log("Ubicación asignada correctamente:", latitud, longitud);
      }, (err) => {
        msgFalla.value = true;
        errorMsg.value = "Error al obtener la ubicación: " + err.message;
        console.log(errorMsg.value);
      });
    } catch (error) {
      msgFalla.value = true;
      errorMsg.value = "Error al obtener la ubicación";
      console.error(errorMsg.value);
    } finally {
      loading.value = false;
    }
  }
  
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
        organizador: currentUser.value.id,
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

  // Eliminar Evento
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


<style scoped lang="scss">
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
    background-color: #0f4f42;
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
    flex-wrap: wrap;
    gap: 20px;
  }

  .campo {
    flex: 1 1 300px;
    display: flex;
    flex-direction: column;
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

  #exito {
    color: #339636;
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

  .btn-asignar-ubicacion {
    padding: 10px;
    background-color: #0F4F42;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-asignar-ubicacion:hover {
    background-color: #0c3b32;
  }

  .texto-emergencia {
    font-size: 0.9rem;
    color: #555;
    margin-top: 8px;
  }
</style><template>
  <div>
    <!-- Encabezado con título y botón -->
    <header class="botonYTitulo">
      <BotonPaginaAnterior />
      <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
    </header>

    <!-- Sección de información del evento -->
    <section class="infoEvento">
      <div class="infoEventoEInputs">
        <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
      </div>

      <div class="contenedorInputs">
        <div class="inputsInfo">
          <!-- Nombre del Evento -->
          <div class="campo">
            <label for="eventoNombre" class="tituloDeInput"><strong>Nombre del evento</strong></label>
            <input
              id="eventoNombre"
              class="inputInfoEvento"
              type="text"
              v-model="evento.nombre"
              required
              placeholder="Ejemplo: Ayuda para María"
            />
            <p v-if="!evento.nombre" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Descripción del Evento -->
          <div class="campo">
            <label for="eventoDescripcion" class="tituloDeInput"><strong>Descripción del evento</strong></label>
            <textarea
              id="eventoDescripcion"
              class="inputInfoEvento"
              v-model="evento.descripcion"
              placeholder="Ejemplo: Hola, buenos días..."
            ></textarea>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Causa del Evento -->
          <div class="campo">
            <label for="eventoCausa" class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></label>
            <input
              id="eventoCausa"
              class="inputInfoEvento"
              type="text"
              v-model="evento.causa"
              required
              placeholder="Ejemplo: Incendio de vivienda"
            />
            <p v-if="!evento.causa" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Ubicación del Evento -->
          <div class="campo">
            <label for="eventoUbicacion" class="tituloDeInput"><strong>Ubicación del evento</strong></label>
            <SelectMunicipios v-model="evento.ubicacion.municipio_id" :municipios="municipios" />
            <label for="asignarUbicacion" class="tituloDeInput"><strong>O también asigna una ubicación en tiempo real</strong></label>
            <button
              id="asignarUbicacion"
              class="btn-asignar-ubicacion"
              type="button"
              @click="asignarUbicacion"
              :disabled="loading"
            >
              {{ loading ? 'Asignando ubicación...' : 'Asignar Ubicación' }}
            </button>

            <!-- Mensajes de error y éxito -->
            <p v-if="msgFalla" class="texto-emergencia">
              <strong>Hubo un error al asignar la ubicación.</strong>
            </p>
            <p v-if="msgExito" class="texto-emergencia">
              <strong>Se asignó correctamente la ubicación a este evento.</strong>
            </p>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Categoría de donaciones -->
          <div class="campo">
            <label for="eventoDonacion" class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></label>
            <select id="eventoDonacion" v-model="evento.donacion_id" required>
              <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                {{ donacion.nombre }}
              </option>
            </select>
          </div>

          <!-- Fecha del Evento -->
          <div class="campo">
            <label for="eventoFecha" class="tituloDeInput"><strong>Fecha Evento</strong></label>
            <input id="eventoFecha" class="inputInfoEvento" type="date" v-model="evento.fecha" />
          </div>
        </div>

        <!-- Imágenes -->
        <div class="inputsInfo">
          <div class="addIMGS">
            <label class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></label>
            <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
          </div>
        </div>
      </div>
    </section>

    <!-- Botón de acción para guardar -->
    <footer class="boton">
      <ButtonDefault
        size="default"
        color="azul"
        :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
        icono="archive"
        class="Publicar"
        @click="guardarEvento"
      />
    </footer>

    <!-- Botón de eliminar evento si estamos en modo edición -->
    <ButtonDefault
      v-if="modoEdicion"
      size="default"
      color="rojo"
      text="Eliminar Evento"
      @click="eliminarEvento"
    />

    <FooterComponent />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';

  // Import services to consume API
  import EventosService from '../services/eventos';
  import { getCurrentUser } from '../services/users';

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
  const municipios = ref([]);
  
  const msgFalla = ref(false); 
  const msgExito = ref(false); 
  const errorMsg = ref("");
  const loading = ref(false);

  onMounted(async () => {
    try {
      // Obtener usuario autenticado
      const userResponse = await getCurrentUser();
      currentUser.value = userResponse;

      // Obtener donaciones
      donaciones.value = await getDonaciones();

      // Obtener municipios
      const response = await api.get('/ubicacion/lista_city/');
      municipios.value = response.data;

      // Cargar datos del evento si estamos en modo edición
      if (modoEdicion) {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
        
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      }
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      alert("Hubo un error al cargar los datos.");
    }
  });

  // Asignar ubicación con geolocalización
  async function asignarUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "Este navegador no soporta geolocalización.";
        return;
    }

    loading.value = true;
    errorMsg.value = "";
    msgFalla.value = false;
    msgExito.value = false;

    try {
      navigator.geolocation.getCurrentPosition(async (position) => {
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        evento.value.ubicacion.latitud = latitud;
        evento.value.ubicacion.longitud = longitud;

        msgExito.value = true;
        console.log("Ubicación asignada correctamente:", latitud, longitud);
      }, (err) => {
        msgFalla.value = true;
        errorMsg.value = "Error al obtener la ubicación: " + err.message;
        console.log(errorMsg.value);
      });
    } catch (error) {
      msgFalla.value = true;
      errorMsg.value = "Error al obtener la ubicación";
      console.error(errorMsg.value);
    } finally {
      loading.value = false;
    }
  }
  
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
        organizador: currentUser.value.id,
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

  // Eliminar Evento
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


<style scoped lang="scss">
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
    background-color: #0f4f42;
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
    flex-wrap: wrap;
    gap: 20px;
  }

  .campo {
    flex: 1 1 300px;
    display: flex;
    flex-direction: column;
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

  #exito {
    color: #339636;
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

  .btn-asignar-ubicacion {
    padding: 10px;
    background-color: #0F4F42;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-asignar-ubicacion:hover {
    background-color: #0c3b32;
  }

  .texto-emergencia {
    font-size: 0.9rem;
    color: #555;
    margin-top: 8px;
  }
</style><template>
  <div>
    <!-- Encabezado con título y botón -->
    <header class="botonYTitulo">
      <BotonPaginaAnterior />
      <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
    </header>

    <!-- Sección de información del evento -->
    <section class="infoEvento">
      <div class="infoEventoEInputs">
        <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
      </div>

      <div class="contenedorInputs">
        <div class="inputsInfo">
          <!-- Nombre del Evento -->
          <div class="campo">
            <label for="eventoNombre" class="tituloDeInput"><strong>Nombre del evento</strong></label>
            <input
              id="eventoNombre"
              class="inputInfoEvento"
              type="text"
              v-model="evento.nombre"
              required
              placeholder="Ejemplo: Ayuda para María"
            />
            <p v-if="!evento.nombre" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Descripción del Evento -->
          <div class="campo">
            <label for="eventoDescripcion" class="tituloDeInput"><strong>Descripción del evento</strong></label>
            <textarea
              id="eventoDescripcion"
              class="inputInfoEvento"
              v-model="evento.descripcion"
              placeholder="Ejemplo: Hola, buenos días..."
            ></textarea>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Causa del Evento -->
          <div class="campo">
            <label for="eventoCausa" class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></label>
            <input
              id="eventoCausa"
              class="inputInfoEvento"
              type="text"
              v-model="evento.causa"
              required
              placeholder="Ejemplo: Incendio de vivienda"
            />
            <p v-if="!evento.causa" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Ubicación del Evento -->
          <div class="campo">
            <label for="eventoUbicacion" class="tituloDeInput"><strong>Ubicación del evento</strong></label>
            <SelectMunicipios v-model="evento.ubicacion.municipio_id" :municipios="municipios" />
            <label for="asignarUbicacion" class="tituloDeInput"><strong>O también asigna una ubicación en tiempo real</strong></label>
            <button
              id="asignarUbicacion"
              class="btn-asignar-ubicacion"
              type="button"
              @click="asignarUbicacion"
              :disabled="loading"
            >
              {{ loading ? 'Asignando ubicación...' : 'Asignar Ubicación' }}
            </button>

            <!-- Mensajes de error y éxito -->
            <p v-if="msgFalla" class="texto-emergencia">
              <strong>Hubo un error al asignar la ubicación.</strong>
            </p>
            <p v-if="msgExito" class="texto-emergencia">
              <strong>Se asignó correctamente la ubicación a este evento.</strong>
            </p>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Categoría de donaciones -->
          <div class="campo">
            <label for="eventoDonacion" class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></label>
            <select id="eventoDonacion" v-model="evento.donacion_id" required>
              <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                {{ donacion.nombre }}
              </option>
            </select>
          </div>

          <!-- Fecha del Evento -->
          <div class="campo">
            <label for="eventoFecha" class="tituloDeInput"><strong>Fecha Evento</strong></label>
            <input id="eventoFecha" class="inputInfoEvento" type="date" v-model="evento.fecha" />
          </div>
        </div>

        <!-- Imágenes -->
        <div class="inputsInfo">
          <div class="addIMGS">
            <label class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></label>
            <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
          </div>
        </div>
      </div>
    </section>

    <!-- Botón de acción para guardar -->
    <footer class="boton">
      <ButtonDefault
        size="default"
        color="azul"
        :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
        icono="archive"
        class="Publicar"
        @click="guardarEvento"
      />
    </footer>

    <!-- Botón de eliminar evento si estamos en modo edición -->
    <ButtonDefault
      v-if="modoEdicion"
      size="default"
      color="rojo"
      text="Eliminar Evento"
      @click="eliminarEvento"
    />

    <FooterComponent />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';

  // Import services to consume API
  import EventosService from '../services/eventos';
  import { getCurrentUser } from '../services/users';

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
  const municipios = ref([]);
  
  const msgFalla = ref(false); 
  const msgExito = ref(false); 
  const errorMsg = ref("");
  const loading = ref(false);

  onMounted(async () => {
    try {
      // Obtener usuario autenticado
      const userResponse = await getCurrentUser();
      currentUser.value = userResponse;

      // Obtener donaciones
      donaciones.value = await getDonaciones();

      // Obtener municipios
      const response = await api.get('/ubicacion/lista_city/');
      municipios.value = response.data;

      // Cargar datos del evento si estamos en modo edición
      if (modoEdicion) {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
        
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      }
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      alert("Hubo un error al cargar los datos.");
    }
  });

  // Asignar ubicación con geolocalización
  async function asignarUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "Este navegador no soporta geolocalización.";
        return;
    }

    loading.value = true;
    errorMsg.value = "";
    msgFalla.value = false;
    msgExito.value = false;

    try {
      navigator.geolocation.getCurrentPosition(async (position) => {
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        evento.value.ubicacion.latitud = latitud;
        evento.value.ubicacion.longitud = longitud;

        msgExito.value = true;
        console.log("Ubicación asignada correctamente:", latitud, longitud);
      }, (err) => {
        msgFalla.value = true;
        errorMsg.value = "Error al obtener la ubicación: " + err.message;
        console.log(errorMsg.value);
      });
    } catch (error) {
      msgFalla.value = true;
      errorMsg.value = "Error al obtener la ubicación";
      console.error(errorMsg.value);
    } finally {
      loading.value = false;
    }
  }
  
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
        organizador: currentUser.value.id,
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

  // Eliminar Evento
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


<style scoped lang="scss">
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
    background-color: #0f4f42;
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
    flex-wrap: wrap;
    gap: 20px;
  }

  .campo {
    flex: 1 1 300px;
    display: flex;
    flex-direction: column;
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

  #exito {
    color: #339636;
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

  .btn-asignar-ubicacion {
    padding: 10px;
    background-color: #0F4F42;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-asignar-ubicacion:hover {
    background-color: #0c3b32;
  }

  .texto-emergencia {
    font-size: 0.9rem;
    color: #555;
    margin-top: 8px;
  }
</style><template>
  <div>
    <!-- Encabezado con título y botón -->
    <header class="botonYTitulo">
      <BotonPaginaAnterior />
      <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
    </header>

    <!-- Sección de información del evento -->
    <section class="infoEvento">
      <div class="infoEventoEInputs">
        <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
      </div>

      <div class="contenedorInputs">
        <div class="inputsInfo">
          <!-- Nombre del Evento -->
          <div class="campo">
            <label for="eventoNombre" class="tituloDeInput"><strong>Nombre del evento</strong></label>
            <input
              id="eventoNombre"
              class="inputInfoEvento"
              type="text"
              v-model="evento.nombre"
              required
              placeholder="Ejemplo: Ayuda para María"
            />
            <p v-if="!evento.nombre" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Descripción del Evento -->
          <div class="campo">
            <label for="eventoDescripcion" class="tituloDeInput"><strong>Descripción del evento</strong></label>
            <textarea
              id="eventoDescripcion"
              class="inputInfoEvento"
              v-model="evento.descripcion"
              placeholder="Ejemplo: Hola, buenos días..."
            ></textarea>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Causa del Evento -->
          <div class="campo">
            <label for="eventoCausa" class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></label>
            <input
              id="eventoCausa"
              class="inputInfoEvento"
              type="text"
              v-model="evento.causa"
              required
              placeholder="Ejemplo: Incendio de vivienda"
            />
            <p v-if="!evento.causa" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Ubicación del Evento -->
          <div class="campo">
            <label for="eventoUbicacion" class="tituloDeInput"><strong>Ubicación del evento</strong></label>
            <SelectMunicipios v-model="evento.ubicacion.municipio_id" :municipios="municipios" />
            <label for="asignarUbicacion" class="tituloDeInput"><strong>O también asigna una ubicación en tiempo real</strong></label>
            <button
              id="asignarUbicacion"
              class="btn-asignar-ubicacion"
              type="button"
              @click="asignarUbicacion"
              :disabled="loading"
            >
              {{ loading ? 'Asignando ubicación...' : 'Asignar Ubicación' }}
            </button>

            <!-- Mensajes de error y éxito -->
            <p v-if="msgFalla" class="texto-emergencia">
              <strong>Hubo un error al asignar la ubicación.</strong>
            </p>
            <p v-if="msgExito" class="texto-emergencia">
              <strong>Se asignó correctamente la ubicación a este evento.</strong>
            </p>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Categoría de donaciones -->
          <div class="campo">
            <label for="eventoDonacion" class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></label>
            <select id="eventoDonacion" v-model="evento.donacion_id" required>
              <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                {{ donacion.nombre }}
              </option>
            </select>
          </div>

          <!-- Fecha del Evento -->
          <div class="campo">
            <label for="eventoFecha" class="tituloDeInput"><strong>Fecha Evento</strong></label>
            <input id="eventoFecha" class="inputInfoEvento" type="date" v-model="evento.fecha" />
          </div>
        </div>

        <!-- Imágenes -->
        <div class="inputsInfo">
          <div class="addIMGS">
            <label class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></label>
            <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
          </div>
        </div>
      </div>
    </section>

    <!-- Botón de acción para guardar -->
    <footer class="boton">
      <ButtonDefault
        size="default"
        color="azul"
        :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
        icono="archive"
        class="Publicar"
        @click="guardarEvento"
      />
    </footer>

    <!-- Botón de eliminar evento si estamos en modo edición -->
    <ButtonDefault
      v-if="modoEdicion"
      size="default"
      color="rojo"
      text="Eliminar Evento"
      @click="eliminarEvento"
    />

    <FooterComponent />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';

  // Import services to consume API
  import EventosService from '../services/eventos';
  import { getCurrentUser } from '../services/users';

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
  const municipios = ref([]);
  
  const msgFalla = ref(false); 
  const msgExito = ref(false); 
  const errorMsg = ref("");
  const loading = ref(false);

  onMounted(async () => {
    try {
      // Obtener usuario autenticado
      const userResponse = await getCurrentUser();
      currentUser.value = userResponse;

      // Obtener donaciones
      donaciones.value = await getDonaciones();

      // Obtener municipios
      const response = await api.get('/ubicacion/lista_city/');
      municipios.value = response.data;

      // Cargar datos del evento si estamos en modo edición
      if (modoEdicion) {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
        
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      }
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      alert("Hubo un error al cargar los datos.");
    }
  });

  // Asignar ubicación con geolocalización
  async function asignarUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "Este navegador no soporta geolocalización.";
        return;
    }

    loading.value = true;
    errorMsg.value = "";
    msgFalla.value = false;
    msgExito.value = false;

    try {
      navigator.geolocation.getCurrentPosition(async (position) => {
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        evento.value.ubicacion.latitud = latitud;
        evento.value.ubicacion.longitud = longitud;

        msgExito.value = true;
        console.log("Ubicación asignada correctamente:", latitud, longitud);
      }, (err) => {
        msgFalla.value = true;
        errorMsg.value = "Error al obtener la ubicación: " + err.message;
        console.log(errorMsg.value);
      });
    } catch (error) {
      msgFalla.value = true;
      errorMsg.value = "Error al obtener la ubicación";
      console.error(errorMsg.value);
    } finally {
      loading.value = false;
    }
  }
  
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
        organizador: currentUser.value.id,
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

  // Eliminar Evento
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


<style scoped lang="scss">
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
    background-color: #0f4f42;
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
    flex-wrap: wrap;
    gap: 20px;
  }

  .campo {
    flex: 1 1 300px;
    display: flex;
    flex-direction: column;
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

  #exito {
    color: #339636;
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

  .btn-asignar-ubicacion {
    padding: 10px;
    background-color: #0F4F42;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-asignar-ubicacion:hover {
    background-color: #0c3b32;
  }

  .texto-emergencia {
    font-size: 0.9rem;
    color: #555;
    margin-top: 8px;
  }
</style><template>
  <div>
    <!-- Encabezado con título y botón -->
    <header class="botonYTitulo">
      <BotonPaginaAnterior />
      <h1>{{ modoEdicion ? 'Editar Evento' : 'Crea tu Evento' }}</h1>
    </header>

    <!-- Sección de información del evento -->
    <section class="infoEvento">
      <div class="infoEventoEInputs">
        <h3 id="subtitulo">INFORMACIÓN DEL EVENTO</h3>
      </div>

      <div class="contenedorInputs">
        <div class="inputsInfo">
          <!-- Nombre del Evento -->
          <div class="campo">
            <label for="eventoNombre" class="tituloDeInput"><strong>Nombre del evento</strong></label>
            <input
              id="eventoNombre"
              class="inputInfoEvento"
              type="text"
              v-model="evento.nombre"
              required
              placeholder="Ejemplo: Ayuda para María"
            />
            <p v-if="!evento.nombre" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Descripción del Evento -->
          <div class="campo">
            <label for="eventoDescripcion" class="tituloDeInput"><strong>Descripción del evento</strong></label>
            <textarea
              id="eventoDescripcion"
              class="inputInfoEvento"
              v-model="evento.descripcion"
              placeholder="Ejemplo: Hola, buenos días..."
            ></textarea>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Causa del Evento -->
          <div class="campo">
            <label for="eventoCausa" class="tituloDeInput"><strong>Causa por la que se crea el evento</strong></label>
            <input
              id="eventoCausa"
              class="inputInfoEvento"
              type="text"
              v-model="evento.causa"
              required
              placeholder="Ejemplo: Incendio de vivienda"
            />
            <p v-if="!evento.causa" class="spanYCampoRequer">
              <span class="material-symbols-outlined campoRequerido" style="font-variation-settings: 'FILL' 1;">
                circle
              </span>
              <strong>Campo requerido</strong>
            </p>
          </div>

          <!-- Ubicación del Evento -->
          <div class="campo">
            <label for="eventoUbicacion" class="tituloDeInput"><strong>Ubicación del evento</strong></label>
            <SelectMunicipios v-model="evento.ubicacion.municipio_id" :municipios="municipios" />
            <label for="asignarUbicacion" class="tituloDeInput"><strong>O también asigna una ubicación en tiempo real</strong></label>
            <button
              id="asignarUbicacion"
              class="btn-asignar-ubicacion"
              type="button"
              @click="asignarUbicacion"
              :disabled="loading"
            >
              {{ loading ? 'Asignando ubicación...' : 'Asignar Ubicación' }}
            </button>

            <!-- Mensajes de error y éxito -->
            <p v-if="msgFalla" class="texto-emergencia">
              <strong>Hubo un error al asignar la ubicación.</strong>
            </p>
            <p v-if="msgExito" class="texto-emergencia">
              <strong>Se asignó correctamente la ubicación a este evento.</strong>
            </p>
          </div>
        </div>

        <div class="inputsInfo">
          <!-- Categoría de donaciones -->
          <div class="campo">
            <label for="eventoDonacion" class="tituloDeInput"><strong>Categoría de donaciones aceptadas</strong></label>
            <select id="eventoDonacion" v-model="evento.donacion_id" required>
              <option v-for="donacion in donaciones" :key="donacion.id" :value="donacion.id">
                {{ donacion.nombre }}
              </option>
            </select>
          </div>

          <!-- Fecha del Evento -->
          <div class="campo">
            <label for="eventoFecha" class="tituloDeInput"><strong>Fecha Evento</strong></label>
            <input id="eventoFecha" class="inputInfoEvento" type="date" v-model="evento.fecha" />
          </div>
        </div>

        <!-- Imágenes -->
        <div class="inputsInfo">
          <div class="addIMGS">
            <label class="tituloDeInput"><strong>Imágenes de lo ocurrido</strong></label>
            <CargarImagenes ref="cargarImagenes" :imagenes-existente="evento.imagenes" />
          </div>
        </div>
      </div>
    </section>

    <!-- Botón de acción para guardar -->
    <footer class="boton">
      <ButtonDefault
        size="default"
        color="azul"
        :text="modoEdicion ? 'Guardar Cambios' : 'Publicar'"
        icono="archive"
        class="Publicar"
        @click="guardarEvento"
      />
    </footer>

    <!-- Botón de eliminar evento si estamos en modo edición -->
    <ButtonDefault
      v-if="modoEdicion"
      size="default"
      color="rojo"
      text="Eliminar Evento"
      @click="eliminarEvento"
    />

    <FooterComponent />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  import BotonPaginaAnterior from '../components/BotonPaginaAnterior.vue';
  import ButtonDefault from '@/components/ButtonDefault.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  import SelectMunicipios from '@/components/SelectMunicipios.vue';
  import CargarImagenes from '@/components/CargarImagenes.vue';

  // Import services to consume API
  import EventosService from '../services/eventos';
  import { getCurrentUser } from '../services/users';

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
  const municipios = ref([]);
  
  const msgFalla = ref(false); 
  const msgExito = ref(false); 
  const errorMsg = ref("");
  const loading = ref(false);

  onMounted(async () => {
    try {
      // Obtener usuario autenticado
      const userResponse = await getCurrentUser();
      currentUser.value = userResponse;

      // Obtener donaciones
      donaciones.value = await getDonaciones();

      // Obtener municipios
      const response = await api.get('/ubicacion/lista_city/');
      municipios.value = response.data;

      // Cargar datos del evento si estamos en modo edición
      if (modoEdicion) {
        const eventoResponse = await getEventoById(eventoId);
        evento.value = { ...eventoResponse };
        
        if (eventoResponse.ubicacion) {
          evento.value.ubicacion.municipio_id = eventoResponse.ubicacion.municipio_id;
        }
        if (eventoResponse.donacion_id) {
          evento.value.donacion_id = eventoResponse.donacion_id;
        }
      }
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      alert("Hubo un error al cargar los datos.");
    }
  });

  // Asignar ubicación con geolocalización
  async function asignarUbicacion() {
    if (!("geolocation" in navigator)) {
        errorMsg.value = "Este navegador no soporta geolocalización.";
        return;
    }

    loading.value = true;
    errorMsg.value = "";
    msgFalla.value = false;
    msgExito.value = false;

    try {
      navigator.geolocation.getCurrentPosition(async (position) => {
        const latitud = position.coords.latitude;
        const longitud = position.coords.longitude;

        evento.value.ubicacion.latitud = latitud;
        evento.value.ubicacion.longitud = longitud;

        msgExito.value = true;
        console.log("Ubicación asignada correctamente:", latitud, longitud);
      }, (err) => {
        msgFalla.value = true;
        errorMsg.value = "Error al obtener la ubicación: " + err.message;
        console.log(errorMsg.value);
      });
    } catch (error) {
      msgFalla.value = true;
      errorMsg.value = "Error al obtener la ubicación";
      console.error(errorMsg.value);
    } finally {
      loading.value = false;
    }
  }
  
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
        organizador: currentUser.value.id,
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

  // Eliminar Evento
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


<style scoped lang="scss">
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
    background-color: #0f4f42;
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
    flex-wrap: wrap;
    gap: 20px;
  }

  .campo {
    flex: 1 1 300px;
    display: flex;
    flex-direction: column;
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

  #exito {
    color: #339636;
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

  .btn-asignar-ubicacion {
    padding: 10px;
    background-color: #0F4F42;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-asignar-ubicacion:hover {
    background-color: #0c3b32;
  }

  .texto-emergencia {
    font-size: 0.9rem;
    color: #555;
    margin-top: 8px;
  }
</style>