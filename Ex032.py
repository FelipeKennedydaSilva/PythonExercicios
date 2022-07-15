# Ano bissexto

ano = int(input('Qual o ano que você quer avaliar? \n'))
print('Avaliando seu ano...')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano avaliado {ano} é Bissexto')
else:
    print(f'O ano avaliado {ano} não é Bissexto')