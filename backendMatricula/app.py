from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from presenters import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(VerHorarioPresenter, '/ver-horario/<int:aluno_id>')
api.add_resource(MatriculaPresenter, '/fazer-matricula')
api.add_resource(EditarMatriculaPresenter, '/editar-matricula/<int:matricula_id>')
api.add_resource(DeletarMatriculaPresenter, '/deletar-matricula/<int:matricula_id>')
api.add_resource(GetMatriculaPeriodoPresenter, '/get-matricula/<int:aluno_id>')
api.add_resource(GetMatriculasAlunoPresenter, '/get-matriculas-aluno/<int:aluno_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)