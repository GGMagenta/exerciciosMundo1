# Pegue 2 números e compare para mostrar qual é maior ou se são iguais
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
    print('O maior valor é o do primeiro número.')
elif n2>n1:
    print('O maior valor é o do segundo número. ')
else:
    print('Os dois números tem o mesmo valor.')
