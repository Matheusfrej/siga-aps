from flask import jsonify, Response
from utils.singleton import SingletonMetaclass

from negocio.controladores import *

from negocio.cadastros import CadastroConta

class Fachada(metaclass=SingletonMetaclass):
    def __init__(self) -> None:
        cadastro_conta = CadastroConta()

        self.__controladorLogin = ControladorLogin(cadastro_conta)
        self.__controladorCadastroCadeira = ControladorCadastroCadeira()
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

    def cadastrarCadeira(self) -> Response:
        try:
            pass
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def realizarMatriculaCadeira(self) -> Response:
        try:
            pass
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def visualizarHorarioLecionadas(self) -> Response:
        try:
            pass
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def visualizarHorarioCursadas(self) -> Response:
        try:
            pass
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500