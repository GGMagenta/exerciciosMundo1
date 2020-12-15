# Crie uma tupla com 5 números aleatórios, mostre eles e diga qual o maior e menor
from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Tupla inteira:\n{tupla}')
maior = menor = tupla[0]
for n in range(1, len(tupla)):
    if tupla[n] > maior:
        maior = tupla[n]
    elif tupla[n] < menor:
        menor = tupla[n]
print(f'O maior número é {maior}, e o menor é {menor}.')
#print(f'O maior número é {max(tupla)}, e o menor é {min(tupla)}.')
