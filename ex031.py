# Calcular a distancia da viagem com o preço de R$0.50, e para viagens acima de 200Km, o preço de R$0.45
km = int(input('Quantos kilometros tem a viagem? '))
if km <= 200:
    print('Será cobrado R$0.50 para cada kilometro, totalizando R${:.2f}'.format(km * 0.5))
else:
    print('Será cobrado R$0.45 para cada kilometro, totalizando R${:.2f}'.format(km * 0.45))
# preco = km * 0.5 if km <= 200 else km * 0.45
# print('O valor total será de R${:.2f}'.format(preco))
