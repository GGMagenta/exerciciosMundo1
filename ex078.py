# Pegue 5 números e guarde em uma lista, mostre o maior e o menor em suas posições
Maior = 0
Menor = 0
lista = []
for i in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
    if i == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(lista)
print(f'O maior número da lista é {maior} na posições: ', end='')
# for pos, i in enumerate(lista):
for i in range(0, len(lista)):
    if lista[i] == maior:
        print(f'{i} ', end='')
print('')
print(f'O menor número da lista é {menor} na posições: ', end='')
for i in range(0, len(lista)):
    if lista[i] == menor:
        print(f'{i} ', end='')
print('')