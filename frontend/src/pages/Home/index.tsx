import { CalendarBlank } from '@phosphor-icons/react'
import styles from './styles.module.css'
import { Header } from '../../components/Header'

export function Home() {
  return (
    <>
      <Header />
      <div className={styles.homeContainer}>
        <div className={styles.homeContent}>
          <h1>Olá, Fulano</h1>
          <div className={styles.links}>
            <a href="" className={styles.linkContainer}>
              <strong>Ver meus horários</strong>
              <CalendarBlank size={32} weight="bold" />
            </a>
            <a href="" className={styles.linkContainer}>
              <strong>Realizar Matrícula</strong>
              <CalendarBlank size={32} weight="bold" />
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
