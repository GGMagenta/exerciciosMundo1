# Pegue 5 valores e coloque na lista  na ordem certa sem usar o sort
lista = []
for i in range(0, 5):
    n = int(input('Digite um número: '))
    if i == 0:
        print('Primeiro elemento adicionado.')
        lista.append(n)
    else:
        if n >= lista[len(lista) - 1]:  # lista[-1]
            print('Colocado no final da lista.')
            lista.append(n)
        else:
            for j in range(0, len(lista)):  # while
                if n <= lista[j]:
                    print(f'Colocado na posição {j}')
                    lista.insert(j, n)
                    break
print(lista)