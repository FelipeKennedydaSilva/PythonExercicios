# Calculando quanto de tinta é preciso para pintar uma parede, 2m² de parede = 1L tinta
L = float(input('Largura da parede: '))
A = float(input('Altura da parede: '))
area = L*A
print(f'Sua parede tem a dimensão de {L}x{A} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {area/2:.2f}l de tinta.')