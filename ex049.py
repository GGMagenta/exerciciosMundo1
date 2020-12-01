# Faça uma tabuada usando for
n = int(input('Escolha um número inteiro: '))
print('Agora veja a tabuada do número {}'.format(n))
for i in range(1, 11):
    print('{:<2} x {:<2} = {:<3}'.format(n, i, n*i))
print('-+'*20)