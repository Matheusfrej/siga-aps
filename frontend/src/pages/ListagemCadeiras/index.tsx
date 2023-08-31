import { useContext, useEffect, useState } from 'react'
import {
  deletarCadeiraRequest,
  getCadeirasProfessor,
} from '../../services/cadeiraService'
import { Header } from '../../components/Header'
import styles from './styles.module.css'
import { Trash } from '@phosphor-icons/react'
import { useNavigate } from 'react-router-dom'
import { SigabContext } from '../../contexts/sigabContext'
import { OfertaCadeiraInterface } from '../Matricula'
import { formatWeekday } from '../../utils/format'

export function ListagemCadeiras() {
  const { showToast } = useContext(SigabContext)
  const [cadeiras, setCadeiras] = useState<OfertaCadeiraInterface[]>([])
  const navigate = useNavigate()

  const fetchCadeiras = async () => {
    try {
      const token = localStorage.getItem('token')
      if (token) {
        const response = await getCadeirasProfessor(token)
        console.log(response)

        setCadeiras(response)
      }
    } catch (error) {}
  }

  useEffect(() => {
    fetchCadeiras()
  }, [])

  // const handleEditCadeira = async (cadeiraId: number) => {
  //   console.log('editou cadeira', cadeiraId)
  // }

  const handleDeleteCadeira = async (cadeiraId: number) => {
    try {
      const token = localStorage.getItem('token')
      await deletarCadeiraRequest(cadeiraId, token!)
      fetchCadeiras()
      showToast('Cadeira deletada com sucesso', true)
    } catch (error) {
      showToast('Houve um erro ao deletar uma cadeira', false)
    }
  }

  const formatHorarioToString = (horario: any) => {
    const teste = {
      sex: [15, 16],
      seg: [12, 13],
    }
    return Object.entries(teste).map((h: any[], idx: number) => {
      return `${formatWeekday(h[0])}: ${h[1]
        .map((hora: number) => hora + ' - ' + hora + 'h50')
        .join(', ')}${idx !== Object.entries(teste).length - 1 ? ' | ' : ''}`
    })
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
                <th>Centro Universitário</th>
                <th>Horário</th>
                <th>Ação</th>
              </tr>
            </thead>
            <tbody>
              {cadeiras.map((cadeira) => (
                <tr key={cadeira.id}>
                  <td>{cadeira.cadeira.nome}</td>
                  <td>{cadeira.centro_universitario}</td>
                  <td>{formatHorarioToString(cadeira.horario)}</td>
                  <td>
                    <div className={styles.actionsContainer}>
                      <button
                        className="btn"
                        onClick={() => handleDeleteCadeira(cadeira.id)}
                      >
                        <Trash />
                      </button>
                      {/* <button
                        className="btn"
                        onClick={() => handleEditCadeira(cadeira.id)}
                      >
                        <Pencil />
                      </button> */}
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
