# Procurando um nome dentro de um texto
# .lower coloca em minúscula
# in está contido

texto = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Silva {"silva" in texto.lower()}')