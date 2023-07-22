import api from '../libs/api'

export const getHorarioRequest = async (token: string) => {
  try {
    const data = { token }
    const info = JSON.stringify(data)
    const response = await api.get('/ver-horario', {
      headers: { 'Content-Type': 'application/json' },
      data: info,
    })

    return response.data
  } catch (error) {
    return -1
  }
}
