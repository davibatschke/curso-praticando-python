valores = input('Digite o Valor das Vendas: ').split()
total = sum(map(float, valores))
print(f'O total de Vendas foi {total}')