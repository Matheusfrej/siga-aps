import api from '../libs/api'

export const loginRequest = async (email: string, senha: string) => {
  const headers = {
    'Content-Type': 'application/json',
  }

  const data = {
    email,
    senha,
  }
  try {
    const response = await api.post('/login', data, {
      withCredentials: false,
      headers,
    })
    console.log(response.data)

    return response.data
  } catch (error) {
    return -1
  }
}
