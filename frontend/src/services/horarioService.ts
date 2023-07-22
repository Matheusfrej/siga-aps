import api from '../libs/api'

export const getHorarioRequest = async (token: string) => {
  try {
    const response = await api.get('/ver-horario', {
      headers: { 
        'Content-Type': 'application/json',
        'token': token
      }
    })

    return response.data
  } catch (error) {
    return -1
  }
}
