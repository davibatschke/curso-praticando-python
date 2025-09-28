def quantidade_vogais(texto):
    vogais = 'aeiou'
    quantidade = 0

    for letra in texto.lower():
        if letra in vogais:
            quantidade += 1
    return quantidade

texto = input('Digite um Pequeno Texto: ')
print(f'O Texto contém: {quantidade_vogais(texto)} Vogais.')