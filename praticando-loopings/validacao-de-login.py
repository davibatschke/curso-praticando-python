while True:
    username = input('Digite um Nome de Usuário: ')
    password = input('Digite uma Senha: ')

    if len(username) < 5:
        print('Nome de Usuário muito curto.')
        continue

    if len(password) < 8:
        print('Senha muito curta.')
        continue

    print(f'Parabéns {username}! Cadastro Finalizado!')
    break