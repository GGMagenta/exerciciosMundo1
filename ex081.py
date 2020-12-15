# Pegue varios números e coloque na lista, depois mostre:
# quantos números tem na lista, a lista em ordem decrescente, e se tem o número 5
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n]').strip()[0]
    if opcao in 'Nn':
        break
print(f'lista final\n{lista}')
print(f'A lista tem {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente é\n{lista}')
n5 = lista.count(5)
# if 5 in lista
if n5 > 0:
    print(f'O número 5 aparece {n5} vezes na lista.')
else:
    print('O número 5 não está na lista.')
