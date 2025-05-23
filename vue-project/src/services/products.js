import api from './API';

const base_url = 'products/';
const images_url = 'images/';
const offers_url = base_url + 'offers/';

const ProductsService = {
  // ==================== PRODUCTOS ====================

  //   async getProducts(params = {}) {
  //   try {
  //     // Construir URLSearchParams manualmente para arrays
  //     const searchParams = new URLSearchParams();

  //     Object.entries(params).forEach(([key, value]) => {
  //       if (Array.isArray(value)) {
  //         value.forEach(v => {
  //           if (v !== null && v !== undefined) {
  //             searchParams.append(key, v);
  //           }
  //         });
  //       } else if (value !== null && value !== undefined && value !== '') {
  //         searchParams.append(key, value);
  //       }
  //     });

  //     const queryString = searchParams.toString();
  //     const url = `${base_url}products/?${queryString}`;

  //     const response = await api.get(url);
  //     return response.data;
  //   } catch (error) {
  //     console.error('Error al obtener productos:', error.response?.data || error.message);
  //     throw error;
  //   }
  // },
  async getProducts(params = {}) {
    try {
      const response = await api.get(`${base_url}products/`, {
        params, // 👈 aquí van los filtros dinámicos
      });
      return response.data;
    } catch (error) {
      console.error('Error al obtener productos:', error.response?.data || error.message);
      throw error;
    }
  },

  async getProductById(id) {
    try {
      const response = await api.get(`${base_url}products/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener el producto:', error.response?.data || error.message);
      throw error;
    }
  },

  async createProduct(productoData) {
    try {
      const response = await api.post(`${base_url}products/`, productoData);
      return response.data;
    } catch (error) {
      console.error('Error al crear el producto:', error.response?.data || error.message);
      throw error;
    }
  },

  async updateProduct(id, productoData) {
    try {
      const response = await api.put(`${base_url}products/${id}/`, productoData);
      return response.data;
    } catch (error) {
      console.error('Error al actualizar el producto:', error.response?.data || error.message);
      throw error;
    }
  },

  async deleteProduct(id) {
    try {
      const response = await api.delete(`${base_url}products/${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al eliminar el producto:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== FAVORITOS ====================

  async addToWishlist(productId) {
    try {
      const response = await api.post(`${base_url}products/${productId}/add_favorites/`);
      return response.data;
    } catch (error) {
      console.error('Error al agregar a favoritos:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== OFERTAS ====================

  async getOffers({ active = null } = {}) {
    try {
      const params = active !== null ? { active } : {};
      const response = await api.get(`${offers_url}`, { params });
      return response.data;
    } catch (error) {
      console.error('Error al obtener ofertas:', error.response?.data || error.message);
      throw error;
    }
  },

  async createOffer(ofertaData) {
    try {
      const response = await api.post(`${offers_url}`, ofertaData);
      return response.data;
    } catch (error) {
      console.error('Error al crear oferta:', error.response?.data || error.message);
      throw error;
    }
  },

  async updateOffer(id, ofertaData) {
    try {
      const response = await api.put(`${offers_url}${id}/`, ofertaData);
      return response.data;
    } catch (error) {
      console.error('Error al actualizar oferta:', error.response?.data || error.message);
      throw error;
    }
  },

  async deleteOffer(id) {
    try {
      const response = await api.delete(`${offers_url}${id}/`);
      return response.data;
    } catch (error) {
      console.error('Error al eliminar oferta:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== CATEGORÍAS Y TAGS ====================

  async getCategories() {
    try {
      const response = await api.get(`${base_url}categories/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener categorías:', error.response?.data || error.message);
      throw error;
    }
  },

  async getTags(categoryId = null) {
    try {
      const params = categoryId ? { category: categoryId } : {};
      const response = await api.get(`${base_url}tags/`, { params });
      return response.data;
    } catch (error) {
      console.error('Error al obtener tags:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== LIST CHOICES ====================
  //list to States of the products
  async getStates() {
    try {
      const response = await api.get(`${base_url}states/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener estados:', error.response?.data || error.message);
      throw error;
    }
  },

  //List to conditions of the products
  async getConditions() {
    try {
      const response = await api.get(`${base_url}conditions/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener condiciones:', error.response?.data || error.message);
      throw error;
    }
  },

  // ==================== IMÁGENES ====================

  async getImagesByProductoId(productId) {
    try {
      const response = await api.get(`${base_url}${images_url}${productId}/`);
      return response.data;
    } catch (error) {
      console.error('Error al obtener imágenes del producto:', error.response?.data || error.message);
      throw error;
    }
  },

  async manageImages(productId, formData) {
    try {
      const response = await api.post(`${base_url}${images_url}${productId}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Error al subir/eliminar imágenes:', error.response?.data || error.message);
      throw error;
    }
  },
};

export default ProductsService;
