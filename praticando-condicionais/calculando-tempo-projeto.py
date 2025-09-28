# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
dia_um = int(input('Informe o Dia para a Atividade A: '))
dia_dois = int(input('Informe o Dia para a Atividade B: '))
dia_tres = int(input('Informe o Dia para a Atividade C: '))
if dia_um < 0 or dia_dois < 0 or dia_tres < 0:
    print('Os dias NÃO podem ser negativos.')
else:
    tempo_total = dia_um + dia_dois + dia_tres
    print(f'O Tempo Total do Projeto é de: {tempo_total} Dias.')