from typing import Annotated
from Ferramenta import Ferramenta

class Lixadeira(Ferramenta) :
        
    def cadastrar(self, nome, tensao, preco, rotacoes):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
        self.____rotacoes = rotacoes

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
    def rotacoes(self):
        return self._rotacoes

    @rotacoes.setter
    def ____rotacoes(self, valor):
        self._rotacoes = valor

    def getInformacoes(self):
        return  '\nNome: '+ self._nome + '\nTensão: ' + self.tensao + 'v\nPreço: R$ ' + str(self.preco)+'\nRotações: '+str(self._rotacoes)+' p/m\n'        