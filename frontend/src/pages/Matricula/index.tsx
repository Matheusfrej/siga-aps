import { Header } from '../../components/Header'
import styles from './styles.module.css'

export function Matricula() {
  return (
    <>
      <Header />
      <div className={styles.matriculaContainer}>
        <div className={styles.matriculaContent}>
          <h1>Matricula</h1>
        </div>
      </div>
    </>
  )
}
