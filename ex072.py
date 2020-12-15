# Crie um tupla com números de 0 até 20 por extenso, depois pegue um número do teclado e mostre
palavras = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Valor inválido.')
    print(f'O número {n} por extenso se escreve: \033[1;33m{palavras[n]}\033[m.')
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n]').strip()[0]
    if opcao in 'Nn':
        break

