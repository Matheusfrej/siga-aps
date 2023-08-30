import api from '../libs/api'
import HorarioInterface from '../components/HorarioCadeira'
const token = localStorage.getItem('token')

interface Cadeira {
  nome: string
  cento_universitario: string
  horarios: typeof HorarioInterface
}

export const cadastrarCadeiraRequest = async (
  nome: string,
  centro_universitario: string,
  formattedHorarios: object,
) => {
  try {
    const userInfoResponse = await api.get('/get-user-info', {
      headers: {
        'Content-Type': 'application/json',
        token,
      },
    })

    const userInfo = userInfoResponse.data

    const data = {
      nome,
      horario: formattedHorarios,
      centro_universitario,
      professor: userInfo,
    }

    const response = await api.post('/cadastrar-cadeira', data, {
      headers: {
        'Content-Type': 'application/json',
        token,
      },
    })

    return response.data
  } catch (error) {
    return -1
  }
}

export const getCadeiras = async (token: string) => {
  const response = await api.get('/cadeira/get-cadeiras-professor', {
    headers: {
      'Content-Type': 'application/json',
      token,
    },
  })
  const formattedCadeiras = response.data.map((cadeira: Cadeira) => ({
    ...cadeira,
  }))
  return formattedCadeiras
}

export const getOfertasCadeiraPeriodo = async () => {
  try {
    const response = await api.get('/cadeira/get-cadeiras-periodo', {
      headers: {
        'Content-Type': 'application/json',
        token,
      },
    })
    return response.data
  } catch (error) {
    console.log(error)
  }
}

export const deletarCadeiraRequest = async (
  cadeiraId: number,
  token: string,
) => {
  const headers = {
    'Content-Type': 'application/json',
    token,
  }

  const data = { id: cadeiraId }
  const response = await api.delete('/cadeira/deletar-oferta-cadeira', {
    headers,
    data,
  })
  return response.data
}
