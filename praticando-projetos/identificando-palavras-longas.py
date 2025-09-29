texto = input('Digite um Pequeno Texto: ')
palavras_longas = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)
if palavras_longas:
    print('Palavras Longas foram Encontradas:')
    for palavra in palavras_longas:
        print(palavra)
else:
    print('Nenhuma Palavra Longa foi Encontrada.')