import api from './API';

const base_url = 'ubicacion/';

const UbicacionService = {
    // ==================== CITIES ====================
    async getCities() {
        try {
            const response = await api.get(base_url + "cities/");
            return response.data;
        } catch (error) {
            console.error('Error al obtener las ciudades:', error.response?.data || error.message);
            throw new Error('Error al obtener las ciudades');
        }
    },
}

export default UbicacionService;