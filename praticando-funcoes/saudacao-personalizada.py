def saudacao_personalizada():
    hora = int(input('Digite a Hora Atual (0-23): '))
    if hora <= 12:
        print('Bom Dia!')
    elif hora <= 18:
        print('Boa Tarde!')
    else:
        print('Boa Noite!')

saudacao_personalizada()