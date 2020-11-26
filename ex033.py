# Ler 3 números e mostrar o maior e o menor
n1 = int(input('Digite o primeiro número: '))
maior = n1
menor = n1
n2 = int(input('Digite o segundo número: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = int(input('Digite o terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('Entre {}, {} e {}, o maior número é {}, e o menor é {}.'.format(n1, n2, n3, maior, menor))
