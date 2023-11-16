from abc import abstractmethod


class ElementAbstract:
    @abstractmethod
    def getString(self):
        pass
    
    @abstractmethod
    def generate(self):
        pass