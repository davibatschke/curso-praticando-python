limite_mensal = 3000.0
gastos = float(input('Digite o Total em Despesas do Mês (R$): '))
if gastos > limite_mensal:
    print('ATENÇÃO! Você passou do Limite Mensal!')
else:
    print('Você ainda está dentro do Limite Mensal, parabéns!')