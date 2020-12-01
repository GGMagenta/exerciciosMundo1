# Jogue Par ou Ímpar com o computador e so pare quando perder, e mostre quantas vezes ganhou
from random import randint
from time import sleep
vitorias = 0
print('Vamos jogar Par ou ímpar!')
while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(1, 10)
    # print(computador)
    escolha = 'a'
    while escolha not in 'PpIi':
        escolha = input('Par ou Ímpar? [p/i] ').strip()[0]
    for i in range(3, 0, -1):
        print(f'{i}...')
        sleep(1)
    print(f'Jogador:{jogador}\nComputador:{computador}')
    sleep(1)
    if (jogador + computador) % 2 == 0:
        print(f'{jogador + computador} é PAR...')
        sleep(1)
        if escolha in 'Pp':
            print('Você ganhou! Vamos jogar novamente...')
        else:
            print('Você perdeu!')
            sleep(1)
            break
    else:
        print(f'{jogador + computador} é ÍMPAR...')
        sleep(1)
        if escolha in 'Ii':
            print('Você ganhou! Vamos jogar novamente...')
        else:
            print('Você perdeu!')
            sleep(1)
            break
    print('=-'*20)
print('=-'*20)
print(f'Você me venceu {vitorias} vezes.')
