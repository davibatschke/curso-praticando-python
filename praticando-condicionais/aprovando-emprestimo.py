valor_renda = float(input('Digite o Valor da sua Renda Mensal: '))
valor_desejado = float(input('Digite o Valor da Parcela Desejada: '))

if valor_renda > 2000 and valor_desejado <= 0.3 * valor_renda:
    print('O seu Empréstimo foi Aprovado!')
elif valor_renda < 2000:
    print('O seu Empréstimo foi Negado! Devido a Renda Insuficiente.')
else:
    print('O seu Empréstimo foi Negado! Devido a Parcela Acima de 30%.')