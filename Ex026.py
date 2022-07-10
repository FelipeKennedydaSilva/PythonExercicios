# Quantas vezes aparece a letra A no texto .count
# Posição da primeira letra A .find
# Posição da ultima letra A .rfind

texto = str(input('Escreva um texto: ')).upper().strip()
print(f'A letra A aparece {texto.count("A")} vezes no texto.')
print(f'A primeira letra A apareceu na posição {texto.find("A")+1}.')
print(f'A ultima letra A apareceu na posição {texto.rfind("A")+1}.')
