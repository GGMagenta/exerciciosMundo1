# Crie a função maior que recebe vários parâmetros e mostre o maior
from time import sleep


def maior(* numeros):
    ma = 0
    print('Analizando números:')
    sleep(1)
    for i, n in enumerate(numeros):
        print(f'{n}', end='... ')
        sleep(0.5)
        if n > ma or i == 0:
            ma = n
    print(f'\nDe todos os {len(numeros)} números analizados, o de maior valor é {ma}.')
    print('=' * 20)
    sleep(1)


# main
maior(1, 2, 3, 5, 4, 7)
maior(2, 9, 3, 8, 4, 1, 7, 0)
maior(-3, -5, -2, -10)
maior(0, 0, 1, 1, 2, 2, 4, 4, 9, 6, 9, 6)
maior(6)
maior()
