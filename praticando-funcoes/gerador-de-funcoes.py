def criar_desconto(porcentagem):
    def calcular_preco(valor):
        return valor - (valor *(porcentagem / 100))
    return calcular_preco
desconto = float(input('Digite o Valor (Porcentagem) do Desconto: '))
calcular_preco_final = criar_desconto(desconto)
valor = float(input('Digite o Valor da Compra: '))
print(f'Preço do Produto Final com Descontos: {calcular_preco_final(valor)}')