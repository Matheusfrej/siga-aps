from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from presenters import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(LoginPresenter, '/login')
api.add_resource(UserInfoPresenter, '/get-user-info')
api.add_resource(CadastrarCadeiraPresenter, '/cadastrar-cadeira')
api.add_resource(EditarCadeiraPresenter, '/editar-cadeira')
api.add_resource(DeletarCadeiraPresenter, '/deletar-cadeira')
api.add_resource(CadastrarOfertaCadeiraPresenter, '/cadastrar-oferta-cadeira')
api.add_resource(EditarOfertaCadeiraPresenter, '/editar-oferta-cadeira')
api.add_resource(DeletarOfertaCadeiraPresenter, '/deletar-oferta-cadeira')
api.add_resource(GetOfertasCadeirasProfessorPresenter, '/get-cadeiras-professor')
api.add_resource(GetOfertasCadeirasPeriodoPresenter, '/get-cadeiras-periodo')
api.add_resource(VerHorarioPresenter, '/ver-horario')
api.add_resource(MatriculaPresenter, '/fazer-matricula')

if __name__ == '__main__':
    app.run(debug=True)