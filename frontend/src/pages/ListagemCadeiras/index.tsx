import { useContext, useEffect, useState } from 'react'
import {
  deletarCadeiraRequest,
  getCadeiras,
} from '../../services/cadeiraService'
import { Header } from '../../components/Header'
import styles from './styles.module.css'
import { Trash, Pencil } from '@phosphor-icons/react'
import { useNavigate } from 'react-router-dom'
import { SigabContext } from '../../contexts/sigabContext'

interface CadeiraInterface {
  id: number
  nome: string
  plano_ensino: string
  centro_universitario: string
  horarios: any[]
}

export function ListagemCadeiras() {
  const { showToast } = useContext(SigabContext)
  const [cadeiras, setCadeiras] = useState<CadeiraInterface[]>([])
  const navigate = useNavigate()

  const fetchCadeiras = async () => {
    try {
      const response = await getCadeiras()
      setCadeiras(response)
    } catch (error) {}
  }

  useEffect(() => {
    fetchCadeiras()
  }, [])

  const handleEditCadeira = async (cadeiraId: number) => {
    console.log('editou cadeira', cadeiraId)
  }

  const handleDeleteCadeira = async (cadeiraId: number) => {
    try {
      await deletarCadeiraRequest(cadeiraId)
      fetchCadeiras()
      showToast('Cadeira deletada com sucesso', true)
    } catch (error) {
      showToast('Houve um erro ao deletar uma cadeira', false)
    }
  }

  return (
    <>
      <Header />
      <div className={styles.listagemContainer}>
        <div className={styles.listagemContent}>
          <div
            style={{
              display: 'flex',
              gap: '2rem',
              justifyContent: 'center',
              alignItems: 'center',
            }}
          >
            <h1>Listagem de Cadeiras</h1>
            <button
              className="btn"
              onClick={() => navigate('/cadastrar-cadeira')}
            >
              <strong>Cadastrar uma nova cadeira</strong>
            </button>
          </div>
          <table className={styles.customTable}>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Plano de Ensino</th>
                <th>Centro Universitário</th>
                <th>Ação</th>
              </tr>
            </thead>
            <tbody>
              {cadeiras.map((cadeira) => (
                <tr key={cadeira.id}>
                  <td>{cadeira.nome}</td>
                  <td>{cadeira.plano_ensino}</td>
                  <td>{cadeira.centro_universitario}</td>
                  <td>
                    <div className={styles.actionsContainer}>
                      <button
                        className="btn"
                        onClick={() => handleDeleteCadeira(cadeira.id)}
                      >
                        <Trash />
                      </button>
                      <button
                        className="btn"
                        onClick={() => handleEditCadeira(cadeira.id)}
                      >
                        <Pencil />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  )
}
