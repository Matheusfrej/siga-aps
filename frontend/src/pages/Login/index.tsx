import { ChangeEvent, FormEvent, useContext, useState } from 'react'
import { Logo } from '../../components/Logo'
import styles from './styles.module.css'
import { useNavigate } from 'react-router-dom'
import { SigabContext } from '../../contexts/sigabContext'

export function Login() {
  const { login, showToast } = useContext(SigabContext)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const navigate = useNavigate()

  const handleLogin = async (event: FormEvent) => {
    event.preventDefault()
    const logged = await login(email, password)
    if (logged) {
      setEmail('')
      setPassword('')
      showToast('Login realizado com sucesso!', true)
      navigate('/')
    } else {
      console.log('entrou aq')

      showToast('Email ou senha inválidos', false)
      setPassword('')
    }
  }

  const handleEmailChange = (event: ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value)
  }

  const handlePasswordChange = (event: ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value)
  }

  return (
    <div className={styles.loginContainer}>
      <div>
        <Logo />
        <h3>Login</h3>
        <form onSubmit={handleLogin}>
          <input
            type="text"
            placeholder="Email"
            value={email}
            onChange={handleEmailChange}
            required
          />
          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={handlePasswordChange}
            required
          />
          <button type="submit">Entrar</button>
        </form>
      </div>
      <span>&copy; Sigab - 2023</span>
    </div>
  )
}
