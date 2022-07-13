km = float(input('Qual é a distância da sua viagem? \n'))
print(f'você está prestes a começar uma viagem de {km}km')
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print(f'O preço da sua passagem será de R${valor:.2f}.')