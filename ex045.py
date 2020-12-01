# Crie um jogo de pedra papel e tesoura
from random import choice
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
print('\033[1;32m='*32)
print('\033[4;30;44mJogo de pedra, papel ou tesoura!\033[m')
print('\033[1;32m=\033[m'*32)
sleep(1)
escolha = int(input('Digite 1 para pedra, 2 para papel e 3 para tesoura: '))
if escolha<1 or escolha>3:
    jogador = choice(lista)
    print('Escolha invalida, então vou escolher {} por você.'.format(jogador))
else:
    jogador = lista[escolha-1]
    print('Você escolheu {}'.format(jogador))
sleep(1)
print('O computador está escolhendo...')
computador = choice(lista)
sleep(2)
print('Pronto?')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Você: {}'.format(jogador))
print('Computador: {}'.format(computador))
sleep(3)
if jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    print('Você ganhou!')
elif jogador==computador:
    print('Empatou.')
else:
    print('Você perdeu...')

