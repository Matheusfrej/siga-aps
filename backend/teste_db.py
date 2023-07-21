from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
# Import the classes you want to test
from entidades import ContaAluno, ContaProfessor, Cadeira, Matricula, Base, ContaBase
from sqlalchemy import select

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
    # Create instances of the classes
    conta_prof = ContaProfessor(email="john@example.com", cpf="123456789", nome="John Doe",
                                data_nascimento=date(1990, 1, 1), ano_entrada="2022", senha="password",
                                siape="12345", formacao="Ph.D")

    conta_aluno = ContaAluno(curso='CC', email="baws@cin.ufpe.br", cpf="987654321", nome="Alice",
                             data_nascimento=date(1995, 5, 5), ano_entrada="2021", senha="12345")

    horario = {'seg': [8, 9], 'ter': [10, 11]}
    cadeira = Cadeira(nome="Database Systems", horario=horario, centro_universitario="School of CS", professor=conta_prof)
    matricula = Matricula(periodo="2023.2", aluno=conta_aluno, cadeiras=[cadeira])

    # Associate the objects with their relationships
    conta_prof.cadeiras.append(cadeira)

    conta_aluno.matriculas.append(matricula)
    matricula.cadeiras.append(cadeira)

    # Add the instances to the session and commit
    session.add_all([conta_prof, conta_aluno, cadeira])
    session.commit()

    # Print the objects to verify they are saved in the database
    print("ContaProfessor:", conta_prof)
    print("ContaAluno:", conta_aluno)
    print("Cadeira:", cadeira)
    print("Matricula:", matricula)
    cadeira = session.query(Cadeira).first()
    print(cadeira.horario)
    session.commit()
if __name__ == "__main__":
    test_create_and_save()