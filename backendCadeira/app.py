from flask import Flask, request

from flask_cors import CORS
from flask_restful import Api, reqparse

from presenters import *

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('ids', type=int, action='append', required=True)

api.add_resource(CadastrarCadeiraPresenter, '/cadastrar-cadeira')
api.add_resource(EditarCadeiraPresenter, '/editar-cadeira')
api.add_resource(DeletarCadeiraPresenter, '/deletar-cadeira')
api.add_resource(CadastrarOfertaCadeiraPresenter, '/cadastrar-oferta-cadeira')
api.add_resource(EditarOfertaCadeiraPresenter, '/editar-oferta-cadeira')
api.add_resource(DeletarOfertaCadeiraPresenter, '/deletar-oferta-cadeira')
api.add_resource(GetOfertasCadeirasProfessorPresenter, '/get-cadeiras-professor')
api.add_resource(GetOfertasCadeirasPeriodoPresenter, '/get-cadeiras-periodo')
api.add_resource(GetOfertaCadeiraById, '/get-oferta-cadeira/<int:oferta_id>')
api.add_resource(GetOfertaCadeiraListById, '/get-oferta-cadeira-list')

@app.route('/')
def greetings():
    return 'Greetings from cadeiraservice!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
