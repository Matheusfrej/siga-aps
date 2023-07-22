from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from negocio import Fachada

app = Flask(__name__)
CORS(app)
api = Api(app)

fachada: Fachada = Fachada()

class LoginResource(Resource):
    def post(self):
        args = request.get_json()
        email = args['email']
        senha = args['senha']
        return fachada.efetuarLogin(email=email, senha=senha)

class UserInfoResource(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.getUserInfo(data)

class CadastrarCadeiraResource(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.cadastrarCadeira(data)

class EditarCadeiraResource(Resource):
    def put(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.editarCadeira(data)

class DeletarCadeiraResource(Resource):
    def delete(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.deletarCadeira(data)

class GetCadeirasProfessorResource(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.getCadeiraProfessor(data)
    
class MatriculaResource(Resource):
    def post(self):
        data = request.get_json()
        data['token'] = request.headers.get('token')
        return fachada.realizarMatriculaCadeira(data)
    
class VerHorarioResource(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return fachada.visualizarHorario(data)

api.add_resource(LoginResource, '/login')
api.add_resource(CadastrarCadeiraResource, '/cadastrar-cadeira')
api.add_resource(EditarCadeiraResource, '/editar-cadeira')
api.add_resource(DeletarCadeiraResource, '/deletar-cadeira')
api.add_resource(GetCadeirasProfessorResource, '/get-cadeiras-professor')
api.add_resource(VerHorarioResource, '/ver-horario')
api.add_resource(MatriculaResource, '/fazer-matricula')

if __name__ == '__main__':
    app.run(debug=True)