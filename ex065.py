# Pegue varios números e calcule a média, o maior e menor valor, perguntando se quer por mais números
maior = 0
menor = 0
cont = 1
soma = 0
media = 0
opcao = 's'
n = int(input('Digite um número: '))
maior = menor = soma = media = n
while opcao == 's':
    opcao = input('Quer digitar outro valor?[s/n] ').lower().strip()
    if opcao == 's':
        n = int(input('Digite outro número: '))
        if n > maior:
            maior=n
        elif n < menor:
            menor = n
        cont += 1
        soma += n
    elif opcao == 'n':
        print('Finalizando programa...')
        media = soma / cont
    else:
        print('Opção invalida.')
        opcao = 's'
print('Você digitou {} números, o maior é {}, o menor é {}, e a média de todos é {}'.format(cont, maior, menor, media))