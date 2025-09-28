def calculando_idade():
    nascimento = int(input('Em que Ano Nasceu? '))
    ano = int(input('Digite o Ano Atual: '))
    soma = ano - nascimento
    print(f'Você tem {soma} anos!')

calculando_idade()