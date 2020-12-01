# Pegue 3 retas e veja se formam um triângulo, e qual tipo
# Escaleno - sem lados iguais   Isósceles - 2 lados iguais   Equilatero - 3 lados iguais
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print('É possivel formar um triângulo!')
    # r1 == r2 == r3
    if r1==r2 and r2==r3:
        print('Todos os lados são iguais, então é um triângulo equilátero.')
    elif r1==r2 or r2==r3 or r1==r3:
        print('Tem 2 lados iguais, então é um triângulo isósceles.')
    # r1 != r2 != r3 != r1
    else:
        print('Todos os lados são diferentes, entâo é um triângulo escaleno')
else:
    print('Não é possivel formar um triângulo.')
