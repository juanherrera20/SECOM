<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import api from "../services/API"; // Asegúrate de que la ruta sea correcta

const router = useRouter();

const handleGoogleCallback = async () => {
    
  try {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get("code");
    console.log("Código de autenticación de Google:", code);
    if (!code) {
      throw new Error("No se recibió código de autenticación de Google");
    }

    const response = await api.post("/auth/google/callback/", { code });

    window.location.href = "/";
  } catch (error) {
    console.error("Error en la autenticación con Google:", error);
  }
};
    

onMounted(() => {
    handleGoogleCallback();
});
</script>

<template>
    <div>Procesando autenticación con Google...</div>
</template>
