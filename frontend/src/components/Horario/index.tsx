import { SigabContext } from '../../contexts/sigabContext'
import { getHorarioRequest } from '../../services/horarioService'
import styles from './styles.module.css'
import { useEffect, useState, useContext } from 'react'

export function Horario() {
  const { showToast } = useContext(SigabContext)
  const [horario, setHorario] = useState()

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
  }, [])

  return (
    <div className={styles.horarioContainer}>
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
      </table>
    </div>
  )
}
