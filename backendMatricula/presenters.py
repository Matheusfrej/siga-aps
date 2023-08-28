from flask_restful import Resource
from flask import request

from negocio.controladores import *
from negocio.cadastros import CadastroMatricula

from utils import AlunoStrategy, MatriculaSerializer

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from comunicacao.contaService import ContaServiceAPI

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

conta_service_api = ContaServiceAPI()

class LoginRequiredMixin(Resource):
    def dispatch_request(self, *args, **kwargs):
        self.current_user = conta_service_api.get_user_info(headers=request.headers)
        return super().dispatch_request(*args, **kwargs)

class MatriculaPresenter(LoginRequiredMixin):
    def post(self):
        data = request.get_json()
        data['aluno_id'] = self.current_user['id']
        try:
            result = controladorMatricula.cadastrar_matricula(data)
            return MatriculaSerializer(result).get_data()
        except Exception as e:
            print(traceback.format_exc())
            return e.__str__(), 500


class DeletarMatriculaPresenter(Resource):
    def delete(self, matricula_id):
        return controladorMatricula.deletarMatriculaCadeira(matricula_id)


class EditarMatriculaPresenter(LoginRequiredMixin):
    def put(self, matricula_id):
        data = request.get_json()
        data['aluno_id'] = self.current_user['id']
        data['id'] = matricula_id
        return MatriculaSerializer(controladorMatricula.editarMatriculaCadeira(data))


class GetMatriculaPeriodoPresenter(LoginRequiredMixin):
    def get(self):
        return MatriculaSerializer(controladorMatricula.getMatriculaCadeira(self.current_user['id']))
    
    
class GetMatriculasAlunoPresenter(LoginRequiredMixin):
    def get(self):
        return MatriculaSerializer(controladorMatricula.getMatriculasAluno(self.current_user['id']))


class VerHorarioPresenter(LoginRequiredMixin):
    def get(self):
        return controladorVisualizarHorarioCursadas.get_horario(self.current_user['id']).data