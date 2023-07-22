import { SigabContext } from '../../contexts/sigabContext'
import { getHorarioRequest } from '../../services/horarioService'
import styles from './styles.module.css'
import { useEffect, useState, useContext } from 'react'

export function Horario() {
  const { showToast } = useContext(SigabContext)
  const [horarioPessoa, setHorarioPessoa] = useState<any>()

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
              <tr key={idx}>
                {horario.map((value, idx2) => {
                  return (
                    <>
                      {value !== 'vazio' && (
                        <th key={idx2}>
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
                      {value === 'vazio' && <th key={idx2}></th>}
                    </>
                  )
                })}
              </tr>
            )
          }
          return (
            <tr key={idx}>
              {horario.map((value, idx3) => {
                const dia = matrizHorario[0][idx3]
                const hora = matrizHorario[idx][0]
                return (
                  <>
                    {value === '' &&
                    horarioPessoa !== undefined &&
                    dia in horarioPessoa &&
                    hora in horarioPessoa[dia] ? (
                      <td key={idx3}>
                        <div className={styles.horarioCard}>
                          <strong>{horarioPessoa[dia][hora]}</strong>
                          <span>
                            {hora}h - {hora}h50
                          </span>
                        </div>
                      </td>
                    ) : value === '' ? (
                      <td key={idx3}>
                        <div className={styles.horarioCard}></div>
                      </td>
                    ) : null}
                    {value !== '' && <td key={idx3}>{value}h</td>}
                  </>
                )
              })}
            </tr>
          )
        })}
      </table>
      {/* 
      <table>
        <tr>
          <th></th>
          <th>Segunda</th>
          <th>Terça</th>
          <th>Quarta</th>
          <th>Quinta</th>
          <th>Sexta</th>
          <th>Sábado</th>
        </tr>
        <tr>
          <td>7h</td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
        </tr>
        <tr>
          <td>8h</td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
        </tr>
        <tr>
          <td>9h</td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
        </tr>
        <tr>
          <td>10h</td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
          <td>
            <div className={styles.horarioCard}>
              <strong>Programação concorrente e distribuída</strong>
              <span>horario tal</span>
            </div>
          </td>
        </tr>
        <tr>
          <td>11h</td>
        </tr>
        <tr>
          <td>12h</td>
        </tr>
        <tr>
          <td>13h</td>
        </tr>
        <tr>
          <td>14h</td>
        </tr>
        <tr>
          <td>15h</td>
        </tr>
        <tr>
          <td>16h</td>
        </tr>
        <tr>
          <td>17h</td>
        </tr>
        <tr>
          <td>18h</td>
        </tr>
        <tr>
          <td>19h</td>
        </tr>
        <tr>
          <td>20h</td>
        </tr>
        <tr>
          <td>21h</td>
        </tr>
        <tr>
          <td>22h</td>
        </tr>
      </table> */}
    </div>
  )
}
