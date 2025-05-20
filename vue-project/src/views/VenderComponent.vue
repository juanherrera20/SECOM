<script setup>
import AddImgsComponent from '@/components/AddImgsComponent.vue'
import ButtonDefault from '@/components/ButtonDefault.vue';
import FooterComponent from '@/components/FooterComponent.vue';

// Codigo de ejemplo para hacer vista de ver Evento
import SelectInput from '@/components/SelectInput.vue';
import EventosService from '../services/eventos';
import { ref, onMounted } from 'vue';

const donations = ref([]);

const formData = ref({
        id: null,
        name: "",
        meet_date: "",
        type_donation: "",
        donation_id: null,
        image: ""
})

onMounted(async () => {
    try {
      const [donationsResponse, eventoResponse] = await Promise.all([
        EventosService.getDonations(),
        EventosService.getEventoById(1)
      ]);
      
      donations.value = donationsResponse;
      formData.value = eventoResponse;
      
      const donation = donations.value.find(obj => obj.name === formData.value.type_donation)
      formData.value.donation_id = donation.id

      console.log('Donations:', donations.value);
      console.log('Evento info', formData.value);
      console.log('Texto de la donación obtenido', formData.value.donation_id)

    } catch (error) {
      console.error('Error cargando datos iniciales:', error);
    }
  });
// Aquí termina el Evento
</script>


<template>
    <div>

    <div class="container">
        <label> {{ formData.type_donation }}</label>
        <label>Donación permitida por el evento {{ formData.donation_id }}</label>
                <SelectInput
                    v-model="formData.donation_id"
                    :options="donations"
                    label="Tipo de Donaciones"
                    extra="Seleccionar el tipo de donacion permitida"
                    :isRequired="false"
                    :isDesabled="false">
              </SelectInput>
        <div class="img">
            <img src="../assets/Images/publica archivo.png" alt="Publicar" id="imgVender">
        </div>

        <div class="tipoProducto">
            <div class="descripciones">
                <div class="sostenibles">
                    <h2 class="white">SOSTENIBLES</h2>
                    <p class="white">Son aquellos que se han producido, 
                    <br>
                    utilizado o diseñado de una manera que 
                    <br>
                    minimiza el impacto negativo en el 
                    <br>
                    medio ambiente y promueve un uso 
                    <br>
                    responsable de los recursos.</p>
                </div>
                <div class="normales">
                    <h2>NORMALES</h2>
                    <p>Son todos los demás productos que 
                        <br>
                        puedes vender en nuestra plataforma.</p>
                </div>
           </div>
        </div>

        <div class="elegirTipo">
            <div class="btns">
                <button class="btn" id="moverALeft">SOSTENIBLES</button>
                <button class="btn">NORMALES</button>
           </div>
        </div>

        <div class="contenedorTitulo">
            <p class="nombreContenedor">INFORMACIÓN DEL PRODUCTO</p>
        </div>

        <div class="fondo">
            <div class="top">
                <div class="Inputs">
                    <div class="inputInterior">
                        <p><strong>Nombre del producto</strong></p>
                        <input type="text" placeholder="Escriba el nombre aquí"/>
                        <div class="mensajeRequerido">
                          <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                          <p class="requerido"><strong>Campo requerido</strong></p>
                        </div>
                    </div>
                    <div class="inputInterior">
                        <p><strong>Descripción</strong></p>
                        <input type="text" placeholder="Describa el producto"/>
                    </div>
                </div>

                <div class="addImgs">
                    <div class="addIMGS">
                        <div>
                            <p class="tituloDeInput"><strong>Añada imágenes de producto</strong></p>
                        </div>
                        <AddImgsComponent />
                    </div>
                </div>
            </div>
            
            <div class="block">
                <div class="cant">
                    <p><strong>Cantidad</strong></p>
                    <input type="number" id="inputCantidad">
                    <div class="mensajeRequerido">
                      <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                      <p class="requerido"><strong>Campo requerido</strong></p>
                    </div>
                </div>
            </div>
            
        </div>

        <div class="contenedorTitulo">
            <p class="nombreContenedor">DIRECCIÓN DEL PRODUCTO</p>
        </div>

        <div class="fondo">
            <div class="mensajeDeAyuda">
                <div>
                  <span class="material-symbols-outlined" id="help">help</span>
                </div>
                <div>
                  <p class="mensajeHelp">Registra la Ubicación donde se publicará el producto, de esta manera los usuarios podrán verla si estan cerca. Puedes usar la dirección asociada a tu cuenta o agregar una para el producto.</p>
                </div>
            </div>

            <div class="Inputs ubica">
                <div class="inputInterior">
                    <p><strong>País</strong></p>
                    <input type="text" placeholder="País de ubicación"/>
                    <div class="mensajeRequerido">
                      <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                      <p class="requerido"><strong>Campo requerido</strong></p>
                    </div>
                </div>
                <div class="inputInterior">
                    <p><strong>Ciudad</strong></p>
                    <input type="text" placeholder="Ciudad de ubicación"/>
                    <div class="mensajeRequerido">
                      <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                      <p class="requerido"><strong>Campo requerido</strong></p>
                    </div>
                </div>
                <div class="inputInterior containerBtnDefault">
                    <ButtonDefault size="default" color="azul" text="Usar mi ubicación" icono="location_on" class="insertarUbic" />
                </div>
            </div>

        </div>

        <div class="contenedorTitulo">
            <p class="nombreContenedor">CATEGORÍAS DEL PRODUCTO</p>
        </div>

        <div class="fondo">
            <div class="mensajeDeAyuda">
                <div>
                  <span class="material-symbols-outlined" id="help">help</span>
                </div>
                <div>
                  <p class="mensajeHelp">Categorizar correctamente tu producto ayudará a que los clientes lo puedan encontrar más fácil.</p>
                </div>
            </div>

            <div>
                <div class="containerCategYSubcateg">
                    <div class="inputInterior forCateg">
                        <p><strong>Categoría</strong></p>
                        <select name="categoriasAceptadas" class="categoriasAceptadas">
                            <option value="opciion1">Transporte</option>
                            <option value="opciion2">Tecnología</option>
                            <option value="opciion3">Hogar y muebles</option>
                            <option value="opciion4">Electrodomésticos</option>
                            <option value="opciion5">Ropa</option>
                            <option value="opciion6">Accesorios y moda</option>
                            <option value="opciion7">Deportes y fitness</option>
                            <option value="opciion8">Cuidado personal</option>
                            <option value="opciion9">Herramientas</option>
                            <option value="opciion10">Juegos y juguetes</option>
                            <option value="opciion11">Manualidades</option>
                            <option value="opciion12">Salud</option>
                        </select>
                        <div class="mensajeRequerido">
                          <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                          <p class="requerido"><strong>Campo requerido</strong></p>
                        </div>
                    </div>
                    
                    <div class="inputInterior forCateg">
                        <p><strong>Subategoría</strong></p>
                        <select name="subcategoriasAceptadas" class="categoriasAceptadas">
                            <option value="opciion1">Subcategoría 1</option>
                            <option value="opciion2">Subcategoría 2...</option>
                        </select>
                        <div class="mensajeRequerido">
                          <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                          <p class="requerido"><strong>Campo requerido</strong></p>
                        </div>
                    </div>
                </div>

                <div class="containerCategYSubcateg">
                    <div class="inputInterior forCateg">
                        <p><strong>Marcas populares</strong></p>
                        <select name="categoriasAceptadas" class="categoriasAceptadas">
                            <option value="opciion1">Opción 1</option>
                            <option value="opciion2">Opción 2...</option>
                        </select>
                    </div>
                    
                    <div class="inputInterior forCateg">
                        <p><strong>Estado del producto</strong></p>
                        <select name="categoriasAceptadas" class="categoriasAceptadas">
                            <option value="opciion1">Sin usar</option>
                            <option value="opciion2">Pocos usos</option>
                            <option value="opciion3">Muchos usos</option>
                            <option value="opciion4">Tercera mano</option>
                            <option value="opciion5">Otro</option>
                        </select>
                        <div class="mensajeRequerido">
                          <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                          <p class="requerido"><strong>Campo requerido</strong></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="contenedorTitulo">
            <p class="nombreContenedor">PRECIOS Y PROMOCIONES</p>
        </div>

        <div class="fondo">
            <div class="Inputs ubica">
                <div class="inputInterior">
                    <p><strong>Precio</strong></p>
                    <input type="text" placeholder="Precio del producto"/>
                    <div class="mensajeRequerido">
                      <span class="material-symbols-outlined puntoRojo">radio_button_unchecked</span>
                      <p class="requerido"><strong>Campo requerido</strong></p>
                    </div>
                </div>
                <div class="inputInterior">
                    <p><strong>Ofertas</strong></p>
                    <select name="categoriasAceptadas" class="categoriasAceptadas">
                            <option value="opciion1">Ninguna</option>
                            <option value="opciion2">10%</option>
                            <option value="opciion3">20%</option>
                            <option value="opciion4">30%</option>
                            <option value="opciion5">40%</option>
                            <option value="opciion6">50%</option>
                            <option value="opciion7">60%</option>
                            <option value="opciion8">70%</option>
                        </select>
                </div>
            </div>
        </div>

        <div class="containerBtnPublicar">
            <ButtonDefault size="default" color="azul" text="Publicar" class="publicarP" />
        </div>

    </div>

    <FooterComponent />

</div>

</template>


<style scoped>

.container {
    display: flex;
    justify-content: center;
    width: 90%;
    margin: 0 auto;
    flex-direction: column;
    margin-top: 20px;
}

#imgVender {
    height: 240px;
    width: 967px;
}

.img {
    display: flex;
    justify-content: center;
}

.sostenibles {
    background: #0B3C32;
}

.normales {
    background: #a59a57;
}

.sostenibles, .normales {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
    padding: 25px;
    border-radius: 1px;
}

h2 {
    margin-block: 5px;
}

.white {
    color: white;
}

p {
    font-size: 14px;
}

.tipoProducto {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

.descripciones {
    display: flex;
}

.elegirTipo {
    display: flex;
    justify-content: center;
}

.btns {
    background: rgb(236, 236, 236);
    padding: 3px 2px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: solid 1px rgb(197, 197, 197);
}

.btn {
    padding: 1px 2px;
    border: none;
    border-radius: 7px;
    background: rgb(236, 236, 236);
    font-family: 'Aldrich', sans-serif;
}


#moverALeft {
    margin-right: 5px;
}

.btn:hover {
    background: #15323f;
    color: white;
}

.btn:focus {
    background: #15323f;
    color: white;
}

.contenedorTitulo {
    background-color: #0F4F42;
    padding: 10px 0px;
    width: 78.5%;
    display: flex;
    justify-content: center;
    margin: 0 auto;
    margin-top: 20px;
}

.nombreContenedor {
    color: white;
    font-size: 35px;
}

.fondo {
    display: flex;
    background-color: rgb(245, 245, 245);
    border: solid 1px rgb(197, 197, 197);
    width: 78.5%;
    margin: 0 auto;
    flex-direction: column;
}

.Inputs {
    display: flex;
    flex-direction: column;
}

.ubica {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.inputInterior {
    margin: 18px 15px;
}

.forCateg {
    padding: 0px 100px;
}

input, .categoriasAceptadas {
    padding: 5px 80px;
    padding-left: 2px;
}

.mensajeRequerido {
    display: flex;
    justify-items: left;
    margin-top: 3px;
}

.puntoRojo {
    background-color: rgb(177, 0, 0);
    color: rgb(177, 0, 0);
    border-radius: 9px;
    font-size: 11px;
    margin-right: 3px;
    padding: 0px 1px;
}

.requerido {
    font-size: 11px;
}

.addImgs {
    margin-right: 50px;
}

#inputCantidad {
    padding: 5px 0px;
}

.top {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.block {
    display: flex;
    margin-left: 1.6%;
    padding-block: 15px;
}

.mensajeDeAyuda {
    display: flex;
    justify-content: left;
    align-items: center;
    margin-bottom: 5px;
}

#help {
    margin-top: 5px;
    margin-right: 7px;
}

.mensajeHelp {
    font-size: 16px;
}

.insertarUbic, .publicarP {
    padding: 10px 0px;
    width: 170px;
    border-radius: 2px;
}

.containerBtnDefault {
    display: flex;
    align-items: center;
}

.containerCategYSubcateg {
    display: flex;
    justify-content: space-between;
}

.containerBtnPublicar {
    display: flex;
    justify-content: center;
    margin: 20px 0px;
}

</style>