class Avaliacao:
    def __init__(self, cliente, nota):
        """
        Inicializa uma instância de Avaliação.
        
        Parâmetros:
        - cliente (str): O nome do cliente.
        - nota (int): Nota do cliente
        """
        self._cliente = cliente
        self._nota = nota