import { CalendarBlank, ClipboardText } from '@phosphor-icons/react'
import styles from './styles.module.css'
import { Header } from '../../components/Header'
import { NavLink, useNavigate } from 'react-router-dom'
import { useContext, useEffect } from 'react'
import { SigabContext } from '../../contexts/sigabContext'

export function Home() {
  const { isLogged, userInfo } = useContext(SigabContext)
  const navigate = useNavigate()

  useEffect(() => {
    const logged = isLogged()

    if (!logged) {
      navigate('/login')
    }
  }, [])

  return (
    <>
      <Header />
      <div className={styles.homeContainer}>
        <div className={styles.homeContent}>
          <h1>Olá, {userInfo.nome}</h1>
          <div className={styles.links}>
            <NavLink to={'/horarios'} className={styles.linkContainer}>
              <strong>Ver meus horários</strong>
              <CalendarBlank size={32} weight="bold" />
            </NavLink>
            {userInfo.discriminator === 'conta_aluno' && (
              <a href="" className={styles.linkContainer}>
                <strong>Realizar Matrícula</strong>
                <ClipboardText size={32} weight="bold" />
              </a>
            )}
            {userInfo.discriminator === 'conta_professor' && (
              <NavLink
                to={'/visualizar-minhas-cadeiras'}
                className={styles.linkContainer}
              >
                <strong>Ver minhas cadeiras</strong>
                <ClipboardText size={32} weight="bold" />
              </NavLink>
            )}
          </div>
        </div>
      </div>
    </>
  )
}
