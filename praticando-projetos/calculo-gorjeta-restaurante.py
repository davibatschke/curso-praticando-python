def calculo_final_gorjeta(conta, gorjeta):
    calculo_gorjeta = conta * (gorjeta / 100)
    return calculo_gorjeta + conta

try:
    valor_conta = float(input('Digite o Valor Total da Conta: '))
    porcentagem_gorjeta = float(input('Digite a Porcentagem da Gorjeta: '))

    resultado = calculo_final_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f'Valor total a Pagar: R${resultado:.2f}')
except ValueError:
    print('ERRO: Digite um Valor Válido.')