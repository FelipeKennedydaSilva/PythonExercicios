# Divide um texto em uma lista .split()
# Conta quantos objetos tem em uma lista len

texto = str(input('Escreva um texto: ')).strip()
listatx = texto.split()
print(f'Seu texto é: \n {texto}.')
print(f'O primeiro nome que apareceu foi: {listatx[0]}.')
print(f'O ultimo nome que apareceu foi: {listatx[len(listatx)-1]}.')