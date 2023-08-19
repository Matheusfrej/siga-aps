import { useEffect, useState } from 'react'
import Select from 'react-select'
import styles from './styles.module.css'

export interface HorarioInterface {
  dia: string
  horarios: string[]
}

const diasDaSemana = [
  { value: 'seg', label: 'Segunda-feira' },
  { value: 'ter', label: 'Terça-feira' },
  { value: 'qua', label: 'Quarta-feira' },
  { value: 'qui', label: 'Quinta-feira' },
  { value: 'sex', label: 'Sexta-feira' },
]

const horariosDisponiveis = [
  { value: 7, label: '07:00' },
  { value: 8, label: '08:00' },
  { value: 9, label: '09:00' },
  { value: 10, label: '10:00' },
  { value: 11, label: '11:00' },
  { value: 12, label: '12:00' },
  { value: 13, label: '13:00' },
  { value: 14, label: '14:00' },
  { value: 15, label: '15:00' },
  { value: 16, label: '16:00' },
  { value: 17, label: '17:00' },
  { value: 18, label: '18:00' },
  { value: 19, label: '19:00' },
  { value: 20, label: '20:00' },
  { value: 21, label: '21:00' },
  { value: 22, label: '22:00' },
]

interface HorarioCadeiraProps {
  onSaveHorarios: (formattedHorarios: any) => void
}

function HorarioCadeira({ onSaveHorarios }: HorarioCadeiraProps) {
  const [horariosCadeira, setHorariosCadeira] = useState<HorarioInterface[]>([])

  useEffect(() => {
    formatHorarios()
  }, [horariosCadeira])

  const handleDiaChange = (selectedOption: any) => {
    const dia = selectedOption.value
    const isDiaAlreadySelected = horariosCadeira.some(
      (horario) => horario.dia === dia,
    )

    if (!isDiaAlreadySelected) {
      setHorariosCadeira([...horariosCadeira, { dia, horarios: [] }])
    }
  }

  const handleHorarioChange = (selectedOptions: any, dia: string) => {
    const horarios = selectedOptions.map((option: any) => option.value)
    const updatedHorarios = horariosCadeira.map((horario) =>
      horario.dia === dia ? { ...horario, horarios } : horario,
    )
    setHorariosCadeira(updatedHorarios)
  }

  const formatHorarios = () => {
    const formattedHorarios = horariosCadeira
      .filter((horario) => horario.horarios.length > 0)
      .map((horario) => {
        const horarios = horario.horarios.map((h) => {
          if (typeof h === 'string') {
            return Number(h.split(':')[0])
          }
          return h
        })
        return { [horario.dia]: horarios }
      })
    onSaveHorarios(formattedHorarios[0])
  }

  return (
    <div className={styles.CampoForms}>
      <p>Horários das Cadeiras</p>
      <div>
        <Select
          options={diasDaSemana}
          onChange={handleDiaChange}
          placeholder="Selecione o dia"
        />
      </div>
      <div>
        {horariosCadeira.map((horario) => (
          <div key={horario.dia} style={{ margin: '1rem 0' }}>
            <p>{`Horários para ${
              horario.dia === 'seg'
                ? 'segunda'
                : horario.dia === 'ter'
                ? 'terça'
                : horario.dia === 'qua'
                ? 'quarta'
                : horario.dia === 'qui'
                ? 'quinta'
                : 'sexta'
            }`}</p>
            <Select
              options={horariosDisponiveis}
              isMulti
              onChange={(selectedOptions) =>
                handleHorarioChange(selectedOptions, horario.dia)
              }
              placeholder="Selecione os horários"
            />
          </div>
        ))}
      </div>
    </div>
  )
}

export default HorarioCadeira
