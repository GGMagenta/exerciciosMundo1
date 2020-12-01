# Faca o computador pensar entre um número entre 0 e 10 e o jogador advinhar
#Repita até adivinhar e mostre em quantas tentativas
from random import randint
n = str(randint(0, 10))
# print(n)
tentativas = 1
print('Estou pensando em um número inteiro entre 0 e 10!')
palpite = input('Qual o número? ')
while n != palpite:
    tentativas += 1
    if palpite.isnumeric():
        palpite = input('Errou, digite outro número e tente novamente: ')
    else:
        palpite = input('Valor invalido! Digite um número inteiro e tente novamente: ')
print('Acertou, pensei no número {}, e você precisou de {} tentativas!'.format(n, tentativas))