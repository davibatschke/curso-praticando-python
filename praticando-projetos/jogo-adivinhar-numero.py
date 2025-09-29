import random
def jogo_adivinhar_numero():
    numero_escolhido = random.randrange(1, 100)
    while True:
        try:
            palpite_jogador = int(input('Escolha um Valor (Entre 1 a 100): '))
            if not 1 <= palpite_jogador <= 100:
                raise ValueError('ERRO: O número escolhido está fora do solicitado.')
 
            if palpite_jogador < numero_escolhido:
                print('Você escolheu um Valor Muito Baixo!')
            elif palpite_jogador > numero_escolhido:
                print('Você escolheu um Valor Muito Alto!')
            else:
                print(f'Parabéns! Você acertou o número: {numero_escolhido}.')
                break
        except ValueError as e:
            print(f'Entrada inválida: {e}')

jogo_adivinhar_numero()