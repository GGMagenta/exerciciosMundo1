# Crie uma lista e 2 funções, uma para sortear 5 números e por na lista,
# e outra para somar os números pares da mesma lista
from random import randint
from time import sleep


def sorteia(list):
    print('Sorteando 5 números: ', end='')
    sleep(1)
    for i in range(0, 5):
        n = randint(0, 10)
        list.append(n)
        print(f'{n}... ', end='')
        sleep(0.5)
    print('Pronto.')


def somaPar(list):
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos os números pares de {list} é {soma}.')


# main
lista = []
sorteia(lista)
# sorteia(lista)
sleep(1)
somaPar(lista)
