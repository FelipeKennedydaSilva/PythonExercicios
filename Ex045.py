# Jogo Pedra / Papel / Tesoura
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if computador == 0 and jogador == 1:
    print('JOGADOR VENCE')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCE')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCE')
elif computador == 1 and jogador == 2:
    print('JOGADOR VENCE')
elif computador == 2 and jogador == 0:
    print('JOGADOR VENCE')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENCE')
elif computador == jogador:
    print('EMPATE')
else:
    print('OPÇÃO INVÁLIDA')
