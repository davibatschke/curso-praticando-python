distancia = int(input('Digite a Distância percorrida (em KM): '))
if distancia <= 100:
    print('O valor do Pedágio fica R$10,00')
elif 100 <= distancia <= 200:
    print('O valor do Pedágio fica R$20,00')
else:
    print('O valor do Pedágio fica R$30,00')