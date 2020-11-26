# Pegar a velocidade do carro, se passar de 80Km/h, aplicar uma multa de R$7.00 a cada kilometro acima do limite
vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    acima = (vel-80)
    print('Esta {}Km/h acima do limite de 80Km/h, a multa e de R${:.2f}.'.format(acima, 7*acima))
else:
    print('Esta dentro do limite de velocidade.')
