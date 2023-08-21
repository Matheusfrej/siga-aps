from flask_restful import Resource
from flask import request

from negocio.controladores import *
from negocio.cadastros import CadastroMatricula

from utils import AlunoStrategy

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from dotenv import load_dotenv

import traceback
import os


load_dotenv('config.env')
db_type = os.getenv('DB_TYPE')
if db_type == 'sqlalchemy':
    repo_factory = SQLAlchemyRepositorioFactory()
else:
    repo_factory = ListRepositorioFactory()

repo_matricula = repo_factory.criar_repositorio_matricula()
cadastro_matricula = CadastroMatricula(repo_matricula)

controladorMatricula = ControladorRealizarMatricula(cadastro_matricula)
controladorVisualizarHorarioCursadas = ControladorVisualizarHorario(
    strategy=AlunoStrategy(cadastro_matricula))


class MatriculaPresenter(Resource):
    def post(self):
        data = request.get_json()
        return controladorMatricula.cadastrar_matricula(data)


class DeletarMatriculaPresenter(Resource):
    def delete(self):
        data = request.get_json()
        return controladorMatricula.deletarMatriculaCadeira(data)


class EditarMatriculaPresenter(Resource):
    def put(self):
        data = request.get_json()
        return controladorMatricula.editarMatriculaCadeira(data)


class GetMatriculaPeriodoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token'),
            'periodo': request.headers.get('periodo')
        }
        return controladorMatricula.getMatriculaCadeira(data)
    
    
class GetMatriculasAlunoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return controladorMatricula.getMatriculasAluno(data)


class VerHorarioPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return controladorVisualizarHorarioCursadas.visualizarHorario(data)