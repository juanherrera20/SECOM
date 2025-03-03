import api from './API'; // Importa la instancia configurada

const base_url = 'usuarios/';

//Obtener el usuario actual autenticado
export const getCurrentUser = async () => {
    try {
        const response = await api.get(base_url + 'me/');
        return response.data;
    } catch (error) {
        console.error('Error al obtener el usuario actual:', error.response?.data || error.message);
        throw new Error('Error al obtener el usuario actual');
    }
}

//Exportamos `getCurrentUser` como default
export default getCurrentUser;