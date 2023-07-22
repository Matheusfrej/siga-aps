from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
# Import the classes you want to test
from entidades import ContaAluno, ContaProfessor, Cadeira, Matricula, Base, ContaBase
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
    # conta_prof = ContaProfessor(email="baws@cin.ufpe.br", cpf="123456789", nome="John Doe",
    #                             data_nascimento=date(1990, 1, 1), ano_entrada="2022",
    #                             siape="12345", formacao="Ph.D")

    # conta_aluno = ContaAluno(curso='CC', email="fgm3@cin.ufpe.br", cpf="987654321", nome="Alice",
    #                          data_nascimento=date(1995, 5, 5), ano_entrada="2021")

    # horario = {'seg': [8, 9], 'ter': [10, 11]}
    # cadeira_1 = Cadeira(nome="A", horario=horario, centro_universitario="School of CS", professor=conta_prof)
    # cadeira_2 = Cadeira(nome="B", horario=horario, centro_universitario="School of CS", professor=conta_prof, prerequisitos=[cadeira_1])
    # cadeira_3 = Cadeira(nome="C", horario=horario, centro_universitario="School of CS", professor=conta_prof, corequisitos=[cadeira_2])
    # cadeira_4 = Cadeira(nome="D", horario=horario, centro_universitario="School of CS", professor=conta_prof, equivalencias=[cadeira_1, cadeira_2])
    # matricula = Matricula(periodo="2023.2", aluno=conta_aluno, cadeiras=[cadeira_1, cadeira_2, cadeira_3, cadeira_4])

    # # Associate the objects with their relationships
    # conta_prof.cadeiras.append(cadeira_1)
    # conta_prof.cadeiras.append(cadeira_2)
    # conta_prof.cadeiras.append(cadeira_3)
    # conta_prof.cadeiras.append(cadeira_4)

    # conta_aluno.matriculas.append(matricula)
    # matricula.cadeiras.append(cadeira_1)
    # matricula.cadeiras.append(cadeira_2)
    # matricula.cadeiras.append(cadeira_3)
    # matricula.cadeiras.append(cadeira_4)

    # # Add the instances to the session and commit
    # session.add_all([conta_prof, conta_aluno, cadeira_1, cadeira_2, cadeira_3, cadeira_4])
    # session.commit()

    # # Print the objects to verify they are saved in the database
    # print("ContaProfessor:", conta_prof)
    # print("ContaAluno:", conta_aluno)
    # print("Cadeira:", cadeira_1)
    # print("Matricula:", matricula)

    for cadeira in session.query(Cadeira).all():
        print(CadeiraSerializer(cadeira).get_data())
        professor = session.query(ContaProfessor).first()
        print(ContaSerializer(professor).get_data())
        print()
        print('##########################################')
        print()

if __name__ == "__main__":
    test_create_and_save()