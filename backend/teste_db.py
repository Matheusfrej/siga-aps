from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
# Import the classes you want to test
from entidades import ContaAluno, ContaProfessor, Cadeira, Matricula, Base, OfertaCadeira
from sqlalchemy import select

from utils import CadeiraSerializer, ContaSerializer

import json

# Create a database engine
engine = create_engine('sqlite:///sigab.db')

# Create the database tables
Base.metadata.create_all(engine)

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

def test_create_and_save():
    # # Create instances of the classes
    conta_prof = ContaProfessor(email="baws@cin.ufpe.br", cpf="123456789", nome="John Doe",
                                data_nascimento=date(1990, 1, 1), ano_entrada="2022",
                                siape="12345", formacao="Ph.D")

    conta_aluno = ContaAluno(curso='CC', email="fgm3@cin.ufpe.br", cpf="987654321", nome="Bruna",
                             data_nascimento=date(2001, 7, 15), ano_entrada="2020.1")

    horario1 = {'seg': [8, 9], 'qua': [10, 11]}
    horario2 = {'seg': [10, 11], 'qua': [8, 9]}
    horario3 = {'ter': [8, 9], 'qui': [10, 11]}
    horario4 = {'ter': [10, 11], 'qui': [8, 9]}

    cadeira1 = Cadeira(nome="Programação Concorrente Distribuída")
    cadeira2 = Cadeira(nome="Análise e Projetos de Sistemas")
    cadeira3 = Cadeira(nome="Sistemas de Informação")
    cadeira4 = Cadeira(nome="Análise e Projetos de Sistemas")

    oferta_cadeira1 = OfertaCadeira(horario=horario1, centro_universitario='CIn', periodo='2023.2', professor=conta_prof, cadeira=cadeira1)
    oferta_cadeira2 = OfertaCadeira(horario=horario2, centro_universitario='CIn', periodo='2023.2', professor=conta_prof, cadeira=cadeira2)
    oferta_cadeira3 = OfertaCadeira(horario=horario3, centro_universitario='CIn', periodo='2023.2', professor=conta_prof, cadeira=cadeira3)
    oferta_cadeira4 = OfertaCadeira(horario=horario4, centro_universitario='CIn', periodo='2023.2', professor=conta_prof, cadeira=cadeira4)

    matricula = Matricula(periodo="2023.2", aluno=conta_aluno, cadeiras=[])

    # Associate the objects with their relationships
    conta_prof.ofertas_cadeiras.append(oferta_cadeira1)
    conta_prof.ofertas_cadeiras.append(oferta_cadeira2)
    conta_prof.ofertas_cadeiras.append(oferta_cadeira3)
    conta_prof.ofertas_cadeiras.append(oferta_cadeira4)

    conta_aluno.matriculas.append(matricula)
    matricula.cadeiras.append(oferta_cadeira1)
    matricula.cadeiras.append(oferta_cadeira2)
    matricula.cadeiras.append(oferta_cadeira3)
    matricula.cadeiras.append(oferta_cadeira4)


    # Add the instances to the session and commit
    session.add_all([
        conta_prof,
        conta_aluno,
        matricula,
        cadeira1,
        cadeira2,
        cadeira3,
        cadeira4,
        oferta_cadeira1,
        oferta_cadeira2,
        oferta_cadeira3,
        oferta_cadeira4])
    session.commit()

    # Print the objects to verify they are saved in the database
    print("ContaProfessor:", conta_prof.nome)
    print("ContaAluno:", conta_aluno.nome)
    for i in range(4):
        print(f"Cadeira {i+1}:", matricula.cadeiras[i].cadeira.nome)

    print("Matricula:", matricula.periodo)
    cadeira = session.query(OfertaCadeira).first()
    print(cadeira.horario)
    session.commit()
if __name__ == "__main__":
    test_create_and_save()