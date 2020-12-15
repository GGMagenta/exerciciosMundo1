# Crie uma tupla com nomes e preços de produto e mostre de forma tabulada
lista = ('Caneta', 3.05, 'Borracha', 4, 'caderno', 15.5, 'mochila', 80.99, 'livro', 150.52)
print('-'*30)
print('{:^30}'.format('Lista de Preços'))
print('-'*30)
for item in range(0, len(lista), 2):
    print(f'{lista[item]:-<20} R${lista[item + 1]:>6.2f}')
# for item in range(0, len(lista)):
#       if item % 2 == 0:
#       print produto
#       else:
#       print preço
