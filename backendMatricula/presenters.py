from flask_restful import Resource
from flask import request
from negocio import Fachada

fachada: Fachada = Fachada()


class UserInfoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getUserInfo(data)


class MatriculaPresenter(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.realizarMatriculaCadeira(data)


class DeletarMatriculaPresenter(Resource):
    def delete(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.deletarMatriculaCadeira(data)


class EditarMatriculaPresenter(Resource):
    def put(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.editarMatriculaCadeira(data)


class GetMatriculaPeriodoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token'),
            'periodo': request.headers.get('periodo')
        }
        return fachada.getMatriculaCadeira(data)
    
    
class GetMatriculasAlunoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getMatriculasAluno(data)


class VerHorarioPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.visualizarHorario(data)