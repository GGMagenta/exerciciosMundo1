# Pegue o primeiro termo de uma PA e a razão e mostre até o 10 termo usando while
primeiro = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão:'))
termo = 0
while termo < 10:
    print(primeiro + razao * termo)
    termo += 1