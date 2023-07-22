import api from '../libs/api'

export const getHorarioRequest = async (token: string) => {
  try {
    const response = await api.get('/ver-horario', {
      data: { token },
    })

    return response.data
  } catch (error) {
    return -1
  }
}
