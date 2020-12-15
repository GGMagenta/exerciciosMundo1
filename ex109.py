# Reaproveite o moeda do exercicio 108 com um parâmetro opcional para mostar o valor formatado.
from ex109Dir import moeda

preco = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O aumento de 10% de {moeda.moeda(preco)} é {moeda.aumentar(preco, 10, True)}')
print(f'A redução de 13% de {moeda.moeda(preco)} é {moeda.diminuir(preco, 13, True)}')
print(moeda.dobro(preco), moeda.dobro(preco, True))
print(moeda.metade(preco), moeda.metade(preco, True))
print(moeda.aumentar(preco, 10), moeda.aumentar(preco, 10, True))
print(moeda.diminuir(preco, 13), moeda.diminuir(preco, 13, True))

# return res if f is false else return moeda(res)
