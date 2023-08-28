import api from '../libs/api'

export const matriculaRequest = async (ofertasCadeirasIDs: number[]) => {
  const headers = {
    'Content-Type': 'application/json',
  }

  const data = {
    ofertasCadeirasIDs,
  }
  try {
    const response = await api.post('/matricula/fazer-matricula', data, {
      withCredentials: false,
      headers,
    })
    console.log(response.data)

    return response.data
  } catch (error) {
    return -1
  }
}
