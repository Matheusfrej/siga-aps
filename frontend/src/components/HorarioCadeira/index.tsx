import { useEffect, useState } from 'react'
import Select from 'react-select'
import styles from './styles.module.css'
import { formatWeekday } from '../../utils/format'

export interface HorarioInterface {
  dia: string[]
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

interface HorarioCadeiraProps {
  onSaveHorarios: (formattedHorarios: any) => void
}

function HorarioCadeira({ onSaveHorarios }: HorarioCadeiraProps) {
  const [horariosCadeira, setHorariosCadeira] = useState<any>({})

  const handleDiaChange = (selectedOption: any) => {
    const dia = selectedOption.value
    if (!(dia in horariosCadeira)) {
      setHorariosCadeira((prevHorarios: any) => ({
        ...prevHorarios,
        [dia]: [],
      }))
    }
  }

  const handleHorarioChange = (selectedOptions: any, dia: string) => {
    const horarios = selectedOptions.map((option: any) => option.value)
    setHorariosCadeira((prevHorarios: any) => ({
      ...prevHorarios,
      [dia]: horarios,
    }))
  }

  useEffect(() => {
    onSaveHorarios(horariosCadeira)
  }, [horariosCadeira])

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
        {Object.keys(horariosCadeira).map((dia) => (
          <div key={dia} style={{ margin: '1rem 0' }}>
            <p>{`Horários para ${formatWeekday(dia)}`}</p>
            <Select
              options={horariosDisponiveis}
              isMulti
              onChange={(selectedOptions) =>
                handleHorarioChange(selectedOptions, dia)
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
