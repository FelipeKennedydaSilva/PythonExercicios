# Classificando atletas
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade <= 9:
    print('Atleta Mirim!')
elif idade <= 14:
    print('Atleta Infantil!')
elif idade <= 19:
    print('Atleta Júnior!')
elif idade <= 25:
    print('Atleta Sênior!')
else:
    print('Atleta Master! ')