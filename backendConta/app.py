from flask import Flask, request
from flask import request

from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from dotenv import load_dotenv

from dados import SQLAlchemyRepositorioFactory, ListRepositorioFactory

from negocio import CadastroConta
from negocio import ControladorConta

from utils import ContaSerializer

from subsistemaFirebase import iSubsistemaFirebase

import os
import traceback

from utils import EmailSenhaInvalidosException

app = Flask(__name__)
CORS(app)
api = Api(app)

load_dotenv('config.env')
db_type = os.getenv('DB_TYPE')
if db_type == 'sqlalchemy':
    repo_factory = SQLAlchemyRepositorioFactory()
else:
    repo_factory = ListRepositorioFactory()

parser = reqparse.RequestParser()
parser.add_argument('ids', type=int, action='append', required=True)

repo_conta = repo_factory.criar_repositorio_conta()

cadastro_cadeira = CadastroConta(repo_conta)

fachada_firebase = iSubsistemaFirebase()

controlador_conta = ControladorConta(cadastro_cadeira, fachada_firebase)

class LoginPresenter(Resource):
    def post(self):
        try:
            args = request.get_json()
            email = args['email']
            senha = args['senha']
            print(email, senha)
            response = controlador_conta.efetuarLogin(email=email, senha=senha)
            if response:
                response['user'] = ContaSerializer(controlador_conta.get_user_by_email(email=email)).get_data()
                return response
            else:
                return {'error': 'email ou senha inválidos'}, 401
        except EmailSenhaInvalidosException as e:
            return {'error': 'email ou senha inválidos'}, 401
        except Exception as e:
            print(traceback.format_exc())
            return 'Erro interno do servidor', 500

class UserInfoPresenter(Resource):
    def get(self):
        data = {
            'token': request.headers.get('token')
        }
        return controlador_conta.getUserInfo(data)

@app.route('/')
def greetings():
    return 'Greetings from contaservice!'

api.add_resource(LoginPresenter, '/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
