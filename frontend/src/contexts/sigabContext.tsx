import { ReactNode, createContext, useState } from 'react'
import { loginRequest } from '../services/loginService'
import { invokeToast } from '../services/toastService'

interface SigabContextProviderProps {
  children: ReactNode
}

interface UserInfo {
  email: string
  cpf: string
  nome: string
  ano_entrada: string
  discriminator: 'conta_aluno' | 'conta_professor'
}

interface SigabContextType {
  userInfo: UserInfo
  isLogged: () => boolean
  login: (email: string, password: string) => Promise<boolean>
  showToast: (message: string, didSuccess: boolean) => void
}

export const SigabContext = createContext({} as SigabContextType)

export function SigabContextProvider({ children }: SigabContextProviderProps) {
  const [userInfo, setUserInfo] = useState({} as UserInfo)

  const login = async (email: string, senha: string) => {
    const response = await loginRequest(email, senha)
    const token = response.idToken
    const expireDate = response.expiresIn
    // console.log(expireDate)
    const dataAtual = new Date()
    const milissegundosAtuais = dataAtual.getTime()
    const milissegundosMaisUmaHora = milissegundosAtuais + 10 * 1000
    const novaData = new Date(milissegundosMaisUmaHora)

    // console.log(novaData)
    setUserInfo(response.user)
    if (token === -1) {
      return false
    }
    localStorage.setItem('token', token.toString())
    localStorage.setItem('userInfo', JSON.stringify(response.user))
    localStorage.setItem('tokenExpireDate', JSON.stringify(novaData))
    return true
  }

  const didTokenExpire = () => {
    if (localStorage.getItem('tokenExpireDate') !== null) {
      const dataAtual = new Date().getTime()
      let dataExpira = localStorage.getItem('tokenExpireDate')
      // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
      dataExpira = JSON.parse(dataExpira!)
      // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
      const dataExpiraDate = new Date(dataExpira!).getTime()
      if (dataAtual > dataExpiraDate) {
        return true
      }
      return false
    }
    return true
  }

  const isLogged = () => {
    if (localStorage.getItem('token') !== null) {
      const tokenExpire = didTokenExpire()
      if (tokenExpire) {
        localStorage.clear()
        return false
      }
      const user = localStorage.getItem('userInfo')
      if (user !== null) {
        setUserInfo(JSON.parse(user))
      }
      return true
    }
    return false
  }

  const showToast = (message: string, didSuccess: boolean) => {
    invokeToast(message, didSuccess)
  }

  return (
    <SigabContext.Provider
      value={{
        userInfo,
        isLogged,
        login,
        showToast,
      }}
    >
      {children}
    </SigabContext.Provider>
  )
}
