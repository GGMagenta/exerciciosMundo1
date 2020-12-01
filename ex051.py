# digite o primeiro termo e a razão de uma PA e mostre ate o decimo termo
n1 = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
print('Na PA com primeior termo de {} e razão de {}, os 10 primeiros termos são:'.format(n1, ra))
for i in range(0, 10):
    print(n1+ra*i)
