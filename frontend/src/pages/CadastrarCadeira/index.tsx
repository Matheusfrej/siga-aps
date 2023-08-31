/* eslint-disable @typescript-eslint/no-explicit-any */
import { ChangeEvent, FormEvent, useState, useContext, useEffect } from 'react'
import styles from './styles.module.css'
import '../../global.css'
import { SigabContext } from '../../contexts/sigabContext'
import {
  cadastrarOfertaCadeiraRequest,
  getCadeirasRequest,
} from '../../services/cadeiraService'
import { Header } from '../../components/Header'
import Select from 'react-select'
import HorarioCadeira from '../../components/HorarioCadeira'
import { useNavigate } from 'react-router'
import { CadeirasOfertadasSelectInterface } from '../Matricula'

export function CadastrarCadeira() {
  const { showToast } = useContext(SigabContext)
  const [cadeiraID, setCadeiraID] = useState<number>(0)
  const [centroUniversitario, setcentroUniversitario] = useState('')
  const [cadeirasDisponiveis, setCadeirasDisponiveis] = useState<any[]>()
  const [formattedHorarios, setFormattedHorarios] = useState<any[]>([])
  const navigate = useNavigate()

  const cadeirasSelect = cadeirasDisponiveis?.map((cadeira) => {
    return { value: cadeira.id, label: cadeira.nome }
  })

  const handleSaveHorarios = (formattedHorarios: any) => {
    setFormattedHorarios(formattedHorarios)
  }

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault()

    const formData = {
      cadeira: cadeiraID,
      centro_universitario: centroUniversitario,
    }
    console.log(formData)

    cadastrarOfertaCadeiraRequest(
      formData.cadeira,
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

  const handleCentroChange = (event: ChangeEvent<HTMLInputElement>) => {
    setcentroUniversitario(event.target.value)
  }

  const handleCadeiraChange = (
    selectedOptions: CadeirasOfertadasSelectInterface,
  ) => {
    setCadeiraID(selectedOptions.value)
    // console.log(cadeirasSelecionadas)
  }

  const getCadeirasDisponiveis = async () => {
    const token = localStorage.getItem('token')
    const response = await getCadeirasRequest(token!)
    setCadeirasDisponiveis(response)
  }

  useEffect(() => {
    getCadeirasDisponiveis()
  }, [])

  return (
    <>
      <Header />
      <div className={styles.cadastroContainer}>
        <div className={styles.cadastroContent}>
          <form onSubmit={handleSubmit}>
            <h1>Cadastrar oferta de cadeira</h1>
            <div className={`${styles.formGroup} ${styles.selectContainer}`}>
              <label>Cadeira</label>
              <Select
                options={cadeirasSelect}
                onChange={handleCadeiraChange}
                placeholder="Selecione uma cadeira"
                hideSelectedOptions
                className={styles.selectContainer}
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
