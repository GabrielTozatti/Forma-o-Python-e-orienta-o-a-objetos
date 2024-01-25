from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        
    def __str__(self):
        return f'Nome: {self._nome} | Preço: {self._preco} | Tipo: {self.tipo} | Tamanho: {self.tamanho}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.03)