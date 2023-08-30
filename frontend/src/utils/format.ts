const formatWeekday = (weekday: string) => {
  return `${
    weekday === 'seg'
      ? 'Segunda'
      : weekday === 'ter'
      ? 'Terça'
      : weekday === 'qua'
      ? 'Quarta'
      : weekday === 'qui'
      ? 'Quinta'
      : weekday === 'sex'
      ? 'Sexta'
      : 'Sábado'
  }`
}

export { formatWeekday }
