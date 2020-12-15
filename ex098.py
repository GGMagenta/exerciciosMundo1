# Crie uma função contador que pegue o inicio, fim e passo
# de 1 ate 10 em 1 em 1, de 10 a 0 de 2 em 2, e uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} com passo {passo}.')
    if fim < inicio:
        passo *= -1
        fim -= 1
    else:
        fim += 1
    sleep(1)
    #  while inicio < fim:
    for i in range(inicio, fim, passo):
        print(f'{i}', end=', ')
        # caso crie um buffer e não mostre o sleep corretamente, colocar no fim do print flush=False
        sleep(0.5)
    print('FIM')


# main
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada!')
i = int(input('Qual o início? '))
f = int(input('Qual o fim? '))
p = int(input('Qual o passo? '))
contador(i, f, p)
