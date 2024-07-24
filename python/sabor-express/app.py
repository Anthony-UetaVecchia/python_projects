import os

restaurantes = [{"nome":"Diavolo's Pizzaria", "categoria":"Italiana", "ativo":False},
                {"nome":"Giorno's Dream Pizzaria", "categoria":"Italiana", "ativo":True},
                {"nome":"Dz7 Burger", "categoria":"Hamburguer", "ativo":True}]


def exibir_nome_programa():
    '''
        Exibe o nome estilizado do programa na tela
    '''
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    '''
        Exibe as opções do menu principal
    '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''
        Exibe mensagem de finalização do aplicativo
    '''
    exibir_subtitulo('Finalizando o App')

def voltar_menu_principal():
    '''
        Solicita uma tecla para voltar ao menu principal 
    
        Outputs:
        - Retorna ao menu principal 
    '''
    input('\n Digite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''
        Exibe um subtítulo estilizado na tela 
    
        Inputs:
        - texto(str): O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 1)
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida():
    '''
        Exibe a mensagem de Opção Inválida e volta ao menu principal

        Outputs:
        - Retorna ao menu principal
    '''
    print('Opção Inválida!\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    '''
        Essa função é responsável por cadastrar um novo restaurante 
    
        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do resteurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    '''
        Lista os restaurantes presentes na lista 
    
        Outputs:
        - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Lista de Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(32)} | {'Categoria'.ljust(20)} | {'Status'}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(30)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()

def alternar_estado_restaurante():
    '''
        Altera o estado ativo/desativado de um restaurante 
    
        Outputs:
        - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante  = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu_principal()

def escolher_opcao():
    '''
        Solicita e executa a opção escolhida pelo usuário 
    
        Outputs:
        - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
        Função principal que inicia o programa
    '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()