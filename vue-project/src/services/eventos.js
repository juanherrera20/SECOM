// src/services/eventos.js
import api from './API';

const base_url = 'eventos/';

// Obtener la lista de eventos
export const getEventos = async () => {
    try {
        const response = await api.get(base_url);
        return response.data;
    } catch (error) {
        console.error('Error al obtener los eventos:', error.response?.data || error.message);
        throw new Error('Error al obtener los eventos');
    }
};

export default getEventos;