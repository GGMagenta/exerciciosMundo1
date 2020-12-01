# Pegue números ate digitar 999, e mostre a soma desconsiderando o flag
cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número inteiro, e "999" para sair: '))
    if n != 999:
        cont+=1
        soma+=n
print('Você digitou {} números, e a soma total de todos é {}'.format(cont, soma))
# n = int(input('Digite um número inteiro, e "999" para sair: '))
# while n != 999:
#     cont+=1
#     soma+=n
#     n = int(input('Digite um número inteiro, e "999" para sair: '))
