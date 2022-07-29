# Para existir um triângulo a soma entre dois lados tem que ser maior que o terceiro lado
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \nAnalisador de Triângulos \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima podem formar Triângulo ', end='')
    if a == b and b == c and c == a:
         print('Equilatero')
    if  a == b and b != c and a != c or c == b and a != c and b != a or a == c and a != b and c != b:
        print('Isosceles')
    if a != b and b != c and a != c:
        print('Escaleno')
else:
    print('Os segmentos acima não podem formar triângulo!')
