import os

restaurantes = [{'nome': 'Daniel San Prime', 'categoria': 'Sushi', 'ativo': False},
                {'nome': 'McDonalds', 'categoria': 'Hamburger', 'ativo': True},
                {'nome': 'Famiglia Petri', 'categoria': 'Italiana', 'ativo': False}
]

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")
    
def exibir_opcoes():
    ''' Esta função apresenta ao usuário as opções disponíveis no menu.'''
    
    print('1 - Cadastrar restaurantes')
    print('2 - Listar restaurantes')
    print('3 - Alternar estado do restaurantes')
    print('4 - Sair\n')

def escolher_opcao():
    '''
    Esta função retorna a opção escolhida pelo usuário.

    Entradas:
    - Escolha da opção

    Saídas:
    - Cadastrar restaurantes
    - Listar restaurantes
    - Finalizar aplicativo
    - Opção inválida
    '''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def opcao_invalida():
    '''Esta função exibe ao usuário a mensagem de opção inválida e, em seguida,
    chama uma função interna para retorná-lo ao menu principal.'''
    
    print('Opcão invaldia, Tente novamente!!!\n')
    voltar_menu_principal() 

def voltar_menu_principal():
    '''Esta função permite que o usuário retorne ao menu principal.

    Entradas:
    - Digite uma tecla para voltar
    '''
    
    input('\nDigite um tecla para voltar ao menu principal ')
    main() 
     
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(f'{linha}\n')        

def cadastrar_restaurante():
    '''Esta função realiza o cadastro de um novo restaurante.

    Entradas:
    - Nome do restaurante
    - Categoria

    Saídas:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    
    exibir_subtitulo('Cadastro de novos resturantes')
    nome_do_resturante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_resturante}:  ')
    dados_do_restaurante = {'nome':nome_do_resturante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_resturante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()
   
def listar_restaurante(): 
    ''' Esta função apresenta ao usuário a lista de restaurantes cadastrados.

    Saídas:
    - Nome do restaurante
    - Categoria
    - Status: Ativado ou Desativado
    '''
     
    exibir_subtitulo('Lista de restaurantes')
    print(f'Nome do restaurante'.ljust(23), 'Categoria'.ljust(22), 'Ativado')
    print('-' * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()    
    
def alternar_estado_restaurante():
    '''Esta função altera o estado do restaurante.

    Saídas:
    - "O restaurante foi ativado com sucesso" se o estado for inativo (False)
    - "O restaurante foi desativado com sucesso" se o estado for ativo (True)
    '''
    
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:  ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] == True else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!!')   
    voltar_menu_principal()
    
def finalizar_app():
    ''' Esta função chama uma função interna para exibir o subtítulo da página.

    Entrada:
    - Subtítulo da página a ser exibido ao usuário
    '''
    
    exibir_subtitulo('Finalizando o app') 
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()