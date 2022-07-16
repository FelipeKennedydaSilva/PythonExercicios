# Calcualndo aumento de salário

valor = float(input('Qual é o salário do funcionário?\n'))
if valor <= 1250:
    x = (valor / 100) * 115
    y = x - valor
else:
    x = (valor / 100) * 110
    y = x - valor
print(f'O funcionário que ganhava R${valor:.2f}, terá um aumento de R${y:.2f}, seu novo salário será R${x:.2f}.')
