# Calculo de massa corporea IMC= peso/altura2
# expoente pow(altura, y)
peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / pow(altura, 2)
print(f'Seu Índice de Massa Corpórea é {imc:.1f}, ', end="")
if imc < 18.5:
    print('ABAIXO DO PESO.')
elif imc > 25 and imc < 30:
    print('SOBREPESO.')
elif imc > 30 and imc < 40:
    print('OBESIDADE.')
elif imc > 40:
    print('OBESIDADE MÓRBIDA.')
else:
    print('Parabéns, PESO IDEAL.')