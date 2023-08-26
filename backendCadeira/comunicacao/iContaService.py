from abc import ABC, abstractmethod

class IContaService(ABC):
    @abstractmethod
    def get_user_info(self, data):
        pass
