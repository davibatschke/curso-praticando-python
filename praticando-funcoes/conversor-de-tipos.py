def conversor_tipos(lista):
    return [int(telefone) for telefone in lista]

def verificando_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            print('Erro durante Conversão.')

    print('Todos os Números foram Convertidos.')

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
telefone_convertido = conversor_tipos(telefones)
print(verificando_tipos(telefone_convertido))