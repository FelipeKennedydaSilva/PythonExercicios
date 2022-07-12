# Analisando o número se é par ou impar
# % módulo de uma divisão todo número par dividido por 2 não retorna resto então o resto é igual a 0.

numero = int(input('Digite um número qualquer: \n'))
print('Analisando seu número...')
x = numero % 2
if x == 0:
    print('Seu número é par!')
else:
    print('Seu número é ímpar!')
