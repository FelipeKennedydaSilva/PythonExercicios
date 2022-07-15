# Ano bissexto
# importando o ano atual
from datetime import date
ano = int(input('Qual o ano que você quer avaliar? \nColoque 0 para analisar o ano atual. \n '))
print('Avaliando seu ano...')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano avaliado {ano} é Bissexto')
else:
    print(f'O ano avaliado {ano} não é Bissexto')