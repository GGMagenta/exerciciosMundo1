# Pegue o preço e calcule o desconto
preco = float(input('qual o preco? '))
des = float(input('qual o desconto? '))
print('o novo preco com {}% de desconto e {}'.format(des,preco*(1-des/100)))
print(preco - (preco * des / 100))
