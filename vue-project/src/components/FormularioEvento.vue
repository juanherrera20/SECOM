<template>
  <!-- Encabezado con título y botón -->
  <header class="botonYTitulo">
    <BotonPaginaAnterior />
    <h1>Crea tu Evento</h1>
  </header>

  <form @submit.prevent="handleSubmit">
    <section class="form-section">
      <div class="form-container">
        <h2>Información Principal</h2>

        <div class="input-box">
          <label class="input-label">Nombre del Evento</label>
          <input
            placeholder="Recaudación de fondos Niños Huerfanos"
            class="input"
            v-model="formData.name"
            type="text"
            required
            :disabled="false"
          />
          <span class="input-helper">Ingresar Nombre principal para el Evento</span>
        </div>

        <div class="input-box">
          <label class="input-label">Fecha de Reunión</label>
          <input
            type="date"
            class="input date"
            name="fecha"
            v-model="formData.meet_date"
          />
          <span class="input-helper">Ingresar Fecha de Reunión definida para el evento</span>
        </div>

        <SelectInput
          v-model="formData.donation_id"
          :options="donations"
          label="Tipo de Donación *"
          extra="Seleccionar el tipo de donación que se va a recibir"
          :isRequired="true"
          :isDesabled="false"
        ></SelectInput>

        <div class="input-box">
          <label class="input-label">Descripción *</label>
          <textarea
            placeholder="Agregar Una Descripción"
            class="input textarea"
            v-model="formData.description"
            :disabled="false"
            :required="true"
          ></textarea>
          <span class="input-helper">Ingrese la Información Principal del Evento</span>
        </div>
      </div>

      <div class="form-container">
        <h2>Ubicación y localización del Evento</h2>

        <div class="location-info">
          <p class="location-description">
            Es necesario ubicar el evento mediante GPS. Por favor elija usar
            ubicación actual o seleccionar una ciudad en el menú desplegable.
          </p>

          <div class="location-grid">
            <!-- Columna izquierda -->
            <div class="location-column">
              <SelectInput
                v-model="formData.ubicacion.city_id"
                :options="cities"
                label="Ciudad"
                extra="Seleccionar la ciudad donde se va a realizar el evento"
                :isRequired="false"
                :isDesabled="false"
              ></SelectInput>

              <div class="input-box">
                <label class="input-label">Nombre del Lugar</label>
                <input
                  placeholder="Ej: Caseta Comunal Barrio Sonda"
                  class="input"
                  v-model="formData.ubicacion.name"
                  type="text"
                  :disabled="false"
                />
                <span class="input-helper">Nombre del lugar (Local, Sector, Barrio, etc)</span>
              </div>
            </div>

            <!-- Columna derecha -->
            <div class="location-column">
              <div class="input-box">
                <label class="input-label">Dirección *</label>
                <input
                  placeholder="Ej: Carrera 4ta #56-34"
                  class="input"
                  v-model="formData.ubicacion.address"
                  type="text"
                  required
                  :disabled="false"
                />
                <span class="input-helper">Dirección exacta del Evento</span>
              </div>

              <SelectInput
                v-model="formData.ubicacion.pais"
                :options="countries"
                label="País"
                extra="Seleccionar el país del evento"
                :isRequired="false"
                :isDesabled="false"
              ></SelectInput>
            </div>
          </div>

          <!-- Sección de geolocalización -->
          <div class="geolocation-section">
            <label class="geolocation-label">Ubicación GPS (Opcional)</label>
            <p class="geolocation-help">
              Puede asignar coordenadas exactas usando su ubicación actual
            </p>

            <div class="geolocation-controls">
              <button
                class="btn-asignar-ubicacion"
                type="button"
                @click="asignUbication"
                :disabled="loading"
              >
                {{ loading ? "Obteniendo ubicación..." : "Usar mi ubicación actual" }}
              </button>

              <div
                v-if="msgExist"
                class="geolocation-feedback"
                :class="{ success: msg.includes('correctamente'), error: msg.includes('Error') }"
              >
                <span>{{ msg }}</span>
              </div>
            </div>

            <div
              v-if="formData.ubicacion.latitude && formData.ubicacion.longitude"
              class="coordinates-display"
            >
              <span>Latitud: {{ formData.ubicacion.latitude.toFixed(6) }}</span>
              <span>Longitud: {{ formData.ubicacion.longitude.toFixed(6) }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="files-container">
        <h2>Imágenes/Fotos del Evento</h2>
        <input
          type="file"
          @change="handleImageUpdload"
          multiple
          accept="image/*"
        />
        <div v-if="selectedImages.length > 0" class="selected-images">
          <h3>Imágenes Seleccionadas</h3>
          <div
            v-for="(img, index) in selectedImages"
            :key="index"
            class="images-list"
          >
            <img
              :src="getImagePreview(img)"
              :alt="img.name"
              class="property-image"
            />
            <button
              @click="removeImage(index)"
              class="remove-file"
              type="button"
            >
              ✕
            </button>
          </div>
        </div>
      </div>

      <div class="form-actions">
        <button type="submit" class="submit-button">Publicar</button>
      </div>
    </section>
  </form>
  <FooterComponent />
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

import BotonPaginaAnterior from "../components/BotonPaginaAnterior.vue";
import FooterComponent from "@/components/FooterComponent.vue";
import SelectInput from "@/components/SelectInput.vue";

import EventosService from "../services/eventos";
import UbicacionService from "@/services/ubicacion";
import { getCurrentUser } from "../services/users";

const route = useRoute();
const router = useRouter();
const countries = ref([
  { id: "Colombia", name: "Colombia" },
  { id: "Ecuador", name: "Ecuador" },
  { id: "Peru", name: "Peru" },
]);
const msg = ref("");
const msgExist = ref(false);
const loading = ref(false);
const selectedImages = ref([]);
const eventoID = ref(null);

const formData = ref({
  name: "",
  meet_date: "",
  organizador: null,
  description: "",
  donation_id: null,
  ubicacion: {
    city_id: null,
    name: "",
    address: "",
    latitude: null,
    longitude: null,
    pais: null,
  },
});

const donations = ref([]);
const cities = ref([]);

onMounted(async () => {
  try {
    const [citiesResponse, donationsResponse] = await Promise.all([
      UbicacionService.getCities(),
      EventosService.getDonations(),
    ]);

    cities.value = citiesResponse;
    donations.value = donationsResponse;

    console.log("Cities:", cities.value);
    console.log("Donations:", donations.value);
  } catch (error) {
    console.error("Error cargando datos iniciales:", error);
  }
});

async function asignUbication() {
  if (!("geolocation" in navigator)) {
    msg.value = "Este navegador no soporta geolocalización.";
    msgExist.value = true;
    return;
  }

  loading.value = true;
  msg.value = "";
  msgExist.value = false;

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const latitud = position.coords.latitude;
      const longitud = position.coords.longitude;

      formData.value.ubicacion.latitude = Number(latitud.toFixed(6));
      formData.value.ubicacion.longitude = Number(longitud.toFixed(6));

      msg.value = "Ubicación asignada correctamente";
      msgExist.value = true;

      console.log("Ubicación asignada correctamente:", latitud, longitud);
      loading.value = false;
    },
    (error) => {
      msg.value = "Error al obtener la ubicación: " + error.message;
      msgExist.value = true;
      loading.value = false;
    }
  );
}

const handleSubmit = async () => {
  msg.value = "";
  msgExist.value = false;

  if (
    !formData.value.ubicacion.city_id &&
    (!formData.value.ubicacion.latitude || !formData.value.ubicacion.longitude)
  ) {
    msg.value = "Debes seleccionar una ciudad o asignar tu ubicación actual.";
    msgExist.value = true;
    return;
  }

  const currentUser = await getCurrentUser();
  formData.value.organizador = currentUser.id;

  try {
    const response = await EventosService.createEvento(formData.value);
    console.log("Evento creado:", response);
    eventoID.value = response.id;

    await uploadImages();
    router.push({ name: "EventosList" });
  } catch (error) {
    console.error("Error al crear el evento:", error);
    msg.value = "Error al crear el evento. Por favor, inténtalo de nuevo.";
    msgExist.value = true;
  }
};

const handleImageUpdload = (event) => {
  const newImages = Array.from(event.target.files);
  selectedImages.value = [...selectedImages.value, ...newImages];
};

const removeImage = (index) => {
  selectedImages.value.splice(index, 1);
};

const getImagePreview = (file) => {
  return URL.createObjectURL(file);
};

const uploadImages = async () => {
  if (!eventoID.value || selectedImages.value.length === 0) {
    return;
  }

  try {
    const formData = new FormData();
    selectedImages.value.forEach((file) => {
      formData.append("new_images", file);
    });

    await EventosService.manageImages(eventoID.value, formData);
    console.log("Imágenes subidas con éxito");
  } catch (error) {
    console.error("Error al subir las imágenes:", error);
  }
};
</script>



<style scoped lang="scss">
  .form-section {
    margin: 0 auto;
    padding: 0px 2rem;
    margin-bottom: 4rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .botonYTitulo {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  h1 {
    font-size: 2.5rem;
    color: $neutral_black;
    margin: 0;
  }

  .form-container {
    background-color: $neutral_gray10;
    padding: 1rem;
    border-radius: 8px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    transition: 1s;
    @include box-shadow-gray50($neutral_gray50);
    position: relative; // Add this line to position the button correctly

    &:hover {
      // box-shadow: 3px 6px 10px $neutral_gray50;
      box-shadow: none;
    }

    h2 {
      grid-column: 1 / -1;
      font-size: 1.5rem;
      color: $neutral_white;
      background-color: $primary_color100;
      border-radius: 8px;
      padding: 0.5rem;
    }

    .input-box {
      @include input-box;

      .input[required] {
        @include form-field($focus-color: $error_red50);
      }
      .input[disabled] {
        @include form-field($focus-color: $third_color100);
        cursor: not-allowed;
      }
      .input {
        @include form-field;
      }
      
      .textarea {
        @include form-field($min-height: 120px);
        resize: vertical;
      }

      .date {
        @include form-field;
        cursor: pointer;
      }
    }
  }

  // Images upload section
.files-container {
  grid-column: 1 / -1;
  background-color: $neutral_gray10;
  padding: 1.5rem;
  border-radius: 8px;
  transition: 1s;
  @include box-shadow-gray50($neutral_gray50);

  &:hover {
    // box-shadow: 3px 6px 10px $neutral_gray50;
    box-shadow: none;
  }


  h2 {
    grid-column: 1 / -1;
    font-size: 1.5rem;
    color: $neutral_white;
    background-color: $primary_color100;
    border-radius: 8px;
    padding: 0.5rem;
  }

  input[type="file"] {
    padding: 0.75rem 1rem;
    background-color: $neutral_white;
    border: 2px dashed $secondary_color50;
    border-radius: 8px;
    cursor: pointer;
    transition: border-color 0.3s;
    margin:1rem 0rem;
    width: 100%;

    &:hover:not(:disabled) {
      border-color: $secondary_color100;
    }

    &:disabled {
      cursor: not-allowed;
      background-color: $neutral_gray20;
    }
  }
}

.selected-images {
  h3 {
    font-size: 1rem;
    color: $secondary_color50;
    margin-bottom: 1rem;
  }

  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.images-list {
  background-color: $neutral_white;
  border: 1px solid $neutral_gray30;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  position: relative;
  transition: transform 0.3s ease;

  &:hover {
    transform: scale(1.02);
  }

  .property-image {
    width: 100%;
    height: 180px;
    object-fit: cover;
    display: block;
    border-bottom: 1px solid $neutral_gray30;
  }

  .remove-file {
    position: absolute;
    top: 8px;
    right: 8px;
    background-color: $error_red50;
    color: $neutral_white;
    border: none;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.2s;

    &:hover {
      background-color: $error_red100;
    }
  }
}

.form-actions {
  display: flex;
  justify-content: center;
  margin-top: 2rem;

  .submit-button {
    background-color: $primary_color100;
    color: $neutral_white;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    border: none;
    border-radius: 8px;
    transition: background-color 0.3s ease;
  }
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

#error {
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

.btn-asignar-ubicacion {
  margin-top: 0.5rem;
  background-color: $third_color100;
  color: $neutral_white;
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background-color: $third_color;
  }

  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
}

.ubicacion-asignada {
  margin-top: 0.5rem;
  .info-text {
    font-size: 0.9rem;
    color: $confirm_green50;
  }
}

.location-info {
  grid-column: 1 / -1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.location-description {
  color: $neutral_black;
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0.5rem 0;
  padding: 0.75rem;
  background-color: rgba($third_color50, 0.1);
  border-left: 3px solid $third_color100;
  border-radius: 0 4px 4px 0;
}

.location-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.location-column {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.geolocation-section {
  margin-top: 1rem;
  padding: 1.25rem;
  background-color: rgba($neutral_gray20, 0.3);
  border-radius: 8px;
  border: 1px dashed $neutral_gray30;
}

.geolocation-label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: $neutral_black;
}

.geolocation-help {
  font-size: 0.85rem;
  color: $neutral_gray70;
  margin-bottom: 1rem;
}

.geolocation-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-asignar-ubicacion {
  background-color: $third_color100;
  color: $neutral_white;
  border: none;
  border-radius: 6px;
  padding: 0.65rem 1.25rem;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
  
  &:hover {
    background-color: darken($third_color100, 10%);
  }
  
  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
    background-color: $neutral_gray40;
  }
}

.geolocation-feedback {
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
  
  &.success {
    background-color: rgba($confirm_green50, 0.2);
    color: darken($confirm_green50, 20%);
  }
  
  &.error {
    background-color: rgba($error_red50, 0.2);
    color: darken($error_red50, 20%);
  }
}
.coordinates-display {
  margin-top: 1rem;
  display: flex;
  gap: 1.5rem;
  font-size: 0.85rem;
  color: $neutral_gray70;
  padding: 0.5rem;
  background-color: rgba($neutral_gray20, 0.2);
  border-radius: 4px;
  
  span {
    font-family: monospace;
  }
}

</style>