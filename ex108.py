# Reaproveite o moeda do exercicio 107 com uma nova função para mostar o valor formatado.
from ex108Dir import moeda

preco = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}')
print(f'O aumento de 10% de {moeda.moeda(preco)} é {moeda.aumentar(preco, 10)}')
print(f'A redução de 13% de {moeda.moeda(preco)} é {moeda.diminuir(preco, 13)}')
