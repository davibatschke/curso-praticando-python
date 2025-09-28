maca = int(input('Digite a quantidade de MAÇÃS vendidas no Mês: '))
banana = int(input('Digite a quantidade de BANANAS vendidas no Mês: '))
if maca > banana:
    print('As Maçãs venderam mais.')
elif maca < banana:
    print('As Bananas venderam mais.')
else:
    print('Ambas venderam as mesmas quantidades.')