from flask import jsonify, Response
from utils.singleton import SingletonMetaclass

from negocio.controladores import *

from negocio.cadastros import CadastroConta
from negocio.cadastros import CadastroCadeira
from subsistemaFirebase.iSubsistemaFirebase import iSubsistemaFirebase

class Fachada(metaclass=SingletonMetaclass):
    def __init__(self) -> None:
        cadastro_conta = CadastroConta()
        cadastro_cadeira = CadastroCadeira()
        subsistemaFirebase = iSubsistemaFirebase()
        self.__subsistemaFirebase = subsistemaFirebase
        self.__controladorLogin = ControladorLogin(cadastro_conta,subsistemaFirebase)
        self.__controladorCadastroCadeira: ControladorCadastroCadeira = ControladorCadastroCadeira(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_conta=cadastro_conta)
        self.__controladorRealizarMatricula = ControladorRealizarMatricula()
        self.__controladorVisualizarHorarioLecionadas = ControladorVisualizarHorario()
        self.__controladorVisualizarHorarioCursadas = ControladorVisualizarHorario()

    def efetuarLogin(self, email: str, senha: str) -> Response:
        try:
            token = self.__controladorLogin.efetuarLogin(email=email, senha=senha)
            return token
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500
    
    def criarConta(self, email: str, senha: str) -> Response:
        try:
            conta = self.__subsistemaFirebase.criarConta(email=email, senha=senha)
            return conta
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500
    
    def getUserInfo(self, token: str) -> Response:
        try:
            user_info = self.__subsistemaFirebase.getInfoConta(token=token)
            return user_info["users"][0]["email"]
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def cadastrarCadeira(self, data) -> Response:
        print(data)
        try:
            cadeira = self.__controladorCadastroCadeira.cadastrar_cadeira(data)
            obj = cadeira.__dict__.copy()
            obj.pop('_sa_instance_state')
            return obj
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def realizarMatriculaCadeira(self) -> Response:
        try:
            pass
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def visualizarHorario(self) -> Response:
        try:
            pass
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500
