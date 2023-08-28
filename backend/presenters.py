from flask_restful import Resource
from flask import request
from negocio import Fachada

fachada: Fachada = Fachada()


class LoginPresenter(Resource):
    def post(self):
        args = request.get_json()
        email = args['email']
        senha = args['senha']
        return fachada.efetuarLogin(email=email, senha=senha)


class UserInfoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getUserInfo(data)


class CadastrarCadeiraPresenter(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.cadastrarCadeira(data)


class EditarCadeiraPresenter(Resource):
    def put(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.editarCadeira(data)


class DeletarCadeiraPresenter(Resource):
    def delete(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.deletarCadeira(data)


class CadastrarOfertaCadeiraPresenter(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.cadastrarOfertaCadeira(data)


class EditarOfertaCadeiraPresenter(Resource):
    def put(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.editarOfertaCadeira(data)


class DeletarOfertaCadeiraPresenter(Resource):
    def delete(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.deletarOfertaCadeira(data)


class GetOfertasCadeirasProfessorPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getOfertaCadeirasProfessor(data)
    

class GetOfertasCadeirasPeriodoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token'),
            'periodo': request.headers.get('periodo')
        }
        return fachada.getOfertaCadeirasPeriodo(data)


class MatriculaPresenter(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.realizarMatriculaCadeira(data)


class VerHorarioPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.visualizarHorario(data)