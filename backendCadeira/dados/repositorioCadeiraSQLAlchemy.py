from .iRepositorioCadeira import IRepositorioCadeira
from entidades import Cadeira
from sqlalchemy.orm import joinedload

class RepositorioCadeiraSQLAlchemy(IRepositorioCadeira):
    def __init__(self, Session):
        self.Session = Session

    def create(self, data):
        with self.Session() as session:
            equivalencias = data.pop('equivalencias', None)
            prerequisitos = data.pop('prerequisitos', None)
            corequisitos = data.pop('corequisitos', None)
            nova_cadeira = Cadeira(**data)
            session.add(nova_cadeira)
            if prerequisitos:
                lista_ids = prerequisitos
                novos_prerequisitos = list(session.query(Cadeira).filter(Cadeira.id.in_(lista_ids)).all())
                nova_cadeira.prerequisitos.clear()
                nova_cadeira.prerequisitos.extend(novos_prerequisitos)
            if corequisitos:
                lista_ids = corequisitos
                novos_corequisitos = list(session.query(Cadeira).filter(Cadeira.id.in_(lista_ids)).all())
                nova_cadeira.corequisitos.clear()
                nova_cadeira.corequisitos.extend(novos_corequisitos)
            if equivalencias:
                lista_ids = equivalencias
                novos_equivalencias = list(session.query(Cadeira).filter(Cadeira.id.in_(lista_ids)).all())
                nova_cadeira.equivalencias.clear()
                nova_cadeira.equivalencias.extend(novos_equivalencias)
            session.commit()
            nova_cadeira = session.query(Cadeira).filter_by(
                id=nova_cadeira.id).options(
                    joinedload(Cadeira.equivalencias),
                    joinedload(Cadeira.prerequisitos),
                    joinedload(Cadeira.corequisitos)).first()
            return nova_cadeira

    def read(self, id):
        with self.Session() as session:
            return session.query(Cadeira).filter_by(id=id).options(
                    joinedload(Cadeira.equivalencias),
                    joinedload(Cadeira.prerequisitos),
                    joinedload(Cadeira.corequisitos)).first()

    def update(self, id, data):
        with self.Session() as session:
            cadeira = session.query(Cadeira).filter_by(
                id=id).first()
            if cadeira:
                if 'nome' in data:
                    cadeira.nome = data.get('nome')
                if 'ementa' in data:
                    cadeira.ementa = data.get('ementa')
                if 'prerequisitos' in data:
                    lista_ids = data.get('prerequisitos')
                    novos_prerequisitos = list(session.query(Cadeira).filter(Cadeira.id.in_(lista_ids)).all())
                    cadeira.prerequisitos.clear()
                    cadeira.prerequisitos.extend(novos_prerequisitos)
                if 'corequisitos' in data:
                    lista_ids = data.get('corequisitos')
                    novos_corequisitos = list(session.query(Cadeira).filter(Cadeira.id.in_(lista_ids)).all())
                    cadeira.corequisitos.clear()
                    cadeira.corequisitos.extend(novos_corequisitos)
                if 'equivalencias' in data:
                    lista_ids = data.get('equivalencias')
                    novos_equivalencias = list(session.query(Cadeira).filter(Cadeira.id.in_(lista_ids)).all())
                    cadeira.equivalencias.clear()
                    cadeira.equivalencias.extend(novos_equivalencias)
                session.commit()
                cadeira = session.query(Cadeira).filter_by(
                    id=id).options(
                        joinedload(Cadeira.equivalencias),
                        joinedload(Cadeira.prerequisitos),
                        joinedload(Cadeira.corequisitos)).first()
                cadeira.prerequisitos, cadeira.corequisitos, cadeira.equivalencias
                return cadeira
            else:
                #TODO lembrar de levantar um erro caso a cadeira não exista
                pass

    def delete(self, id):
        with self.Session() as session:
            cadeira = session.query(Cadeira).filter_by(id=id).first()
            if cadeira:
                session.delete(cadeira)
                session.commit()
                return True
            else:
                # TODO fazer um raise
                return False

    def read_id_in_list(self, id_list):
        with self.Session() as session:
            return {cadeira.id: cadeira for cadeira in session.query(Cadeira).options(
                        joinedload(Cadeira.equivalencias),
                        joinedload(Cadeira.prerequisitos),
                        joinedload(Cadeira.corequisitos)).filter(Cadeira.id.in_(id_list)).all()}
