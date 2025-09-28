num1 = int(input('Digite o Primeiro Valor: '))
num2 = int(input('Digite o Segundo Valor: '))
operador = input('Escolha uma Operação (+, -, *, /): ')
if operador == '+':
    soma = lambda a, b: a + b
    print(soma(num1, num2))
elif operador == '-':
    subtra = lambda a, b: a - b
    print(subtra(num1, num2))
elif operador == '*':
    multip = lambda a, b: a * b
    print(multip(num1, num2))
elif operador == '/':
    divis = lambda a, b: a / b if b != 0 else 'Syntax ERROR.'
    print(divis(num1, num2))
else:
    print('Syntax ERROR.')