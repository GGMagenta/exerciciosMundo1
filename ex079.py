# Pegue varios números, e so adicione na lista caso seja único, no fim mostre em ordem crescente
lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        print('Valor adicionado.')
        lista.append(n)
    else:
        print('Valor já existe na lista.')
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n]').strip()[0]
    if opcao in 'Nn':
        break
print('=-'*25)
lista.sort()
print(f'A lista final em ordem crescente é:\n{lista}')