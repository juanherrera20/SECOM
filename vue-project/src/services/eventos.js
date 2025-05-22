import api from './API';

const base_url = 'eventos/';
const imagenes_url = 'images/';
const posts_url = base_url + 'posts/';

const EventosService = {
  // ==================== EVENTOS ====================

  async getEventos() {
    try {
      const response = await api.get(`${base_url}eventos/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener los eventos:', error.response?.data || error.message);
      throw error;
    }
  },

  async getEventoById(id) {
    try {
      const response = await api.get(`${base_url}eventos/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener el evento:', error.response?.data || error.message);
      throw error;
    }
  },

  async createEvento(eventoData) {
    try {
      const response = await api.post(`${base_url}eventos/`, eventoData);
      return response.data;
    } catch (error) {
      console.error('Error al crear el evento:', error.response?.data || error.message);
      throw error;
    }
  },

  async updateEvento(id, eventoData) {
    try {
      const response = await api.put(`${base_url}eventos/${id}/`, eventoData);
      return response.data;
    } catch (error) {
      console.error('Error al actualizar el evento:', error.response?.data || error.message);
      throw error;
    }
  },

  async deleteEvento(id) {
    try {
      const response = await api.delete(`${base_url}eventos/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al eliminar el evento:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== SUBSCRIPCIÓN A EVENTO ====================

  async subscribeToEvento(eventoId) {
    try {
      const response = await api.post(`${base_url}eventos/${eventoId}/subscribe/`);
      return response.data;
    } catch (error) {
      console.error('Error al suscribirse al evento:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== POSTS DE EVENTOS ====================

    async getPosts(eventoId = null) {
        try {
            const response = await api.get(posts_url, {
            params: eventoId ? { evento: eventoId } : {},
            });
            return response.data;
        } catch (error) {
            console.error('Error al obtener posts de eventos:', error.response?.data || error.message);
            throw error;
        }
    },

  async getPostById(id) {
    try {
      const response = await api.get(`${posts_url}${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener el post:', error.response?.data || error.message);
      throw error;
    }
  },

  async createPost(data) {
    try {
      const response = await api.post(posts_url, data);
      return response.data;
    } catch (error) {
      console.error('Error al crear el post:', error.response?.data || error.message);
      throw error;
    }
  },

  async updatePost(id, data) {
    try {
      const response = await api.put(`${posts_url}${id}/`, data);
      return response.data;
    } catch (error) {
      console.error('Error al actualizar el post:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== DONACIONES ====================

  async getDonations() {
    try {
      const response = await api.get(`${base_url}donations/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener las donaciones:', error.response?.data || error.message);
      throw error;
    }
  },

  async getDonationsByEventoId(eventoId) {
    try {
      const response = await api.get(`${base_url}donations/evento/${eventoId}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener la donación del evento:', error.response?.data || error.message);
      throw error;
    }
  },


  // ==================== IMÁGENES ====================
  // List Images Evento
  async getImagesByEventoId(eventoId) {
    try {
      const response = await api.get(`${base_url}${imagenes_url}${eventoId}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener las imágenes del evento:', error.response?.data || error.message);
      throw error;
    }
  },

  // Add & delete Images Evento
  async manageImages(eventoId, images) {
    try {
      const response = await api.post(`${base_url}${imagenes_url}${eventoId}/`, images, 
        {
        headers: {
          'Content-Type': 'multipart/form-data', // Sobrescribí el global solo acá
        },
      });
      return response.data;
    } catch (error) {
      console.error('Error al gestionar imágenes del evento:', error.response?.data || error.message);
      throw error;
    }
  },
};

export default EventosService;
