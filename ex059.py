# Pegar 2 valores e mostrar o menu do que fazer com os valores
operacao = 0
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print("""Operações disponiveis:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair""")
operacao = 0
while operacao != 5:
    operacao = int(input('Selecione a operação: '))
    if operacao == 1:
        print('A soma entre {} e {} é igual a {}'.format(v1,v2,v1 + v2))
    elif operacao == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(v1, v2, v1 * v2))
    elif operacao == 3:
        if v1 > v2:
            print('Entre {} e {} o maior é {}'.format(v1,v2,v1))
        elif v2>v1:
            print('Entre {} e {} o maior é {}'.format(v1, v2, v2))
        else:
            print('Os 2 números são iguais.')
    elif operacao == 4:
        print('Você escolheu selecionar novos números.')
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
    elif operacao == 5:
        print('Você escolheu sair do programa.')
    else:
        print('Valor invalido.')
print('Programa finalizado.')