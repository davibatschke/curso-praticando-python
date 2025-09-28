def validar_cadastro(cpf):
    if not cpf.isdigit():
        return 'ERRO: O CPF Precisa conter Apenas Números.'
    if len(cpf) != 11:
        return 'CPF Inválido. Ele precisa conter 11 Caracteres.'
    return 'O CPF que Você digitou é Válido!'

cadastro_validar = input('Digite o seu CPF (Cadastro de Pessoa Física): ')
print(validar_cadastro(cadastro_validar))