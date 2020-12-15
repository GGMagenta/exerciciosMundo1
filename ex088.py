# crie um programa para preguntar quantos jogos deseja fazer e dar 6 palpites de 1 a 60
from random import randint
from time import sleep
quantidade = int(input('Quantos jogos quer fazer? '))
sleep(1)
todos = []
for i in range(0, quantidade):
    jogo = []
    for j in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                break
    jogo.sort()
    todos.append(jogo[:])
for i, j in enumerate(todos):
    print(f'Jogo {i + 1}:\n{j}\n')
    sleep(1)
print('Programa finalizado.')

"""for i in range(0, quantidade):
    print(f'Jogo {i + 1}')
    print('=-' * 25)
    jogo = []
    for j in range(0, 6):
        while True:
            n = int(input(f'Número {j + 1} [De 0 a 60]: '))
            if 0 < n <= 60 and n not in jogo:
                jogo.append(n)
                break
            else:
                print('Número inválido')
    todos.append(jogo[:])
    print(f'Jogo {i + 1} cadastrado.\n\n')
for i in todos:
    print(i)"""
