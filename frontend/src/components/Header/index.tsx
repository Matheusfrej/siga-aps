import { ArrowLineRight } from '@phosphor-icons/react'
import { Logo } from '../Logo'
import styles from './styles.module.css'
import { useContext } from 'react'
import { SigabContext } from '../../contexts/sigabContext'
import { useNavigate } from 'react-router-dom'

export function Header() {
  const { logout } = useContext(SigabContext)

  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  const handleLogoClick = () => {
    navigate('/')
  }

  return (
    <header className={styles.headerContainer}>
      <div>
        <div onClick={handleLogoClick} className={styles.logoHeader}>
          <Logo />
        </div>
        <button onClick={handleLogout}>
          <ArrowLineRight size={20} />
          <p>Sair</p>
        </button>
      </div>
    </header>
  )
}
