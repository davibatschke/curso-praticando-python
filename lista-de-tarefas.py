lista_de_tarefas = []
import os

def menu_principal():
    while True:
        limpar_visualizacao()
        print('Bem-Vindo a sua Lista de Tarefas de Terminal')
        print('--------------------------------------------')

        opcoes_menu = {'1': 'Adicionar uma Tarefa',
                    '2': 'Remover uma Tarefa',
                    '3': 'Exibir a Lista de Tarefa',
                    '4': 'Encerrar o Programa'}
        for chave, valor in opcoes_menu.items():
            print(f'{chave} - {valor}')

        escolha = input('\nQual das Opções Deseja? ')
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            remover_tarefa()
        elif escolha == '3':
            exibir_lista_tarefa()
        elif escolha == '4':
            print('Encerrando o Sistema...')
            break
        else:
            print('A Opção que você escolheu é inválida.')
        input('Aperte qualquer tecla para Continuar...')

def adicionar_tarefa():
    limpar_visualizacao()
    tarefa = input('O que deseja Adicionar como Tarefa? ')
    print(f'Tarefa: {tarefa} foi Adicionada a Lista!')
    lista_de_tarefas.append(tarefa)
    retorna_menu_principal()

def remover_tarefa():
    limpar_visualizacao()
    if not lista_de_tarefas:
        print('A lista está vazia, volte para Adicionar uma Tarefa!')
        retorna_menu_principal()

    for num, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f'{num} - {tarefa}')
    escolha = input('Digite o Número da Tarefa que Queira Remover: ')
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(lista_de_tarefas):
            removida = lista_de_tarefas.pop(indice)
            print(f'A Tarefa: "{removida}" foi Removida da Lista.')
        else:
            print('O Número da Tarefa que você Escolheu é Inválido.')
    else:
        print('Parece que um Erro Aconteceu : ERRO De Entrada.')
    retorna_menu_principal()

def exibir_lista_tarefa():
    limpar_visualizacao()
    if not lista_de_tarefas:
        print('A lista está vazia, volte para Adicionar uma Tarefa!')
        print('\nPara retornar ao Menu Principal')
        input('Basta Pressionar Qualquer Tecla.')
        menu_principal()

    for num, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f'{num} - {tarefa}')
    retorna_menu_principal()

def retorna_menu_principal():
    print('\nPara retornar ao Menu Principal')
    input('Basta Pressionar Qualquer Tecla.')
    menu_principal()

def limpar_visualizacao():
    os.system('cls' if os.name == 'nt' else 'clear')

menu_principal()