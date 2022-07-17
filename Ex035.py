# Para existir um triângulo a soma entre dois lados tem que ser maior que o terceiro lado

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \nAnalisador de Triângulos \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')
