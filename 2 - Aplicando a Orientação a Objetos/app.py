"""IMPORTS"""
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa


'''RESTAURANTES'''
restaurante_japones = Restaurante('Japa', 'Japonesa')

'''ATIVAÇÃO'''
restaurante_japones.alternar_estado()

'''AVALIAÇÕES'''
restaurante_japones.receber_avaliacao('Gabriel', 5)
restaurante_japones.receber_avaliacao('Lais', 4)
restaurante_japones.receber_avaliacao('Emy', 2)

'''PRODUTOS'''
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_paozinho = Prato('Paozinho', 2, 'O melhor pão da cidade')
sobremesa01 = Sobremesa('Pudim', 22, 'Sobremesa', 'médio')

'''APLICANDO DESCONTOS NOS PRODUTOS'''
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

'''ADICIONAR PRODUTOS NOS RESTAURANTES'''
restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prato_paozinho)
restaurante_japones.adicionar_no_cardapio(sobremesa01)


"""Define a função principal"""
def main():
    # Restaurante.listar_restaurantes()
    restaurante_japones.exibir_cardapio

if __name__ == '__main__':
    main()