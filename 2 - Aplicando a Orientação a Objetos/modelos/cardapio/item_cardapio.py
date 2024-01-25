from abc import ABC, abstractmethod # Importando abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome =  nome
        self._preco = preco
    
    @abstractmethod # Significa que todas as classes derivadas precisão ter esse metodo 
    def aplicar_desconto(self):
        pass