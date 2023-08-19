from flask import jsonify, Response
from utils import SingletonMetaclass

from negocio.controladores import *
from entidades import ContaProfessor
from negocio.cadastros import CadastroConta
from negocio.cadastros import CadastroCadeira
from negocio.cadastros import CadastroMatricula
from negocio.cadastros import CadastroOfertaCadeira
from subsistemaFirebase.iSubsistemaFirebase import iSubsistemaFirebase

from utils import ProfessorStrategy, AlunoStrategy

from utils import CadeiraSerializer, ContaSerializer, OfertaCadeiraSerializer

from utils import ConflitoDeHorarioError, CamposVaziosError

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from dotenv import load_dotenv

import traceback
import os

class Fachada(metaclass=SingletonMetaclass):
    def __init__(self) -> None:
        load_dotenv('config.env')
        db_type = os.getenv('DB_TYPE')
        if db_type == 'sqlalchemy':
            repo_factory = SQLAlchemyRepositorioFactory()
        else:
            repo_factory = ListRepositorioFactory()
        repo_conta = repo_factory.criar_repositorio_conta()
        repo_cadeira = repo_factory.criar_repositorio_cadeira()
        repo_matricula = repo_factory.criar_repositorio_matricula()
        repo_oferta_cadeira = repo_factory.criar_repositorio_oferta_cadeira()
        cadastro_conta = CadastroConta(repo_conta)
        cadastro_cadeira = CadastroCadeira(repo_cadeira)
        cadastro_matricula = CadastroMatricula(repo_matricula)
        cadastro_oferta_cadeira = CadastroOfertaCadeira(repo_oferta_cadeira)
        subsistemaFirebase = iSubsistemaFirebase()
        self.__subsistemaFirebase = subsistemaFirebase
        self.__controladorConta = ControladorConta(cadastro_conta,subsistemaFirebase)
        self.__controladorCadastroCadeira: ControladorCadastroCadeira = ControladorCadastroCadeira(
            cadastro_cadeira=cadastro_cadeira)
        self.__controladorRealizarMatricula = ControladorRealizarMatricula()
        self.__controladorOfertaCadeira: ControladorOfertaCadeira = ControladorOfertaCadeira(
            cadastro_oferta_cadeira=cadastro_oferta_cadeira
        )
        # TODO passar a strategy quando chamar o método e não inicialmente
        self.__controladorVisualizarHorarioLecionadas = ControladorVisualizarHorario(
            strategy=ProfessorStrategy(cadastro_oferta_cadeira)
        )
        self.__controladorVisualizarHorarioCursadas = ControladorVisualizarHorario(
            strategy=AlunoStrategy(cadastro_matricula)
        )

    def get_curr_user_decorator(func):
        ''' usar em métodos que precisam do usuário '''
        def wrapper(self, data):
            token = data.pop('token')
            user_info = self.__subsistemaFirebase.getInfoConta(token=token)
            email = user_info['users'][0]['email']
            data['user'] = self.__controladorConta.get_user_by_email(email=email)
            result = func(self, data)
            return result
        return wrapper

    def efetuarLogin(self, email: str, senha: str) -> Response:
        ''' Realiza o login '''
        try:
            data = self.__controladorConta.efetuarLogin(email=email, senha=senha)
            data['user'] = ContaSerializer(self.__controladorConta.get_user_by_email(email=email)).get_data()
            return data
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500
    
    def criarConta(self, email: str, senha: str) -> Response:
        try:
            conta = self.__subsistemaFirebase.criarConta(email=email, senha=senha)
            return conta
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def getUserInfo(self, data) -> Response:
        try:
            return ContaSerializer(data['user']).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def cadastrarCadeira(self, data) -> Response:
        try:
            cadeira = self.__controladorCadastroCadeira.cadastrar_cadeira(data)
            return CadeiraSerializer(cadeira).get_data()
        except CamposVaziosError as e:
            return e.__str__(), 400
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def editarCadeira(self, data) -> Response:
        try:
            cadeira = self.__controladorCadastroCadeira.editar_cadeira(data)
            return CadeiraSerializer(cadeira).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def deletarCadeira(self, data) -> Response:
        try:
            deleted = self.__controladorCadastroCadeira.deletar_cadeira(data)
            return {'success': deleted}
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def cadastrarOfertaCadeira(self, data) -> Response:
        try:
            data['professor'] = data.pop('user').id
            cadeira = self.__controladorOfertaCadeira.cadastrar_oferta_cadeira(data)
            return OfertaCadeiraSerializer(cadeira).get_data()
        except CamposVaziosError as e:
            return e.__str__(), 400
        except ConflitoDeHorarioError as e:
            return e.__str__(), 500
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def editarOfertaCadeira(self, data) -> Response:
        try:
            data['professor'] = data.pop('user')
            cadeira = self.__controladorOfertaCadeira.editar_oferta_cadeira(data)
            return OfertaCadeiraSerializer(cadeira).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def deletarOfertaCadeira(self, data) -> Response:
        try:
            deleted = self.__controladorOfertaCadeira.deletar_oferta_cadeira(data)
            return {'success': deleted}
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def getOfertaCadeirasProfessor(self, data) -> Response:
        try:
            ofertas_cadeiras = self.__controladorOfertaCadeira.get_ofertas_cadeiras_by_professor(data['user'].id)
            return OfertaCadeiraSerializer(ofertas_cadeiras, many=True).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    def realizarMatriculaCadeira(self) -> Response:
        try:
            pass
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

    @get_curr_user_decorator
    def visualizarHorario(self, data) -> Response:
        try:
            user = data['user']
            if type(user) is ContaProfessor:
                horario = self.__controladorVisualizarHorarioLecionadas.get_horario(user_id=user.id)
            else:
                horario = self.__controladorVisualizarHorarioCursadas.get_horario(user_id=user.id)
            return horario.data
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

