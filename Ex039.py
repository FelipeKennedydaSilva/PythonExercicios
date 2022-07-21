# Data de alistamento
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deeria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
