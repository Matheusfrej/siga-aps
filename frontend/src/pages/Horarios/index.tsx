import { Header } from '../../components/Header'
import { Horario } from '../../components/Horario'
import styles from './styles.module.css'

export function Horarios() {
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
