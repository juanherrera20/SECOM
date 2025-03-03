// src/services/municipios.js
import api from './API';

const base_url = 'ubicacion/';

// Obtener la lista de municipios
export const getMunicipios = async () => {
    try {
        const response = await api.get(base_url + "municipios/");
        return response.data;
    } catch (error) {
        console.error('Error al obtener los municipios:', error.response?.data || error.message);
        throw new Error('Error al obtener los municipios');
    }
};

export default getMunicipios;