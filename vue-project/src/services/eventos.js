// src/services/eventos.js
import api from './API';

const base_url = 'eventos/';
const donaciones_url = 'donaciones/';
const imagenes_url = 'imagenes/';

// Obtener la lista de eventos
export const getEventos = async () => {
    try {
        const response = await api.get(base_url + "eventos/");
        return response.data;
    } catch (error) {
        console.error('Error al obtener los eventos:', error.response?.data || error.message);
        throw new Error('Error al obtener los eventos');
    }
};

// Obtener un evento por ID
export const getEventoById = async (id) => {
    try {
        const response = await api.get(`${base_url}eventos/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener el evento:', error.response?.data || error.message);
        throw new Error('Error al obtener el evento');
    }
};

// Crear un nuevo evento
export const createEvento = async (eventoData) => {
    try {
        const response = await api.post(base_url + "eventos/", eventoData);
        return response.data;
    } catch (error) {
        console.error('Error al crear el evento:', error.response?.data || error.message);
        throw new Error('Error al crear el evento');
    }
};

// Actualizar un evento existente
export const updateEvento = async (id, eventoData) => {
    try {
        const response = await api.put(`${base_url}eventos/${id}/`, eventoData);
        return response.data;
    } catch (error) {
        console.error('Error al actualizar el evento:', error.response?.data || error.message);
        throw new Error('Error al actualizar el evento');
    }
};

// Eliminar un evento
export const deleteEvento = async (id) => {
    try {
        const response = await api.delete(`${base_url}eventos/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Error al eliminar el evento:', error.response?.data || error.message);
        throw new Error('Error al eliminar el evento');
    }
};

// Obtener la lista de donaciones
export const getDonaciones = async () => {
    try {
        const response = await api.get(base_url + donaciones_url);
        return response.data;
    } catch (error) {
        console.error('Error al obtener las donaciones:', error.response?.data || error.message);
        throw new Error('Error al obtener las donaciones');
    }
};

// Obtener imágenes de un evento
export const getImagenesByEventoId = async (eventoId) => {
    try {
        const response = await api.get(`${base_url}${imagenes_url}${eventoId}/`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener las imágenes:', error.response?.data || error.message);
        throw new Error('Error al obtener las imágenes');
    }
};

// Agregar o eliminar imágenes de un evento
export const manageImagenes = async (eventoId, newImages, deletedImages) => {
    try {
        const formData = new FormData();
        newImages.forEach((image) => formData.append('new_images', image));
        deletedImages.forEach((imageId) => formData.append('deleted_images', imageId));

        const response = await api.post(`${base_url}${imagenes_url}${eventoId}/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error al gestionar las imágenes:', error.response?.data || error.message);
        throw new Error('Error al gestionar las imágenes');
    }
};

export default {
    getEventos,
    getEventoById,
    createEvento,
    updateEvento,
    deleteEvento,
    getDonaciones,
    getImagenesByEventoId,
    manageImagenes,
};