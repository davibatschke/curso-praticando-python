nota_um = float(input('Digite a Primeira Nota: '))
nota_dois = float(input('Digite a Segunda Nota: '))
nota_tres = float(input('Digite a Terceira Nota: '))
media = (nota_um + nota_dois + nota_tres) / 3
print(f'A média do Aluno é: {media:.1f}')
if media >= 7:
    print('Aluno está Aprovado.')
elif 5 <= media < 7:
    print('Aluno está de Recuperação.')
elif 5 > media:
    print('Aluno está Reprovado.')
else:
    print('Houve um ERRO no Sistema...')