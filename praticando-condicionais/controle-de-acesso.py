horario = int(input('Digite o Horário Atual (Formato 24 Horas): '))
if 8 <= horario < 18:
    print('Acesso Autorizado.')
else:
    print('Acesso Negado.')