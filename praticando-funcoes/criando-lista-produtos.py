produto = input('Digite os Produtos (Separados por Vírgula): ').split(',')
precos = input('Digite os Preços (Separados por Vírgula): ').split(',')
for produto, precos in zip(produto, precos):
    print(f'{produto.strip()}: {precos.strip()}')