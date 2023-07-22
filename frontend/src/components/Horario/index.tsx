import { SigabContext } from '../../contexts/sigabContext'
import { getHorarioRequest } from '../../services/horarioService'
import styles from './styles.module.css'
import { useEffect, useState, useContext } from 'react'

export function Horario() {
  const { showToast } = useContext(SigabContext)
  const [horario, setHorario] = useState<object>()

  const matrizHorario = [
    ['vazio', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab'],
    ['7h', '', '', '', '', '', ''],
    ['8h', '', '', '', '', '', ''],
    ['9h', '', '', '', '', '', ''],
    ['10h', '', '', '', '', '', ''],
    ['11h', '', '', '', '', '', ''],
    ['12h', '', '', '', '', '', ''],
    ['13h', '', '', '', '', '', ''],
    ['14h', '', '', '', '', '', ''],
    ['15h', '', '', '', '', '', ''],
    ['16h', '', '', '', '', '', ''],
    ['17h', '', '', '', '', '', ''],
    ['18h', '', '', '', '', '', ''],
    ['19h', '', '', '', '', '', ''],
    ['20h', '', '', '', '', '', ''],
    ['21h', '', '', '', '', '', ''],
    ['22h', '', '', '', '', '', ''],
  ]

  const getHorario = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
      return
    }
    console.log(token)

    const response = await getHorarioRequest(token)
    if (response === -1) {
      showToast('Houve um erro ao carregar os seus horários', false)
      return
    }
    console.log('chegou em Horario', response)
  }

  useEffect(() => {
    getHorario()
    setHorario({
      seg: {
        '8': 'Programação Concorrente Distribuída',
        '9': 'Programação Concorrente Distribuída',
        '10': 'Análise e Projetos de Sistemas',
        '11': 'Análise e Projetos de Sistemas',
      },
      ter: {
        '8': 'Sistemas de Informação',
        '9': 'Sistemas de Informação',
        '10': 'Análise e Projetos de Sistemas',
        '11': 'Análise e Projetos de Sistemas',
      },
      qua: {
        '10': 'Programação Concorrente Distribuída',
        '11': 'Programação Concorrente Distribuída',
        '8': 'Análise e Projetos de Sistemas',
        '9': 'Análise e Projetos de Sistemas',
      },
      qui: {
        '10': 'Sistemas de Informação',
        '11': 'Sistemas de Informação',
        '8': 'Análise e Projetos de Sistemas',
        '9': 'Análise e Projetos de Sistemas',
      },
      sex: {},
      sab: {},
    })
  }, [])

  return (
    <div className={styles.horarioContainer}>
      <table>
        {matrizHorario.map((horario, idx) => {
          if (idx === 0) {
            return (
              <tr key={idx}>
                {horario.map((value, idx) => {
                  return (
                    <>
                      {value !== 'vazio' && (
                        <th key={idx}>
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
                      {value === 'vazio' && <th key={idx}></th>}
                    </>
                  )
                })}
              </tr>
            )
          }
          return (
            <tr key={idx}>
              {horario.map((value, idx) => {
                return (
                  <>
                    {value === '' && (
                      <td key={idx}>
                        <div className={styles.horarioCard}>
                          <strong>Programação concorrente e distribuída</strong>
                          <span>horario tal</span>
                        </div>
                      </td>
                    )}
                    {value !== '' && <td key={value + idx}>{value}</td>}
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
