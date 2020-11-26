#Pegue a largura e altura de uma parede e calcule a área e quantos litros de tinta necessarios para pintar
# 1 litro de tinta pinta 2m²
la = float(input('digite a largura: '))
al = float(input('digite a altura: '))
print('Com uma area de {}m², voce precisa de {} litros de tinta'.format(la*al, la*al/2))
