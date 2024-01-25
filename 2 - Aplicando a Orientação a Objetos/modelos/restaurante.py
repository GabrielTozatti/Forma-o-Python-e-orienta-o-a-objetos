from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.
        
        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A Categoria do restaurante.
        """
        self._nome = nome.title()    
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'Nome: {self._nome}, Categoria: {self._categoria}, Ativado: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'\n{'ID'.ljust(25)} | {'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} {'Status'}')
        c = 1
        for restaurante in cls.restaurantes:
            print(f'{str(c).ljust(25)} | {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} {restaurante.ativo}')
            c+=1
        print(f'\n')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return f'✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if nota >= 0 and nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property  
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return f'-'
        quantidade_de_notas = len(self._avaliacao)
        somas_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media =  round(somas_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): # Verifica se item é uma instância da class ItemCardapio ou se é um class Derivada de ItemCardapio
            self._cardapio.append(item)
    
    @property 
    def exibir_cardapio(self):
        """
        Exibe o cardápio do restaurante, mostrando informações detalhadas sobre cada item, como nome, preço e descrição.
        
        Parâmetros:
        - self: A instância do objeto Restaurante.

        O método percorre o cardápio do restaurante e exibe as informações de cada item.
        """
        print(f'\nCardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'): # Verifica se item tem algum atributo chamado descricao
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tipo') and hasattr(item, 'tamanho'):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tipo: {item.tipo} | Tamanho: {item.tamanho}'
                print(mensagem)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)             
        print(f'\n')