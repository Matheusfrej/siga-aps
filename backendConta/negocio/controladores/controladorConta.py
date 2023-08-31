from utils import SingletonMetaclass

from flask import Response

import traceback

from utils import EmailSenhaInvalidosException

class ControladorConta(metaclass=SingletonMetaclass):
    def __init__(self, cadastroConta, iSubsistemaFirebase):
        self.__cadastroConta = cadastroConta
        self.__iSubsistemaFirebase = iSubsistemaFirebase

    def efetuarLogin(self, email, senha):
        logado = self.__iSubsistemaFirebase.validarLogin(email, senha)
        if logado:
            return logado
        else:
            raise EmailSenhaInvalidosException()
    
    def get_user_by_email(self, email):
        user = self.__cadastroConta.get_by_email(email)
        if user:
            return user
        else:
            return {'error': 'usuário não encontrado'}, 404

    def criarConta(self, email: str, senha: str) -> Response:
        try:
            conta = self.__iSubsistemaFirebase.criarConta(email=email, senha=senha)
            return conta
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
    
    def get_curr_user_by_token(self, data):
        ''' usar em métodos que precisam do usuário '''
        token = data.pop('token')
        user_info = self.__iSubsistemaFirebase.getInfoConta(token=token)
        email = user_info['users'][0]['email']
        user = self.get_user_by_email(email=email)
        return user