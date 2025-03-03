// src/services/api.js
import axios from 'axios';


/* 
Aquí definimos la configuraión global de Axios, servicio para mandar peticiones
a la API De Django Rest Framework, el uso de credenciales y el tipo de contenido 
es necesario para manejar la autenticación con JWT Token y el envío de datos en formato JSON.
*/ 

// Instancia global de axios
const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/', // URL del backend
  withCredentials: true, // Permitir envío de cookies
  headers: { 'Content-Type': 'application/json' }
});


export default api;