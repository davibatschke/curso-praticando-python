import random
def verificar_vencedor(opcao_usuario, opcao_computador):
    if (opcao_usuario == 'Pedra' and opcao_computador == 'Pedra' or 
        opcao_usuario == 'Papel' and opcao_computador == 'Papel' or
        opcao_usuario == 'Tesoura' and opcao_computador == 'Tesoura'):
        return f'Houve um Empate! Computador escolheu: {opcao_computador}'

    if (opcao_usuario == 'Papel' and opcao_computador == 'Pedra' or
        opcao_usuario == 'Tesoura' and opcao_computador == 'Papel' or
        opcao_usuario == 'Pedra' and opcao_computador == 'Tesoura'):
        return f'Você Ganhou! Computador escolheu: {opcao_computador}'
    
    if (opcao_usuario == 'Pedra' and opcao_computador == 'Papel' or
        opcao_usuario == 'Papel' and opcao_computador == 'Tesoura' or
        opcao_usuario == 'Tesoura' and opcao_computador == 'Pedra'):
        return f'Computador Ganhou! Computador escolheu: {opcao_computador}'

jogadas_disponiveis = ['Papel', 'Pedra', 'Tesoura']
opcao_usuario = input('Faça a Sua Escolha (Pedra ou Papel ou Tesoura): ').title()
opcao_computador = random.choice(jogadas_disponiveis)
if opcao_usuario not in jogadas_disponiveis:
    print('A Jogada que você escolheu é Inválida.')
else:
    print(verificar_vencedor(opcao_usuario, opcao_computador))