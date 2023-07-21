import { ReactNode, createContext, useState } from 'react'
import { loginRequest } from '../services/loginService'

interface SigabContextProviderProps {
  children: ReactNode
}

interface UserInfo {
  id: number
  email: string
  cpf: string
  nome: string
  data_nascimento: Date
  ano_entrada: string
  senha: string
  discriminator: 'conta_aluno' | 'conta_professor'
}

interface SigabContextType {
  userInfo: UserInfo
  login: (email: string, password: string) => Promise<boolean>
}

export const SigabContext = createContext({} as SigabContextType)

export function SigabContextProvider({ children }: SigabContextProviderProps) {
  const [userInfo, setUserInfo] = useState({} as UserInfo)

  const login = async (email: string, senha: string) => {
    const token = await loginRequest(email, senha)
    if (token === -1) {
      return false
    }
    localStorage.setItem('token', token.toString())
    return true
  }

  return (
    <SigabContext.Provider
      value={{
        userInfo,
        login,
      }}
    >
      {children}
    </SigabContext.Provider>
  )
}
