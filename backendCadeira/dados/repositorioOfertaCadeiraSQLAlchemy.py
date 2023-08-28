
import datetime
from .iRepositorioOfertaCadeira import IRepositorioOfertaCadeira
from entidades import OfertaCadeira
from entidades import Cadeira
from sqlalchemy.orm import joinedload


class RepositorioOfertaCadeiraSQLAlchemy(IRepositorioOfertaCadeira):
    def __init__(self, Session):
        self.Session = Session

    def create(self, data):
        with self.Session() as session:
            nova_oferta_cadeira = OfertaCadeira(**data)
            session.add(nova_oferta_cadeira)
            session.commit()
            nova_oferta_cadeira = session.query(
                OfertaCadeira).filter_by(
                    id=nova_oferta_cadeira.id).options(
                        joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.corequisitos),
                        joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.prerequisitos),
                        joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.equivalencias)).first()
            print(nova_oferta_cadeira.cadeira)
            return nova_oferta_cadeira

    def read(self, id):
        with self.Session() as session:
            return session.query(OfertaCadeira).filter_by(id=id).options(
                joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.corequisitos),
                joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.prerequisitos),
                joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.equivalencias)
            ).first()

    def update(self, id, data):
        with self.Session() as session:
            oferta_cadeira = session.query(OfertaCadeira).filter_by(id=id).options(joinedload(OfertaCadeira.cadeira)).first()
            if oferta_cadeira:
                if 'horario' in data:
                    oferta_cadeira.horario = data.get('horario')
                if 'plano_ensino' in data:
                    oferta_cadeira.plano_ensino = data.get('plano_ensino')
                if 'centro_universitario' in data:
                    oferta_cadeira.centro_universitario = data.get('centro_universitario')
                if 'professor_id' in data:
                    oferta_cadeira.professor_id = data.get('professor_id')
                if 'professor' in data:
                    oferta_cadeira.professor_id = data.get('professor')
                if 'cadeira_id' in data:
                    oferta_cadeira.cadeira_id = data.get('cadeira_id')
                if 'cadeira' in data:
                    oferta_cadeira.cadeira_id = data.get('cadeira')
                if 'periodo' in data:
                    oferta_cadeira.periodo = data.get('periodo')
                session.commit()
                oferta_cadeira = session.query(OfertaCadeira).filter_by(id=id).options(joinedload(OfertaCadeira.cadeira)).first()
                return oferta_cadeira
            else:
                #TODO lembrar de levantar um erro caso a cadeira não exista
                pass

    def delete(self, id):
        print(id)
        with self.Session() as session:
            oferta_cadeira = session.query(
                OfertaCadeira).filter_by(id=id).first()
            if oferta_cadeira:
                session.delete(oferta_cadeira)
                session.commit()
                return True
            else:
                # TODO fazer um raise
                return False

    def get_by_professor(self, professor_id):
        with self.Session() as session:
            ofertas_cadeiras = session.query(
                OfertaCadeira).options(joinedload(OfertaCadeira.cadeira)).filter_by(professor_id=int(professor_id))
            return list(ofertas_cadeiras)

    def get_current_by_professor(self, professor_id):
        with self.Session() as session:
            curr_date = datetime.now()
            year = curr_date.year
            month = curr_date.month
            periodo = f'{year}.{1 if month <= 6 else 2}'
            ofertas_cadeiras = session.query(
                OfertaCadeira).options(joinedload(OfertaCadeira.cadeira)
            ).filter_by(professor_id=int(professor_id), periodo=periodo)
            return list(ofertas_cadeiras)
        
    def get_by_periodo(self):
        with self.Session() as session:
            curr_date = datetime.now()
            year = curr_date.year
            month = curr_date.month
            periodo = f'{year}.{1 if month <= 6 else 2}'
            ofertas_cadeiras = session.query(
                OfertaCadeira).options(joinedload(OfertaCadeira.cadeira)).filter_by(periodo=periodo)
            return list(ofertas_cadeiras)

    def read_id_in_list(self, id_list):
        with self.Session() as session:
            return {
                cadeira.id: cadeira
                    for cadeira in
                        session.query(OfertaCadeira).options(
                            joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.corequisitos),
                            joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.prerequisitos),
                            joinedload(OfertaCadeira.cadeira).joinedload(Cadeira.equivalencias)
                        ).filter(OfertaCadeira.id.in_(id_list)).all()}
