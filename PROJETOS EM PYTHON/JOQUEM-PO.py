from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-=' * 10)
print('Compurador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if computador == 0:    #   Computador jogou pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('Jogada invalida!')
elif computador == 1 :  #   Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('Jogada invalida!')

elif computador == 2:  # COMP JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE VENCE')

    else:
        print('Jogada invalida!')
