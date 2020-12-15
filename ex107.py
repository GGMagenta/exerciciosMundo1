# Crie o módulo moeda.py com as funções aumentar, diminuir, dobro e metade
from ex107Dir import moeda

preco = float(input('Digite o preço: R$'))
print(f'O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}')
print(f'A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}')
print(f'O aumento de 10% de {preco} é R${moeda.aumentar(preco, 10):.2f}')
print(f'A redução de 13% de {preco} é R${moeda.diminuir(preco, 13):.2f}')
