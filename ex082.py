# Pegue varios números, depois separe em mais duas listas,
# uma com números pares, e outra com números ímpares
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n]').strip()[0]
    if opcao in 'Nn':
        break
pares = []
impares = []
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista com todos os números:\n{lista}')
print(f'Lista com os números pares:\n{pares}')
print(f'Lista com os números ímpares:\n{impares}')