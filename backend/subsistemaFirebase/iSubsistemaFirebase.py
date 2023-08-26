from subsistemaFirebase.fachadaComunicacaoFirebase import Firebase
from dotenv import load_dotenv
from utils import SingletonMetaclass

import traceback
import os


class iSubsistemaFirebase(metaclass=SingletonMetaclass):
    def __init__(self):
        load_dotenv('config.env')
        self.api_key=os.getenv('API_KEY')
        self.auth_domain=os.getenv('AUTH_DOMAIN')
        self.config = {
        'apiKey': self.api_key,
        'authDomain': self.auth_domain
        } 
        self.__fachadaFirebase = Firebase(self.config).auth()

    def validarLogin(self, email, senha):
        logado = self.__fachadaFirebase.validarLogin(email, senha)
        return logado
    
    def getInfoConta(self, token):
        token = self.__fachadaFirebase.infoConta(token)
        return token
    
    def criarConta(self, email, senha):
        try:
            conta = self.__fachadaFirebase.criarConta(email,senha)
            return conta
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
