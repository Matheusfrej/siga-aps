
from .iRepositorioOfertaCadeira import IRepositorioOfertaCadeira
from entidades import OfertaCadeira
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
                    id=nova_oferta_cadeira.id).options(joinedload('*')).first()
            return nova_oferta_cadeira

    def read(self, id):
        with self.Session() as session:
            return session.query(OfertaCadeira).filter_by(id=id).first()

    def update(self, id, data):
        with self.Session() as session:
            oferta_cadeira = session.query(OfertaCadeira).filter_by(id=id).first()
            if oferta_cadeira:
                for key, value in data.items():
                    setattr(oferta_cadeira, key, value)
                session.commit()
                pass
            else:
                #TODO lembrar de levantar um erro caso a cadeira não exista
                pass

    def delete(self, id):
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
                OfertaCadeira).options(joinedload(OfertaCadeira.cadeira)).filter_by(professor_id=professor_id)
            return list(ofertas_cadeiras)
        
    def get_by_periodo(self, periodo):
        with self.Session() as session:
            ofertas_cadeiras = session.query(
                OfertaCadeira).options(joinedload(OfertaCadeira.cadeira)).filter_by(periodo=periodo)
            return list(ofertas_cadeiras)

    def read_id_in_list(self, id_list):
        with self.Session() as session:
            return {
                cadeira.id: cadeira
                    for cadeira in
                        session.query(OfertaCadeira).filter(OfertaCadeira.id.in_(id_list)).all()}
