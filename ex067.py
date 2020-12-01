# Pegue um número e mostre a tabuada ate o usuario digitar um número negativo
while True:
    numero = int(input('Digite um número inteiro e \033[1;32mpositivo\033[m: '))
    if numero < 0:
        break
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero * i}')
        i += 1
    print('='*20)
print('Você digitou um número \033[1;31mnegativo\033[m, o programa será encerrado.')
