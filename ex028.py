# O computador "escolhe" um número entre 0 e 5, e diz se o jogador acertou ou errou.
# from time import sleep
from random import randint
nCom = randint(0, 5)
nPlayer = int(input('Estou pensando em um número entre 0 e 5, qual é? '))
# print('Processando...')
# sleep(3)
if nPlayer == nCom:
    print('Você acertou!')
else:
    print('Errou, o numero era {}'.format(nCom))
