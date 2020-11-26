# Pege o comprimento de 3 retas e diga se formam um triângulo
reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('Comprimento da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possivel formar o triângulo com as retas.')
else:
    print('Não é possivel formar o triângulo com as retas.')
