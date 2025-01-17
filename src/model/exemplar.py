'''
modelo Exemplar
'''

from src.model.base import Base


class Exemplar(Base):
    '''
    classe Exemplar
    '''

    def __init__(
            self,
            identificacao: int,
            numero_de_renovacoes: int = 0,
    ) -> None:
        '''
        Inicialização
        '''
        super().__init__(identificacao)
        self.numero_de_renovacoes: int = numero_de_renovacoes

    def acrescentar_numero_renovacoes(self) -> None:
        '''
        Acrescenta +=1 na renovacao
        '''
        self.numero_de_renovacoes += 1

    def pode_renovar(self, renovacoes_permitidas: int) -> bool:
        '''
        Renova se puder.
        retorna False ou True
        '''
        return self.numero_de_renovacoes < renovacoes_permitidas

    def __str__(self) -> str:
        return f"Exemplar ID: {self.identificacao}, Renovações: {self.numero_de_renovacoes}"
