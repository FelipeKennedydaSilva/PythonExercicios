n = int(input('Digite um número: '))
q = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        q += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[m0 Número {n} foi divisível {q} vezes')
if q == 2:
    print('ELE É PRIMO!')
else:
    print('ELE NÃO É PRIMO!')

