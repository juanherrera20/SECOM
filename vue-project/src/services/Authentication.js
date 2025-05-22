import api from './API'; // Importa la instancia configurada

const token_generate = 'usuarios/api/token/';

export const login = async (email, password) => {
  try {
    const response = await api.post(token_generate, { email, password });

    // Para guardar el token en localStorage
    localStorage.setItem('token', response.data.access);

    localStorage.setItem('loginSuccess', 'true')

    return response.data;
  } catch (error) {
    console.error('Error en login:', error.response?.data || error.message);
    throw new Error('Credenciales incorrectas o error en el servidor.');
  }
};

// Refrescar token (ya lo maneja `api.js`, pero lo dejamos por si acaso)
export const refreshToken = async () => {
  try {
    const response = await api.post('usuarios/api/token/refresh/');
    return response.data;
  } catch (error) {
    console.error('Error al refrescar el token:', error.response?.data || error.message);
    throw error;
  }s
};

// Cerrar sesión
export const logout = async () => {
  try {
    await api.post('usuarios/logout/');

    localStorage.setItem('loginSuccess', 'false')

    return { message: 'Sesión cerrada correctamente' };
  } catch (error) {
    console.error('Error en logout:', error.response?.data || error.message);
    throw new Error('No se pudo cerrar sesión.');
  }
};


// Registro de usuario
export const register = async (data) => {
    try {
        const response = await api.post('usuarios/register/', data);
        return response.data;
    } catch (error) {
        console.error('Error en registro:', error.response?.data || error.message);
        throw new Error('Error al registrar el usuario');
    }
}
