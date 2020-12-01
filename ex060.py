# Pegue um número e mostre o fatorial usando while
fatorial = 1
n = int(input('Digite um número inteiro para calcular o fatorial: '))
numero = n
# for i in range(i, 1, -1):
while n > 1:
    fatorial *= n
    print(n, end=' *\n')
    n -= 1
print('1 =\n{}'.format(fatorial))
print('{}! = {}'.format(numero, fatorial))
