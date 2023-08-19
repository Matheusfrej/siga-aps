import { useContext, useEffect } from 'react'
import { Header } from '../../components/Header'
import { Horario } from '../../components/Horario'
import styles from './styles.module.css'
import { useNavigate } from 'react-router-dom'
import { SigabContext } from '../../contexts/sigabContext'

export function Horarios() {
  const { isLogged } = useContext(SigabContext)
  const navigate = useNavigate()

  useEffect(() => {
    const logged = isLogged()

    if (!logged) {
      navigate('/login')
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <>
      <Header />
      <div className={styles.horariosContainer}>
        <div className={styles.horariosContent}>
          <h1>Horários</h1>
          <Horario />
        </div>
      </div>
    </>
  )
}
