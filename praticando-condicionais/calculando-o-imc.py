peso = float(input('Digite o seu Peso (em KG): '))
altura = float(input('Digite a sua Altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu IMC é: {imc:.2f}')
    print('Você está Abaixo do Peso.')
elif imc >= 18.5 < 25:
    print(f'O seu IMC é: {imc:.2f}')
    print('Você está no Peso Ideal.')
elif imc >= 25:
    print(f'O seu IMC é: {imc:.2f}')
    print('Você está Acima do Peso.')
else:
    print('Algo deu Errado!')