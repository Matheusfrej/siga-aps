import { CalendarBlank, ClipboardText } from '@phosphor-icons/react'
import styles from './styles.module.css'
import { Header } from '../../components/Header'
import { NavLink } from 'react-router-dom'

export function Home() {
  return (
    <>
      <Header />
      <div className={styles.homeContainer}>
        <div className={styles.homeContent}>
          <h1>Olá, Fulano</h1>
          <div className={styles.links}>
            <NavLink to={'/horarios'} className={styles.linkContainer}>
              <strong>Ver meus horários</strong>
              <CalendarBlank size={32} weight="bold" />
            </NavLink>
            <a href="" className={styles.linkContainer}>
              <strong>Realizar Matrícula</strong>
              <ClipboardText size={32} weight="bold" />
            </a>
          </div>
        </div>
      </div>
    </>
  )
}
