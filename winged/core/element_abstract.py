from abc import abstractmethod


class ElementAbstract:
    @abstractmethod
    def get_string(self):
        pass

    @abstractmethod
    def generate(self):
        pass
