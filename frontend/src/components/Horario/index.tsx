import { SigabContext } from '../../contexts/sigabContext'
import { getHorarioRequest } from '../../services/horarioService'
import styles from './styles.module.css'
import { useEffect, useState, useContext } from 'react'

export function Horario() {
  const { showToast } = useContext(SigabContext)
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [horarioPessoa, setHorarioPessoa] = useState<any>()

  const listaCadeiras: string[] = []

  const matrizHorario = [
    ['vazio', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab'],
    ['7', '', '', '', '', '', ''],
    ['8', '', '', '', '', '', ''],
    ['9', '', '', '', '', '', ''],
    ['10', '', '', '', '', '', ''],
    ['11', '', '', '', '', '', ''],
    ['12', '', '', '', '', '', ''],
    ['13', '', '', '', '', '', ''],
    ['14', '', '', '', '', '', ''],
    ['15', '', '', '', '', '', ''],
    ['16', '', '', '', '', '', ''],
    ['17', '', '', '', '', '', ''],
    ['18', '', '', '', '', '', ''],
    ['19', '', '', '', '', '', ''],
    ['20', '', '', '', '', '', ''],
    ['21', '', '', '', '', '', ''],
    ['22', '', '', '', '', '', ''],
  ]

  const getHorario = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
      return
    }

    const response = await getHorarioRequest(token)
    if (response === -1) {
      showToast('Houve um erro ao carregar os seus horários', false)
      return
    }
    delete response.dom
    setHorarioPessoa(response)
  }

  useEffect(() => {
    getHorario()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <div className={styles.horarioContainer}>
      <table>
        {matrizHorario.map((horario, idx) => {
          if (idx === 0) {
            return (
              <thead key={idx}>
                <tr>
                  {horario.map((value, idx2) => {
                    return (
                      <>
                        {value !== 'vazio' && (
                          <th key={`${idx}${idx2}`}>
                            {value === 'seg'
                              ? 'Segunda'
                              : value === 'ter'
                              ? 'Terça'
                              : value === 'qua'
                              ? 'Quarta'
                              : value === 'qui'
                              ? 'Quinta'
                              : value === 'sex'
                              ? 'Sexta'
                              : 'Sábado'}
                          </th>
                        )}
                        {value === 'vazio' && <th key={`${idx}${idx2}`}></th>}
                      </>
                    )
                  })}
                </tr>
              </thead>
            )
          }
          return (
            <tbody key={idx}>
              <tr>
                {horario.map((value, idx3) => {
                  const dia = matrizHorario[0][idx3]
                  const hora = matrizHorario[idx][0]
                  const temCadeira =
                    value === '' &&
                    horarioPessoa !== undefined &&
                    dia in horarioPessoa &&
                    hora in horarioPessoa[dia]
                  let nomeCadeira = ''
                  if (temCadeira) {
                    nomeCadeira = horarioPessoa[dia][hora]
                    if (!listaCadeiras.includes(nomeCadeira)) {
                      listaCadeiras.push(nomeCadeira)
                    }
                  }
                  return (
                    <>
                      {temCadeira ? (
                        <td
                          key={`${idx}${idx3}`}
                          className={
                            styles[
                              'cadeira' + listaCadeiras.indexOf(nomeCadeira)
                            ]
                          }
                        >
                          <div className={styles.horarioCard}>
                            <strong>{nomeCadeira}</strong>
                            <span>
                              {hora}h - {hora}h50
                            </span>
                          </div>
                        </td>
                      ) : value === '' ? (
                        <td key={`${idx}${idx3}`}>
                          <div className={styles.horarioCard}></div>
                        </td>
                      ) : null}
                      {value !== '' && <td key={`${idx}${idx3}`}>{value}h</td>}
                    </>
                  )
                })}
              </tr>
            </tbody>
          )
        })}
      </table>
    </div>
  )
}
