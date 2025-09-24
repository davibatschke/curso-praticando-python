import os
def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Bem-Vindo ao Conversor de Temperaturas de Terminal!')
        print('Convertemos Celsius, Fahrenheit e também Kelvin.')
        print('---------------------------------------------------')

        opcoes_menu = {'1': 'Converter: Celsius -> Fahrenheit',
                    '2': 'Converter: Celsius -> Kelvin',
                    '3': 'Converter: Fahrenheit -> Celsius',
                    '4': 'Converter: Fahrenheit -> Kelvin',
                    '5': 'Converter: Kelvin -> Celsius',
                    '6': 'Converter: Kelvin -> Fahrenheit',
                    '7': 'Encerrar o Conversor de Terminal'
                    }
        for chave, valor in opcoes_menu.items():
            print(f'{chave} - {valor}')
        escolhendo = input('\nQual das Opções acima Deseja? ')
        if escolhendo == '7':
            print('Encerrando o Sistema... Tchau!')
            break
        try:
            valor_conversao = float(input('Digite o Valor que deseja Converter: '))
            resultado, unidade = convertendo_temperaturas(escolhendo, valor_conversao)
            if resultado is not None:
                print(f'O Valor convertido é: {resultado:.1f} {unidade}')
            else:
                print('Opção que você escolheu é Inválida.')
        except ValueError:
            print('Entrada Inválida, Digite um Número Válido.')
        input('Digite Qualquer Tecla para Continuar... ')

def convertendo_temperaturas(escolhendo, valor_conversao):
    if escolhendo == '1':
        return (valor_conversao * 9/5) + 32, 'Fahrenheit'
    elif escolhendo == '2':
        return (valor_conversao + 273.15), 'Kelvin'
    elif escolhendo == '3':
        return (valor_conversao - 32) * 5/9, 'Celsius'
    elif escolhendo == '4':
        return (valor_conversao - 32) * 5/9 + 273.15, 'Kelvin'
    elif escolhendo == '5':
        return (valor_conversao - 273.15), 'Celsius'
    elif escolhendo == '6':
        return (valor_conversao * 9/5) - 459.67, 'Fahrenheit'
    else:
        return None, None

menu_principal()