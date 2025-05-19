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

    // Para obtener la ciudad del evento
    async getCityById(id) {
    try {
      const response = await api.get(`${base_url}cities/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener la ciudad por ID:', error.response?.data || error.message);
      throw new Error('No se pudo obtener la ciudad');
    }
  },

}

export default UbicacionService;