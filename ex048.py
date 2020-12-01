# soma de todos os números ímpares multiplos de 3 entre 1 e 500
soma = 0
print('Veja a soma de todos os números ímpares multiplos de 3 entre 1 e 500')
#for i in range(1,501):
#    if i % 3 == 0 and i % 2 !=0:
#        soma += i
for i in range(3, 501, 3):
    if i % 2 !=0:
        soma += i
print('A soma é \033[1;31m{}'.format(soma))
