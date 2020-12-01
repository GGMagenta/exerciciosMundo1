# Leia 6 números e mostre a soma dos pares
soma = 0
for i in range(1, 7):
    n = int(input('Digite un número inteiro: '.format(i)))
    if n % 2 == 0:
        soma+=n
print('Dos 6 números que você digitou, a soma dos números pares é igual a {}.'.format(soma))
