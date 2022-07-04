# Calculando o Seno, Cosseno e tangente de X -> está em radiano
import math
x = float(input('Digite o ângulo que voê deseja: '))
seno = math.sin(math.radians(x))
cosseno = math.cos(math.radians(x))
tangente = math.tan(math.radians(x))
print(f'O ângulo de {x} tem o SENO de {seno:.2f}')
print(f'O ângulo de {x} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {x} tem a TANGENTE de {tangente:.2f}')