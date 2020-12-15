#Pegue 4 números e guarde em um tupla, e mostre quantos 9 foram digitados, a posicção do número 3 e quantos números pares
tupla = (int(input('Digite o primeiro valor: ')),
         int(input('Digite o segundo valor: ')),
         int(input('Digite o terceiro valor: ')),
         int(input('Digite o quarto valor: ')))
n9 = tupla.count(9)
print(f'O número 9 apareceu {n9} vezes;')
if 3 in tupla:
    print(f'O primeiro número 3 está na posição {tupla.index(3)} da tupla.')
else:
    print('Não tem o número 3 na tupla.')
print('Os números pares são: ')
for i in tupla:
    if i % 2 == 0:
        print(i)
