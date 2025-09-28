quantidade_livros = 5
while quantidade_livros > 0:
    quantidade_livros -= 1
    print(f'Venda Realizada! Estoque atual: {quantidade_livros}')

    if quantidade_livros == 0:
        print('Estoque Esgotado.')