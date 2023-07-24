import { ChangeEvent, FormEvent, useState, useContext } from 'react'
import styles from './styles.module.css'
import '../../global.css'
import { SigabContext } from '../../contexts/sigabContext'
import { cadastrarCadeiraRequest } from '../../services/cadeiraService'
import { Header } from '../../components/Header'
import HorarioCadeira from '../../components/HorarioCadeira'
import { useNavigate } from 'react-router'

export function CadastrarCadeira() {
  const { showToast } = useContext(SigabContext)
  const [nome, setNome] = useState('')
  const [planoEnsino, setPlanoEnsino] = useState('')
  const [centroUniversitario, setCentroUniversitario] = useState('')
  const [formattedHorarios, setFormattedHorarios] = useState<any[]>([])
  const navigate = useNavigate()

  const handleSaveHorarios = (formattedHorarios: any) => {
    setFormattedHorarios(formattedHorarios)
  }

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault()
    const formData = {
      nome,
      plano_ensino: planoEnsino,
      centro_universitario: centroUniversitario,
    }

    cadastrarCadeiraRequest(
      formData.nome,
      formData.plano_ensino,
      formData.centro_universitario,
      formattedHorarios,
    )
      .then((response) => {
        if (response === -1) {
          showToast('Erro ao cadastrar a cadeira!', false)
        } else {
          showToast('Cadastro realizado com sucesso!', true)
          navigate('/horarios')
        }
      })
      .catch((error) => {
        showToast(`Erro ao cadastrar a cadeira! ${error}`, false)
      })
  }

  const handleNomeChange = (event: ChangeEvent<HTMLInputElement>) => {
    setNome(event.target.value)
  }

  const handlePlanoEnsinoChange = (event: ChangeEvent<HTMLInputElement>) => {
    setPlanoEnsino(event.target.value)
  }

  const handleCentroChange = (event: ChangeEvent<HTMLInputElement>) => {
    setCentroUniversitario(event.target.value)
  }

  return (
    <>
      <Header />
      <div className={styles.cadastroContainer}>
        <div className={styles.cadastroContent}>
          <form onSubmit={handleSubmit}>
            <h1>Cadastro Cadeira</h1>
            <div className={styles.formGroup}>
              <label>Nome</label>
              <input
                type="text"
                value={nome}
                onChange={(e) => handleNomeChange(e)}
              />
            </div>
            <div className={styles.formGroup}>
              <label>Plano de Ensino</label>
              <input
                type="text"
                value={planoEnsino}
                onChange={(e) => handlePlanoEnsinoChange(e)}
              />
            </div>
            <div className={styles.formGroup}>
              <HorarioCadeira onSaveHorarios={handleSaveHorarios} />
            </div>
            <div className={styles.formGroup}>
              <label>Centro universitário</label>
              <input
                type="text"
                value={centroUniversitario}
                onChange={(e) => handleCentroChange(e)}
              />
            </div>
            <div>
              <button className="btn" type="submit">
                Salvar
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  )
}
