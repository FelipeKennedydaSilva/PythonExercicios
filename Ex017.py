# Calculando a hipotenusa de um triângulo com a função math.hypot( * coordenadas )
import math
x = float(input('Comprimento de cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {math.hypot(x,y):.2f}')



