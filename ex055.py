# Pegue 5 pesos e mostre o maior e o menor
peso = float(input('Digite o peso em Kg: '))
maior = peso
menor = peso
for i in range(0, 4):
    peso = float(input('Digite o peso em Kg: '))
    if peso> maior:
        maior = peso
    elif peso < menor:
        menor = peso
if maior == menor:
    print('Parece que todos tem o mesmo peso de {}Kg!'.format(maior))
else:
    print('O maior peso registrado é {}Kg, e o menor é {}Kg.'.format(maior,menor))
