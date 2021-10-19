from abc import ABC, ABCMeta, abstractmethod, abstractproperty

class Ferramenta(metaclass=ABCMeta):

    @property
    @abstractproperty
    def nome(self):
        pass

    @nome.setter
    def nome(self, valor):
        pass    
    
    @property
    @abstractproperty
    def tensao(self):
        pass

    @tensao.setter
    def tensao(self, valor):
        pass

    @property
    @abstractproperty
    def preco(self):
        pass

    @preco.setter
    def preco(self, valor):
        pass
    
    @abstractmethod
    def getInformacoes(self):
        pass

    @abstractmethod
    def cadastrar(self, nome, tensao, preco):
        pass

