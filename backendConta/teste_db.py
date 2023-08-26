from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
# Import the classes you want to test
from entidades import ContaAluno, ContaProfessor, Base

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
    conta_prof = ContaProfessor(email='baws@cin.ufpe.br', cpf='123456789', nome='John Doe',
                                data_nascimento=date(1990, 1, 1), ano_entrada='2022',
                                siape='12345', formacao='Ph.D')

    conta_aluno = ContaAluno(curso='CC', email='fgm3@cin.ufpe.br', cpf='987654321', nome='Bruna',
                             data_nascimento=date(2001, 7, 15), ano_entrada='2020.1')

    # Add the instances to the session and commit
    session.add_all([
        conta_prof,
        conta_aluno])
    session.commit()

if __name__ == '__main__':
    test_create_and_save()