<script setup>

</script>


<template>

    <div class="container">
        <div class="contenedorDeSubirFotos">
            <div class="subirFotos">
                <a href="#">
                <span id="iconoSubirFotos" class="material-symbols-outlined">
                photo_library
                </span>
                </a>
            </div>
            <div class="contenedorDeSubirFotos2">
                <div class="subirFotos2">
                    <a href="#">
                    <span id="iconoSubirFotos2" class="material-symbols-outlined">
                    photo_library
                    </span>
                    </a>
                </div>
                <div class="subirFotos2">
                    <a href="#">
                    <span id="iconoSubirFotos2" class="material-symbols-outlined">
                    photo_library
                    </span>
                    </a>
                </div>
                <div class="subirFotos2">
                    <a href="#">
                    <span id="iconoSubirFotos2" class="material-symbols-outlined">
                    photo_library
                    </span>
                    </a>
                </div>
                <div class="subirFotos2">
                    <a href="#">
                    <span id="iconoSubirFotos2" class="material-symbols-outlined">
                    photo_library
                    </span>
                    </a>
                </div>
            </div>
        </div>
    </div>

</template>


<style scoped>


.tituloDeInput {
    margin-bottom: 2px;
}

.contenedorDeSubirFotos {
    display: block;
    justify-content: center;
}

.contenedorDeSubirFotos2 {
    display: flex;
    justify-content: space-between;
    margin: 0;
    padding-top: 5px;
}

.subirFotos {
    border-style: solid;
    border-width: 1px;
    border-color: gray;
    display: flex;
    justify-content: center;
    padding: 30px 120px;
}

#iconoSubirFotos {
    color: #898384;
    font-size: 60px;
}

#iconoSubirFotos:hover {
    color: #5a5a5a;
}

.subirFotos2 {
    border-style: solid;
    border-width: 1px;
    border-color: gray;
    justify-content: center;
    padding: 0px 10px;
}

#iconoSubirFotos2 {
  color: #898384;
  font-size: 50px;
}
#iconoSubirFotos2:hover {
  color: #5a5a5a;
}

.container {
    display: flex;
    align-items: center;
    flex-direction: column;
}

</style>