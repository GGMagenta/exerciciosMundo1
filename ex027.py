# Pegue o nome e liste o primeiro e o último separadamente
nome = input('Digite seu nome completo: ').strip()
lista = nome.split()
print('Nome completo: {}'.format(nome))
print('Primeiro nome: {}'.format(lista[0]))
print('Último nome: {}'.format(lista[len(lista)-1]))
# lista.reverse()
# print('Último nome: {}'.format(lista[0]))
