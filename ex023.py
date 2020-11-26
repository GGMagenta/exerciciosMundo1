# Pegue um numero de ate 4 digitos e mostre separadamente
n = input('Digite um numero de 0 a 9999: ')
n1 = int(n)
un = n1 // 1 % 10
de = n1 // 10 % 10
ce = n1 // 100 % 10
mi = n1 // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(un, de, ce, mi))
