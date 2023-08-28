import api from '../libs/api'

export const matriculaRequest = async (
  ofertasCadeirasIDs: number[],
  token: string,
) => {
  const headers = {
    'Content-Type': 'application/json',
    token,
  }

  const data = {
    cadeiras: ofertasCadeirasIDs.map((ofertaCadeiraID) =>
      ofertaCadeiraID.toString(),
    ),
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
