from flask import jsonify, Response
from utils.singleton import SingletonMetaclass

from negocio.controladores import *
from entidades import ContaProfessor
from negocio.cadastros import CadastroConta
from negocio.cadastros import CadastroCadeira
from negocio.cadastros import CadastroMatricula
from subsistemaFirebase.iSubsistemaFirebase import iSubsistemaFirebase

from utils import ProfessorStrategy, AlunoStrategy

class Fachada(metaclass=SingletonMetaclass):
    def __init__(self) -> None:
        cadastro_conta = CadastroConta()
        cadastro_cadeira = CadastroCadeira()
        cadastro_matricula = CadastroMatricula()
        subsistemaFirebase = iSubsistemaFirebase()
        self.__currentUser = None
        self.__userType = None
        self.__subsistemaFirebase = subsistemaFirebase
        self.__controladorConta = ControladorConta(cadastro_conta,subsistemaFirebase)
        self.__controladorCadastroCadeira: ControladorCadastroCadeira = ControladorCadastroCadeira(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_conta=cadastro_conta)
        self.__controladorRealizarMatricula = ControladorRealizarMatricula()
        self.__controladorVisualizarHorarioLecionadas = ControladorVisualizarHorario(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_matricula=cadastro_matricula,
            strategy=ProfessorStrategy
        )
        self.__controladorVisualizarHorarioCursadas = ControladorVisualizarHorario(
            cadastro_cadeira=cadastro_cadeira,
            cadastro_matricula=cadastro_matricula,
            strategy=AlunoStrategy
        )

    def efetuarLogin(self, email: str, senha: str) -> Response:
        try:
            token = self.__controladorConta.efetuarLogin(email=email, senha=senha)
            return {'TOKEN': token}
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
            email = user_info["users"][0]["email"]
            user = self.__controladorConta.get_user_by_email(email=email)
            print(user)
            obj = user.__dict__.copy()
            obj.pop('_sa_instance_state')
            return obj
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def cadastrarCadeira(self, data) -> Response:
        try:
            cadeira = self.__controladorCadastroCadeira.cadastrar_cadeira(data)
            obj = cadeira.__dict__.copy()
            obj.pop('_sa_instance_state')
            return obj
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500
    
    def editarCadeira(self, data) -> Response:
        try:
            cadeira = self.__controladorCadastroCadeira.editar_cadeira(data)
            obj = cadeira.__dict__.copy()
            obj.pop('_sa_instance_state')
            return obj
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

    def deletarCadeira(self, data) -> Response:
        try:
            cadeira = self.__controladorCadastroCadeira.deletar_cadeira(data)
            obj = cadeira.__dict__.copy()
            obj.pop('_sa_instance_state')
            return obj
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500
    
    def getCadeirProfessor(self, data) -> Response:
        try:
            cadeira = self.__controladorCadastroCadeira.get_cadeira_by_professor(data)
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

    def visualizarHorario(self, data) -> Response:
        try:
            user = self.getUserInfo(data.get('token'))
            print(user)
            print(user)
            if type(user) == ContaProfessor:
                horario = self.__controladorVisualizarHorarioLecionadas.get_horario(user_id=user.get('id'))
            else:
                horario = self.__controladorVisualizarHorarioCursadas.get_horario(user_id=user.get('id'))
            print(horario.data)
            return horario.data
        except Exception as e:
            print(e)
            return 'Erro interno do servidor', 500

