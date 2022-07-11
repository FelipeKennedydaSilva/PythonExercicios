# Gerando um numéro aleatorio randint(intervalo)
# importando a biblioteca random
# condições if e else, se então!

from random import randint
x = randint(0,5)
y = int(input('Pensei em um número entre 0 a 5, adivinhe qual é? \n'))
if y == x:
    print(f'Parabéns! o número que pensamos foi {x}')
else:
    print(f'Não foi dessa vez! o número que pensei foi {x}')
