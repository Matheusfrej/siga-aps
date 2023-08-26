from abc import ABC, abstractmethod


class ICadeiraService(ABC):
    @abstractmethod
    def get_ofertas_cadeiras_periodo(self, data):
        pass
    
    @abstractmethod
    def get_oferta_cadeira_by_id(self, data):
        pass

