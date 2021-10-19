from typing import Annotated

from Ferramenta import Ferramenta

class Furadeira(Ferramenta):

    def cadastrar(self, nome, tensao, preco, potencia):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
        self._potencia = potencia

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor 

    @property
    def tensao(self):
        return self._tensao

    @tensao.setter
    def tensao(self, valor):
        self._tensao = valor
    
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    # Fracamente protegido
    def __potencia(self, valor):
        self._potencia = valor

    def getInformacoes(self):
        return  '\nNome: '+ self._nome + '\nTensão: ' + self.tensao + 'v\nPreço: R$ ' + str(self.preco)+'\nPotência: '+str(self._potencia)+' watts\n'



