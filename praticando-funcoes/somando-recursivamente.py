def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)
numero = int(input('Digite um Valor para N: '))
print(f'A soma de 1 até {numero} é igual a: {soma_recursiva(numero)}')