# Pegue 7 números e coloque em uma única lista separando pares e ímpares
# depois mostre em ordem crescente
lista = [[], []]  #0 par 1 ímpar
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}° valor: '))
    if n % 2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os números pares digitados foram:\n{lista[0]}')
print(f'Os números ímpares digitados foram:\n{lista[1]}')
