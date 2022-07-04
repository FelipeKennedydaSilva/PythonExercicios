# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
print(f'O total a pagar é de R${(dias*60)+(km*0.15)}')