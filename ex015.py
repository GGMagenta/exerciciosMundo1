#Calcule o preço do aluguel de um carro
#R$60.00 por dia alugado + R$0.15 por kilometro rodado
dias = int(input('quantos dias o carro foi alugado? '))
km = float(input('quantos km ele rodou? '))
preco = 60 * dias + km * 0.15
print('o preco por dia ficou R${:.2f}, mais R${:.2f} da quilimetragem, com o total de R${:.2f}'.format((60*dias), (km * 0.15), preco))
