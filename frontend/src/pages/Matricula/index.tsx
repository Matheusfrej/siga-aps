import { useState } from 'react'
import { Header } from '../../components/Header'
import { Horario } from '../../components/Horario'
import styles from './styles.module.css'

export function Matricula() {
  const [currentHorario, setCurrentHorario] = useState<object>({})

  // {
  //   "seg": {
  //       "8": "Programação Concorrente Distribuída",
  //       "9": "Programação Concorrente Distribuída",
  //       "10": "Análise e Projetos de Sistemas",
  //       "11": "Análise e Projetos de Sistemas"
  //   },
  //   "ter": {
  //       "8": "Sistemas de Informação",
  //       "9": "Sistemas de Informação",
  //       "10": "Tópicos Avançados em Algoritmos",
  //       "11": "Tópicos Avançados em Algoritmos"
  //   },
  //   "qua": {
  //       "8": "Análise e Projetos de Sistemas",
  //       "9": "Análise e Projetos de Sistemas",
  //       "10": "Programação Concorrente Distribuída",
  //       "11": "Programação Concorrente Distribuída"
  //   },
  //   "qui": {
  //       "8": "Tópicos Avançados em Algoritmos",
  //       "9": "Tópicos Avançados em Algoritmos",
  //       "10": "Sistemas de Informação",
  //       "11": "Sistemas de Informação"
  //   },
  //   "sex": {},
  //   "sab": {}
  // }

  return (
    <>
      <Header />
      <div className={styles.matriculaContainer}>
        <div className={styles.matriculaContent}>
          <h1>Matricula</h1>

          <Horario isMatricula={true} horarioMatricula={currentHorario} />
        </div>
      </div>
    </>
  )
}
