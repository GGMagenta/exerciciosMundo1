# Pegue um número e diga se ele é primo
n = int(input('Digite um número inteiro: '))
divisor = 0
for i in range(2, n):
    if n % i == 0 and divisor == 0:
        divisor = i
if divisor != 0:
    print('{} não é primo, seu menor divisor é {}'.format(n, divisor))
else:
    print('{} é primo.'.format(n))
