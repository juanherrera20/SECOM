<script setup>

</script>


<template>
<div class="pagina">
    <div class="eventos">
        <button class="boton eventos-right"><span class="material-symbols-outlined">arrow_left</span></button>
        <p>Participa en eventos de donación en tu zona y apoya a los que lo necesitan</p>
        <button class="boton eventos-left"><span class="material-symbols-outlined">arrow_right</span></button>
        <button class="destructive">Ver mas...</button>
    </div>
    <div class="tendencias">
        <h2>TENDENCIAS</h2>
        <div class="anuncio1"></div>
        <div class="anuncio2"></div>
        <div class="anuncio3"></div>
    </div>
    <div class="novedades">
        <h2>NOVEDADES</h2>
        <button class="boton novedades-left"><span class="material-symbols-outlined">arrow_left</span></button>
        <div class="producto">
            <div class="imagen n1"></div>
            <div class="precios">
                <span class="material-symbols-outlined">favorite</span>
                <span class="descuento" hidden>$500.000</span>
                <span>$730.000</span>
            </div>
            <p class="descripcion">Televisor Smart 75 Neo Qled 4k Qn85d</p>
            <div class="etiquetas">
                <p>TVs</p>
            </div>
            <div class="stars">
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
            </div>
        </div>
        <div class="producto">
            <div class="imagen n2"><p>Oferta 50%</p></div>
            <div class="precios">
                <span class="material-symbols-outlined">favorite</span>
                <span class="descuento">$250.000</span>
                <span>$125.000</span>
            </div>
            <p class="descripcion">iMac Retina 4k , Pantalla 21.5 Año 2019 Excelente Estado</p>
            <div class="etiquetas">
                <p class="pc">Computadora</p>
            </div>
            <div class="stars">
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
            </div>
        </div>
        <div class="producto">
            <div class="imagen n3"></div>
            <div class="precios">
                <span class="material-symbols-outlined">favorite</span>
                <span class="descuento" hidden>$250.000</span>
                <span>$690.000</span>
            </div>
            <p class="descripcion">Sony Playstation 4 - 500gb +7 Juegos Digitales+precio:630000</p>
            <div class="etiquetas">
                <p class="pc">Juegos</p>
            </div>
            <div class="stars">
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
            </div>
        </div>
        <div class="producto">
            <div class="imagen n4"></div>
            <div class="precios">
                <span class="material-symbols-outlined">favorite</span>
                <span class="descuento" hidden>$250.000</span>
                <span>$30.000</span>
            </div>
            <p class="descripcion">PANTALON STYLE TALLA 8</p>
            <div class="etiquetas">
                <p class="pc">Pantalones</p>
            </div>
            <div class="stars">
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
                <span class="material-symbols-outlined">star</span>
            </div>
        </div>
        <button class="boton novedades-right"><span class="material-symbols-outlined">arrow_right</span></button>
    </div>
    <div class="vender">
        <button class="destructive">Empezar a Vender..</button>
    </div>
    <div class="unete">
        <button class="destructive">Registrate</button>
    </div>
</div>
</template>


<style scoped>
.pagina {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 80% 1fr;
    grid-template-rows: repeat(5,400px);
    row-gap: 4rem;
}

.eventos {
    display: grid;
    grid-template-columns: 10% 80% 10%;
    grid-template-rows: 60% 40%;
    background-image: linear-gradient(to left, #15323F 37%, rgba(255, 126, 95, 0) 72%), url(../assets/Images/eventos.jpg);
    background-size: 100% 500px;
    grid-column: 2 / 3;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.eventos p {
    width: 380px;
    color: whitesmoke;
    font-size: 28px;
    grid-area: 2 / 2 / 3 / 3;
    justify-self: end;
    margin: 0;
}

/*Botones para cambiar de información*/
.boton {
    background-color: transparent;
    border: 1px solid black;
    border-radius: 100%;
    width: 30px;
    height: 30px;
    justify-self: center;
}

.eventos-right{
    grid-area: 1 / 1 / 2/ 2;
    align-self: end;
}

.eventos-left{
    grid-area: 1 / 3 / 2/ 4;
    align-self: end;
}

.destructive{
    grid-area: 2 / 3 / 3 / 4;
    align-self: center;
    width: 99px;
    height: 25px;
    background-color: #2DD7B5;
    font-family: 'Aldrich', sans-serif;
    color: whitesmoke;
    border-radius: 10px;
    padding: 0;
    border: 0;

}

.destructive:hover {
    background-color: #1C957C;
}

.boton:hover{
    background-color: rgba(255, 255, 255, 0.35);
}

/*Aquí empieza la parte de tendecias*/
.tendencias {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 10% 90%;
    gap: 10px;
    grid-column: 2 / 3;
}

.tendencias h2 {
    border-bottom: 2px solid gray;
    padding: 5px;
    grid-area: 1 / 1 / 2 / 4;
}

.anuncio1{
    background-image: url(../assets/Images/ofertas.png);
    background-size: cover;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.anuncio2{
    background-image: url(../assets/Images/cuida-planeta.jpg);
    background-size: cover;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.anuncio3{
    background-image: url(../assets/Images/intercambios-locos.jpg);
    background-size: cover;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

/*Aquí empieza la parte de novedades*/
.novedades {
    display: grid;
    grid-template-columns: 4% repeat(4, 1fr) 4%;
    grid-template-rows: 10% 90%;
    gap: 10px;
    grid-column: 2 / 3;
}

.novedades h2 {
    border-bottom: 2px solid gray;
    padding: 5px;
    grid-area: 1 / 1 / 2 / 7;
}

.novedades-left {
    order: -1;
    align-self: center;
}

.novedades-right {
    order: 1;
    align-self: center;
}

.producto {
    display: grid;
    background-color: #F3F2F2;
    grid-template-rows: 55% 1fr 2fr 1fr 1fr;
    border-radius: 3px;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);
}

.imagen {
    background-size: cover; /* Hace que la imagen cubra todo el contenedor */
    background-position: center; /* Centra la imagen en el contenedor */
    background-repeat: no-repeat; /* Evita que la imagen se repita */
    border-radius: 3px;
}

.imagen p {
    background-color: yellow;
    display: inline-block; 
}

.n1 {
    background-image: url(../assets/Images/televisor.webp);
}
.n2 {
    background-image: url(../assets/Images/applePC.webp);
}
.n3 {
    background-image: url(../assets/Images/playstation.webp);
}
.n4 {
    background-image: url(../assets/Images/pantalon.webp);
}

.precios {
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #0B3C32;
    padding: 5px;
}

.descripcion {
    padding: 5px;
}

.descuento {
    color: gray;
    text-decoration: line-through;
}

.etiquetas {
    display: flex;
    align-items: center;
    justify-content: start;
    padding: 5px;
}
.etiquetas p {
    background-color: rgb(170, 53, 156);
    display: inline-block; 
    border-radius: 6px;
}

.pc {
    background-color: #8E7C3C;
}

.stars {
    padding: 5px;
}

.stars span{
    color: #779553;
}

/*Aquí empieza la parte de Vender*/
.vender {
    display: flex;
    justify-content: end;
    background-image: url(../assets/Images/Vender-nosotros.png);
    background-size: 100% 100%; /* Ajusta la imagen para que encaje completamente dentro del contenedor */
    background-repeat: no-repeat;
    padding: 30px;
    grid-column: 2 / 3;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.vender button{
    width: 150px;
    align-self: flex-end;
}

/*Aquí empieza la parte de Unete*/
.unete {
    background-image: url(../assets/Images/Unete-nosotros.png);
    display: flex;
    justify-content: end;
    background-size: 100% 100%; /* Ajusta la imagen para que encaje completamente dentro del contenedor */
    background-repeat: no-repeat;
    padding: 30px;
    grid-column: 2 / 3;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); /*Esta es la sombra a aplicar en todos los elementos*/
}

.unete button {
    align-self: flex-end;
}

</style>