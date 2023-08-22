class ConflitoDeHorarioError(Exception):
    def __init__(self, nova_cadeira, cadeira_conflito):
        self.nova_cadeira = nova_cadeira
        self.cadeira_conflito = cadeira_conflito

    def __str__(self):
        return f'Conflito de Horário: Não foi possível se matricular em {self.nova_cadeira} porque seu horário conflita com {self.cadeira_conflito}.'

class CamposVaziosError(Exception):
    def __init__(self, campos):
        self.campos = campos

    def __str__(self):
        return f'Existem campos não preenchidos: {", ".join(self.campos)}.'
   
    
class ConflitoDeEquivalencia(Exception):
    def __init__(self, nova_cadeira, cadeira_conflito):
        self.nova_cadeira = nova_cadeira
        self.cadeira_conflito = cadeira_conflito

    def __str__(self):
        return f'Conflito de Equivalência: Não foi possível se matricular em {self.nova_cadeira} porque já cursou sua equivalente {self.cadeira_conflito}.'
    

class ConflitoDePreRequisito(Exception):
    def __init__(self, nova_cadeira):
        self.nova_cadeira = nova_cadeira

    def __str__(self):
        return f'Conflito de Requisito: Não foi possível se matricular em {self.nova_cadeira} porque você não cursou seus pré-requisitos.'
    

class ConflitoDeCoRequisito(Exception):
    def __init__(self, nova_cadeira):
        self.nova_cadeira = nova_cadeira

    def __str__(self):
        return f'Conflito de Requisito: Não foi possível se matricular em {self.nova_cadeira} porque você não se matriculou também em seus co-requisitos.'
    
    
class CadeiraJaCursada(Exception):
    def __init__(self, nova_cadeira):
        self.nova_cadeira = nova_cadeira

    def __str__(self):
        return f'Conflito: Não foi possível se matricular em {self.nova_cadeira} porque você já cursou essa cadeira.'



class MatriculaJaRealizada(Exception):
    def __str__(self):
        return f'Você já fez matricula nesse período letivo.'