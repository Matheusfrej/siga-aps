import { useState, useEffect } from 'react'
import { Header } from '../../components/Header'
import { Horario } from '../../components/Horario'
import Select from 'react-select'
import styles from './styles.module.css'
import { getOfertasCadeiraPeriodo } from '../../services/cadeiraService'
import { matriculaRequest } from '../../services/matriculaService'
import { invokeToast } from '../../services/toastService'
import { useNavigate } from 'react-router-dom'

export interface CadeirasOfertadasSelectInterface {
  value: number
  label: string
}

export interface OfertaCadeiraInterface {
  id: number
  horario: any
  periodo: string
  plano_ensino: string
  professor_id: number
  centro_universitario: string
  cadeira: {
    id: number
    ementa: string
    nome: string
  }
}

export interface Dicio {
  seg: Record<string, string>
  ter: Record<string, string>
  qua: Record<string, string>
  qui: Record<string, string>
  sex: Record<string, string>
  sab: Record<string, string>
  dom: Record<string, string>
}

export function Matricula() {
  const [currentHorario, setCurrentHorario] = useState<object>({})
  const [cadeirasSelecionadas, setCadeirasSelecionadas] = useState<number[]>()
  const [cadeirasOfertadas, setCadeirasOfertadas] =
    useState<OfertaCadeiraInterface[]>()

  const cadeirasOfertadasSelect = cadeirasOfertadas?.map((ofertaCadeira) => {
    return { value: ofertaCadeira.id, label: ofertaCadeira.cadeira.nome }
  })

  const getCadeiraOfertada = (id: number) => {
    return cadeirasOfertadas?.filter(
      (cadeiraOfertada) => id === cadeiraOfertada.id,
    )[0]
  }

  const navigate = useNavigate()

  const handleCadeiraChange = (
    selectedOptions: CadeirasOfertadasSelectInterface[],
  ) => {
    setCadeirasSelecionadas(
      selectedOptions.map(
        (selectedOption: { value: number }) => selectedOption.value,
      ),
    )
    // console.log(cadeirasSelecionadas)
  }

  useEffect(() => {
    // console.log('entrou')

    const dicio: Dicio = {
      seg: {},
      ter: {},
      qua: {},
      qui: {},
      sex: {},
      sab: {},
      dom: {},
    }
    const cadeirasSelecionadasCompletas = cadeirasSelecionadas?.map(
      (cadeira) => {
        return getCadeiraOfertada(cadeira)
      },
    )

    cadeirasSelecionadasCompletas?.forEach((cadeira) => {
      for (const [k, v] of Object.entries(cadeira!.horario)) {
        for (const h of v) {
          dicio[k][h] = cadeira?.cadeira.nome
        }
      }
    })

    setCurrentHorario(dicio)
    // console.log(currentHorario)

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [cadeirasSelecionadas])

  const getOfertasCadeiras = async () => {
    const cadeiras = await getOfertasCadeiraPeriodo()
    setCadeirasOfertadas(cadeiras)
  }

  const fazMatricula = async () => {
    // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
    const token = localStorage.getItem('token')
    const response = await matriculaRequest(cadeirasSelecionadas!, token!)
    if (response !== -1) {
      invokeToast('Matrícula realizada com sucesso', true)
      navigate('/horarios')
      // setInterval(() => {
      //   navigate('/')
      // }, 3000)
    } else {
      invokeToast('Houve um erro ao realizar a matrícula', false)
    }
  }

  useEffect(() => {
    getOfertasCadeiras()
  }, [])
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
          <div className={styles.selectContainer}>
            <Select
              options={cadeirasOfertadasSelect}
              onChange={handleCadeiraChange}
              placeholder="Selecione suas cadeiras"
              hideSelectedOptions
              isMulti
            />
          </div>
          <Horario isMatricula={true} horarioMatricula={currentHorario} />

          <button
            className={`btn ${styles.confirmButton}`}
            onClick={() => fazMatricula()}
          >
            Confirmar
          </button>
        </div>
      </div>
    </>
  )
}
